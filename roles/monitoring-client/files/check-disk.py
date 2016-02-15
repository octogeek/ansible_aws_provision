#!/usr/bin/env python3
__author__ = 'aydar'

import shutil
import sys

def check_mountpoint(path):
    disk = shutil.disk_usage(path)
    state = (1 - disk.free/disk.total)*100
    if state <= 70:
        print(state)
        sys.exit(0)
    elif 70 < state <= 90:
        print("Alert, only 30% size is free")
        sys.exit(1)
    elif 90 < state <= 95:
        print("Alarm! less 10% size is free on disk from my storage")
        sys.exit(2)
    else:
        sys.exit(10)

if sys.argv[1]:
    point = sys.argv[1]
else:
    sys.exit(10)
print(check_mountpoint(point))