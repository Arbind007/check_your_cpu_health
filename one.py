#!/usr/bin/env python3
from network import *
import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/"):
    print("Error! You are using have less than 20 percent of storage left try clearing out some clone data")
elif not check_cpu_usage():
    print("Error! Your  CPU usage is more tha 75 percent of memory. Please try by reducing some task")
elif not check_disk_usage("/") or not check_cpu_usage():
    print("Error! Both your cpu and disk has reached to computers max limit")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")

