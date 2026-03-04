import re
from collections import Counter

log_file = "../logs/sample_auth.log"

failed_ips = []

pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

with open(log_file, "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            failed_ips.append(match.group(1))

ip_counts = Counter(failed_ips)

print("Top Failed Login IPs")
print("--------------------")

for ip, count in ip_counts.most_common():
    print(ip, "-", count, "failed attempts")

print("\nPotential Brute Force IPs")
print("-------------------------")

for ip, count in ip_counts.items():
    if count >= 5:
        print(ip, "triggered brute force threshold")
