import subprocess
import random
from datetime import datetime, timedelta
import os

# Date range: January 2025 to May 2025
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 5, 31)

# Build list of all days
all_days = []
current = start_date
while current <= end_date:
    all_days.append(current)
    current += timedelta(days=1)

# Select 40% of days randomly
selected_days = random.sample(all_days, int(len(all_days) * 0.40))
selected_days.sort()

# 15% of selected days will be heavy days (~20 commits)
heavy_days_count = int(len(selected_days) * 0.15)
heavy_days = set(random.sample(range(len(selected_days)), heavy_days_count))

for idx, day in enumerate(selected_days):
    if idx in heavy_days:
        num_commits = random.randint(18, 23)  # ~20 commits
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