#!/usr/bin/env python3
__author__ = 'aydar'

import sys, psutil


def check_cpu():
    cpu = psutil.cpu_percent()
    if cpu <= 40:
        print("Done " + str(cpu))
        sys.exit(0)
    elif 40 < cpu <= 70:
        print("Alert, cpu is " + str(cpu))
        sys.exit(1)
    elif 70 < cpu:
        print("Alarm! cpu is " + str(cpu))
        sys.exit(2)
    else:
        sys.exit(10)


print(check_cpu())