#!/usr/bin/env python3
"""Geser timing subtitle .srt."""
import sys, re
src, delta = sys.argv[1], float(sys.argv[2])
def shift(m):
      h, mn, s = int(m.group(1)), int(m.group(2)), float(m.group(3)) + delta
      mn += int(s // 60); s %= 60; h += mn // 60; mn %= 60
      return f"{h:02d}:{mn:02d}:{s:06.3f}".replace(".", ",")
  out = re.sub(r"(\d{2}):(\d{2}):(\d{2},\d{3})", shift, open(src, encoding="utf-8-sig").read())
open(src.replace(".srt", "_shift.srt"), "w", encoding="utf-8").write(out)
print("saved:", src.replace(".srt", "_shift.srt"))
