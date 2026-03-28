#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path


def load_options():
    with open("/data/options.json", "r", encoding="utf-8") as f:
        return json.load(f)


def build_url(host, port, freq, service_id, pids, profile):
    return f"http://{host}:{port}?freq={freq:.1f}&serviceId={service_id}&pids={pids}&profile={profile}"


def probe_stream(url, timeout_seconds):
    cmd = [
        "ffprobe",
        "-v", "error",
        "-rw_timeout", "5000000",
        "-analyzeduration", "2M",
        "-probesize", "2M",
        "-show_entries", "stream=codec_type",
        "-of", "json",
        "-i", url,
    ]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return False, "timeout"

    out = (proc.stdout or "") + "\n" + (proc.stderr or "")
    try:
        data = json.loads(proc.stdout or "{}")
    except json.JSONDecodeError:
        return False, out.strip()[:400]

    streams = data.get("streams", [])
    has_video = any(s.get("codec_type") == "video" for s in streams)
    has_audio = any(s.get("codec_type") == "audio" for s in streams)

    if has_video and has_audio:
        return True, "video+audio"
    if has_video:
        return True, "video_only"

    if proc.returncode != 0:
        return False, out.strip()[:400]

    return False, "no_streams"


def rank(detail):
    if detail == "video+audio":
        return 3
    if detail == "video_only":
        return 1
    return 0


def main():
    opts = load_options()
    host = opts["bridge_host"]
    port = int(opts["bridge_port"])
    freqs = [float(x) for x in opts["frequencies"]]
    service_ids = [int(x) for x in opts["service_ids"]]
    pid_candidates = list(opts["pid_candidates"])
    channel_hints = dict(opts.get("channel_hints", {}))
    profile = opts.get("profile", "pass")
    timeout_seconds = int(opts.get("timeout_seconds", 10))
    output_m3u = Path(opts.get("output_m3u", "/share/genidtv_channels.m3u"))

    print(f"[Q41 Scanner] bridge={host}:{port} profile={profile}")
    print(f"[Q41 Scanner] output={output_m3u}")

    results = []

    for freq in freqs:
        for service_id in service_ids:
            key = f"{freq:.1f}:{service_id}"
            channel_name = channel_hints.get(key, f"CH_{freq:.1f}_{service_id}")
            best = None
            best_rank = -1

            for pids in pid_candidates:
                url = build_url(host, port, freq, service_id, pids, profile)
                ok, detail = probe_stream(url, timeout_seconds)
                print(
                    f"[Q41 Scanner] test channel={channel_name} "
                    f"freq={freq:.1f} sid={service_id} pids={pids} -> {detail}"
                )

                if ok and rank(detail) > best_rank:
                    best = {
                        "name": channel_name,
                        "freq": freq,
                        "service_id": service_id,
                        "pids": pids,
                        "url": url,
                        "detail": detail,
                    }
                    best_rank = rank(detail)
                    if best_rank >= 3:
                        break

            if best is not None:
                results.append(best)

    deduped = {}
    for item in results:
        name = item["name"]
        current = deduped.get(name)
        if current is None or rank(item["detail"]) > rank(current["detail"]):
            deduped[name] = item

    output_m3u.parent.mkdir(parents=True, exist_ok=True)
    lines = ["#EXTM3U", ""]
    for name in sorted(deduped.keys()):
        item = deduped[name]
        lines.append(f"#EXTINF:-1,{name}")
        lines.append(item["url"])
        lines.append("")

    output_m3u.write_text("\n".join(lines), encoding="utf-8")
    print(f"[Q41 Scanner] wrote {len(deduped)} channels to {output_m3u}")

    if deduped:
        for name in sorted(deduped.keys()):
            item = deduped[name]
            print(
                f"[Q41 Scanner] {name}: "
                f"freq={item['freq']:.1f} sid={item['service_id']} "
                f"pids={item['pids']} ({item['detail']})"
            )
    else:
        print("[Q41 Scanner] no working channels found")


if __name__ == "__main__":
    main()
