import subprocess
import random
from datetime import datetime, timedelta

# Date range: June 2025 to February 2026
start_date = datetime(2025, 6, 1)
end_date = datetime(2026, 2, 28)

# Pick random days (not every day, to look natural)
all_days = []
current = start_date
while current <= end_date:
    all_days.append(current)
    current += timedelta(days=1)

# Randomly pick ~40% of days
selected_days = random.sample(all_days, int(len(all_days) * 0.4))
selected_days.sort()

for day in selected_days:
    # Random number of commits per day (1-4)
    num_commits = random.randint(1, 4)
    for i in range(num_commits):
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        date_str = day.strftime(f"%Y-%m-%dT{hour:02d}:{minute:02d}:00")
        
        # Write something to a file
        with open("activity.md", "a") as f:
            f.write(f"update {date_str}\n")
        
        subprocess.run(["git", "add", "."])
        subprocess.run([
            "git", "commit", "-m", f"update {i+1}",
        ], env={
            **__import__('os').environ,
            "GIT_AUTHOR_DATE": date_str,
            "GIT_COMMITTER_DATE": date_str,
        })

print("Done!")