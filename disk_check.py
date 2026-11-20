import psutil
from datetime import datetime


def log_result(percent, limit, status, log_file="disk_check.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] usage={percent:.1f}% limit={limit:.1f}% status={status}\n"
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(line)

def ask_limit():
    while True:
        while True:
            try:
                percent = float(input("Percent: "))
                break
            except ValueError:
                print("Type numbers.")

        if 0 <= percent <= 100:
            print("Percent correct")
            return percent
        else:
            print("Type percent from 1 to 100")


def get_status(percent, limit=80):
    if percent > limit:
        return "WARNING: disk is almost full"
    else:
        return "OK"

path = "/"
limit = ask_limit()
disk = psutil.disk_usage(path)
status = get_status(disk.percent, limit)
log_result(disk.percent, limit, status)

total_gb = disk.total / (1024**3)
free_gb = disk.free / (1024**3)

print(
    f"Disk usage:({path}) {disk.percent:.1f}% (free: {free_gb:.1f} GB / total: {total_gb:.1f} GB)"
)

print(status)