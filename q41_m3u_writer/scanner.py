#!/usr/bin/env python3
from pathlib import Path

OUTPUT = Path("/share/genidtv_channels.m3u")

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    content = """#EXTM3U

#EXTINF:-1,SBS
http://192.168.0.28:30012?freq=135.0&serviceId=1&pids=16,17,17,20&profile=pass

#EXTINF:-1,KBS1
http://192.168.0.28:30012?freq=129.0&serviceId=2&pids=32,33,33,36&profile=pass

#EXTINF:-1,KBS2
http://192.168.0.28:30012?freq=141.0&serviceId=2&pids=32,33,33,36&profile=pass

#EXTINF:-1,OBS
http://192.168.0.28:30012?freq=153.0&serviceId=1&pids=32,33,33,36&profile=pass

#EXTINF:-1,MBC
http://192.168.0.28:30012?freq=123.0&serviceId=1&pids=16,17,17,20&profile=pass

#EXTINF:-1,EBS1
http://192.168.0.28:30012?freq=147.0&serviceId=1&pids=16,17,17,20&profile=pass

#EXTINF:-1,EBS2
http://192.168.0.28:30012?freq=147.0&serviceId=2&pids=32,33,33,36&profile=pass
"""
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"[Q41 M3U] wrote {OUTPUT}")

if __name__ == "__main__":
    main()
