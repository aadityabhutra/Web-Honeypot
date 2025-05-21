import json
from collections import Counter
import matplotlib.pyplot as plt

# Read log file
with open('attack_logs.json', 'r') as f:
    logs = [json.loads(line) for line in f.readlines()]

# Count attacks by path
path_counts = Counter(log['path'] for log in logs)

# Plot
plt.bar(path_counts.keys(), path_counts.values())
plt.xlabel('Path')
plt.ylabel('Number of Attacks')
plt.title('Attack Attempts by Path')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('attack_plot.png')
plt.show()

