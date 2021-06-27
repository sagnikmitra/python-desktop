from rich.progress import track
import time
for i in track(range(20), description="Working..."):
    print(f"Working {i}")
    time.sleep(0.5)
"""
The output is something like this:
Working 0
Working 1
Working 2
Working 3
Working 4
Working 5
Working 6
Working 7
Working 8
Working 9
Working... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
"""
