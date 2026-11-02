# Disk Check Script

A simple Python script to calculate disk usage percentage and check its status based on user input.

---

## What the Script Does

1. Prompts the user for the total disk size (in gigabytes).
2. Prompts the user for the used disk space (in gigabytes).
3. Validates the input data (prevents division by zero and logical errors).
4. Calculates the disk usage percentage.
5. Prints the result rounded to one decimal place.
6. Outputs a `WARNING` if disk usage exceeds 80%, or `OK` if there is enough space.

---

## How to Run

Make sure you have Python 3 installed. Run the script in your terminal using the following command:

```bash
python3 disk_check.py
