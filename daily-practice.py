import subprocess
import random
from datetime import datetime, timedelta
import os

# Date range: June 2025 to February 2026
start_date = datetime(2025, 6, 1)
end_date = datetime(2026, 2, 28)

# Build list of all days
all_days = []
current = start_date
while current <= end_date:
    all_days.append(current)
    current += timedelta(days=1)

# Select 65% of days randomly
selected_days = random.sample(all_days, int(len(all_days) * 0.65))
selected_days.sort()

# 20% of selected days will be heavy days (20 commits)
heavy_days_count = int(len(selected_days) * 0.20)
heavy_days = set(random.sample(range(len(selected_days)), heavy_days_count))

for idx, day in enumerate(selected_days):
    if idx in heavy_days:
        num_commits = random.randint(18, 22)  # ~20 commits
    else:
        num_commits = random.randint(1, 4)    # normal days

    for i in range(num_commits):
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        date_str = day.strftime(f"%Y-%m-%dT{hour:02d}:{minute:02d}:00")

        with open("activity.md", "a") as f:
            f.write(f"update {date_str} commit {i+1}\n")

        subprocess.run(["git", "add", "."])
        subprocess.run([
            "git", "commit", "-m", f"update {i+1}",
        ], env={
            **os.environ,
            "GIT_AUTHOR_DATE": date_str,
            "GIT_COMMITTER_DATE": date_str,
        })

print("Done!")