import json
from collections import Counter

# Read log file
with open('attack_logs.json', 'r') as f:
    logs = [json.loads(line) for line in f.readlines()]

# Count attacks by path
path_counts = Counter(log['path'] for log in logs)
print("Attack counts by path:")
for path, count in path_counts.items():
    print(f"{path}: {count}")

# Optional: Count by IP
ip_counts = Counter(log['ip'] for log in logs)
print("\nAttack counts by IP:")
for ip, count in ip_counts.items():
    print(f"{ip}: {count}")
