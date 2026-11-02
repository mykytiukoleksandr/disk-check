# 1. ask for total disk size (GB)

total = float(input("Total disk size (GB): "))
if total == 0:
    print("Error: total disk size cannot be zero")
    exit()

# 2. ask for used space (GB)

used = float(input("Used space (GB): "))

# 3. calculate usage percent

if used > total:
    print("Error: used space cannot exceed total")
    exit()

usage_percent = used / total * 100

# 4. print the percent with one decimal

print(f"Disk usage: {usage_percent:.1f}%")

# 5. print WARNING if above 80, otherwise OK    

if usage_percent > 80:
    print("WARNING: disk is almost full")
else:
    print("OK")