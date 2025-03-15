#!/usr/bin/env python3

import os
import sys
from glob import glob

d = os.path.basename(os.getcwd())
print(f"# {d}")

# todo is glob result always sorted
for webp in glob("*.webp"):
  print()
  print(f"## {webp}")
  print(f"![]({webp})")
