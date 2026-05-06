"""
Update progress.md with the latest coding statistics
"""

import json
import os
from datetime import datetime

STATS_FILE = 'stats.json'
PROGRESS_FILE = 'progress.md'

def load_stats():
    """Load statistics from JSON file"""
    if not os.path.exists(STATS_FILE):
        return None
    
    with open(STATS_FILE, 'r') as f:
        return json.load(f)

def format_progress_entry(stats):
    """Format statistics into markdown entry"""
    date_str = datetime.now().strftime('%Y-%m-%d')
    entry = f"\n## {date_str}\n\n"
    
    # LeetCode
    if stats.get('leetcode'):
        lc = stats['leetcode']
        entry += "### 🔴 LeetCode\n"
        entry += f"- **Username**: {lc.get('username', 'N/A')}\n"
        entry += f"- **Total Solved**: {lc.get('total_solved', 0)}\n"
        entry += f"- **Easy**: {lc.get('easy', 0)}\n"
        entry += f"- **Medium**: {lc.get('medium', 0)}\n"
        entry += f"- **Hard**: {lc.get('hard', 0)}\n\n"
    
    # StrataScratch
    if stats.get('stratascratch'):
        ss = stats['stratascratch']
        entry += "### 📊 StrataScratch\n"
        entry += f"- **Username**: {ss.get('username', 'N/A')}\n"
        entry += f"- **Problems Solved**: {ss.get('problems_solved', 0)}\n"
        entry += f"- **Total Points**: {ss.get('total_points', 0)}\n"
        entry += f"- **Coding Score**: {ss.get('coding_score', 0)}\n\n"
    
    # HackerRank
    if stats.get('hackerrank'):
        hr = stats['hackerrank']
        entry += "### 🏆 HackerRank\n"
        entry += f"- **Username**: {hr.get('username', 'N/A')}\n"
        entry += f"- **Badges Earned**: {hr.get('badges_count', 0)}\n"
        if hr.get('badges'):
            entry += f"- **Recent Badges**: {', '.join(hr['badges'])}\n\n"
    
    entry += "---\n"
    return entry

def update_progress():
    """Update progress.md file"""
    stats = load_stats()
    if not stats:
        print("❌ No stats file found")
        return
    
    # Check if entry already exists for today
    date_str = datetime.now().strftime('%Y-%m-%d')
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            content = f.read()
        
        # If today's entry exists, update it
        if f"## {date_str}" in content:
            print(f"📝 Entry for {date_str} already exists, skipping...")
            return
    
    # Create new entry
    entry = format_progress_entry(stats)
    
    # Append to progress file
    with open(PROGRESS_FILE, 'a') as f:
        f.write(entry)
    
    print(f"✅ Progress updated for {date_str}")

if __name__ == '__main__':
    update_progress()
