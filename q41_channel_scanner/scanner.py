#!/usr/bin/env python3
from pathlib import Path
import shutil

OUTPUT = Path("/share/genidtv_channels.m3u")
BACKUP = Path("/share/genidtv_channels.m3u.bak")

CHANNELS = [
    ("MBC",  "http://192.168.0.28:30012?freq=123.0&serviceId=1&pids=16,17,17,20&profile=pass"),
    ("KBS1", "http://192.168.0.28:30012?freq=129.0&serviceId=2&pids=32,33,33,36&profile=pass"),
    ("SBS",  "http://192.168.0.28:30012?freq=135.0&serviceId=1&pids=16,17,17,20&profile=pass"),
    ("KBS2", "http://192.168.0.28:30012?freq=141.0&serviceId=2&pids=32,33,33,36&profile=pass"),
    ("EBS1", "http://192.168.0.28:30012?freq=147.0&serviceId=1&pids=16,17,736,20&profile=pass"),
    ("EBS2", "http://192.168.0.28:30012?freq=147.0&serviceId=2&pids=32,33,736,36&profile=pass"),
    ("OBS",  "http://192.168.0.28:30012?freq=153.0&serviceId=1&pids=32,33,33,36&profile=pass"),
]

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    # 기존 파일 백업
    if OUTPUT.exists():
        shutil.copy2(OUTPUT, BACKUP)
        print(f"[Q41 M3U] backup saved -> {BACKUP}")

    lines = ["#EXTM3U", ""]

    for name, url in CHANNELS:
        lines.append(f"#EXTINF:-1,{name}")
        lines.append(url)
        lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"[Q41 M3U] wrote {len(CHANNELS)} channels")
    for name, _ in CHANNELS:
        print(f"[Q41 M3U] {name}")


if __name__ == "__main__":
    main()
