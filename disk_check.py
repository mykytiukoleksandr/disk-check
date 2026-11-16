def is_valid(total, used):
    if total <= 0 or used < 0 or total < used:
        return False
    else:
        return True

def calc_percent(used, total):
    return (used / total) * 100

def get_status(percent, limit=80):
    if percent > limit:
        return "WARNING: disk is almost full"
    else:
        return "OK"

total = float(input("Total disk size (GB): "))
used = float(input("Used space (GB): "))

if is_valid(total, used):
    usage_percent = calc_percent(used, total)
    status = get_status(usage_percent)

    print(f"Disk usage {usage_percent:.1f}%")
    print(status)
else:
    exit()