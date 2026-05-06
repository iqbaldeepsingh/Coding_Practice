import json
import os
from datetime import datetime


# ─── LOAD STATS ─────────────────────────────────────────
def load_stats():
    with open("stats.json", "r") as f:
        return json.load(f)


# ─── UPDATE PROGRESS.MD ─────────────────────────────────
def update_progress(stats):
    date      = stats["date"]
    leetcode  = stats["leetcode"]
    hackerrank = stats["hackerrank"]
    strata    = stats["stratascratch"]

    new_entry = f"""
## {date}

### 🟡 LeetCode
| Metric | Value |
|--------|-------|
| Easy Solved | {leetcode.get('easy', 0)} |
| Medium Solved | {leetcode.get('medium', 0)} |
| Hard Solved | {leetcode.get('hard', 0)} |
| Total Solved | {leetcode.get('all', 0)} |
| Ranking | {leetcode.get('ranking', 'N/A')} |

### 🟢 HackerRank
| Metric | Value |
|--------|-------|
| Total Solved | {hackerrank.get('total_solved', 0)} |
| Rank | {hackerrank.get('rank', 'N/A')} |

### 🔵 StrataScratch
| Metric | Value |
|--------|-------|
| Easy Solved | {strata.get('easy', 0)} |
| Medium Solved | {strata.get('medium', 0)} |
| Hard Solved | {strata.get('hard', 0)} |
| Total Solved | {strata.get('total_solved', 0)} |

---
"""

    # Read existing progress
    if os.path.exists("progress.md"):
        with open("progress.md", "r") as f:
            existing = f.read()
    else:
        existing = "# 📊 Coding Progress Tracker\n\n"

    # Check if today already logged
    if date in existing:
        print(f"Already logged for {date} — skipping")
        return

    # Append new entry at top after header
    lines = existing.split("\n")
    header = lines[0]
    rest   = "\n".join(lines[1:])
    updated = f"{header}\n{new_entry}{rest}"

    with open("progress.md", "w") as f:
        f.write(updated)

    print(f"Progress updated for {date} ✅")


# ─── MAIN ───────────────────────────────────────────────
if __name__ == "__main__":
    stats = load_stats()
    update_progress(stats)