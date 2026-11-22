import re
from datetime import datetime, timedelta

log_file = "auth.log"
threshold = 5
time_window = timedelta(minutes=10)

failed_attempts = {}

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:
    if "Failed password" in line:
        ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
        time_match = re.search(r"^(\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2})", line)

        if ip_match and time_match:
            ip = ip_match.group(1)
            timestamp = datetime.strptime(
                time_match.group(1), "%b %d %H:%M:%S"
            )

            if ip not in failed_attempts:
                failed_attempts[ip] = []

            failed_attempts[ip].append(timestamp)

print("SOC BRUTE FORCE DETECTION")
print("-------------------------")

for ip, timestamps in failed_attempts.items():
    timestamps.sort()
    alert = False

    for start_time in timestamps:
        window_end = start_time + time_window

        count = sum(
            1 for t in timestamps
            if start_time <= t <= window_end
        )

        if count >= threshold:
            alert = True
            break

    print(f"IP Address: {ip}")
    print(f"Total Failed Attempts: {len(timestamps)}")

    if alert:
        print("ALERT: Possible Brute Force Attack!")
        print("Reason: 5 or more failed attempts within 10 minutes.")
    else:
        print("NORMAL: No brute force threshold detected.")

    print("-------------------------")
