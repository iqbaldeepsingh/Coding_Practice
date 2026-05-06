# 🚀 Coding Practice Auto-Sync

Automatically sync your daily coding progress from **LeetCode**, **StrataScratch**, and **HackerRank** to GitHub!

## 📋 What This Does

- ✅ Fetches your daily stats from 3 coding platforms
- ✅ Updates `progress.md` automatically every day
- ✅ Maintains a complete coding history on GitHub
- ✅ Creates daily commits with your progress
- ✅ No manual updates needed!

## 🔧 Setup Instructions

### Step 1: Add GitHub Secrets

Go to your repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add these three secrets with your usernames:

| Secret Name | Value |
|------------|-------|
| `LEETCODE_USERNAME` | Your LeetCode username |
| `STRATASCRATCH_USERNAME` | Your StrataScratch username |
| `HACKERRANK_USERNAME` | Your HackerRank username |

**Example:**
- Secret: `LEETCODE_USERNAME`
- Value: `john_doe`

### Step 2: Done! 🎉

The automation is now active! It will:
- Run every day at **00:00 UTC** (midnight)
- Fetch your latest stats
- Update `progress.md`
- Automatically commit the changes

### Manual Trigger

You can also manually run the sync anytime:
1. Go to **Actions** tab
2. Select **Sync Coding Progress** workflow
3. Click **Run workflow**

## 📁 Repository Structure

```
Coding_Practice/
├── .github/
│   └── workflows/
│       └── sync-coding-progress.yml    # Daily automation
├── scripts/
│   ├── fetch_stats.py                  # Fetch platform stats
│   └── update_progress.py              # Update progress file
├── progress.md                         # Your daily progress log
└── README.md                           # This file
```

## 📊 How It Works

1. **Daily Trigger**: GitHub Actions runs at midnight UTC
2. **Fetch Stats**: Connects to LeetCode, StrataScratch, and HackerRank APIs
3. **Update Progress**: Creates/updates `progress.md` with today's stats
4. **Auto Commit**: Commits changes with timestamp
5. **History**: Your complete coding journey is preserved in Git history

## ⏰ Customizing the Schedule

To change when the sync runs, edit `.github/workflows/sync-coding-progress.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'  # Change this line
```

**Cron format:** `minute hour day month day-of-week`

**Examples:**
- `0 6 * * *` → Daily at 6 AM UTC
- `0 12 * * *` → Daily at 12 PM UTC (noon)
- `0 0 * * 1` → Every Monday at midnight

[Cron syntax reference](https://crontab.guru/)

## 📝 Progress File Format

Your `progress.md` will look like:

```
## 2026-05-06

### 🔴 LeetCode
- **Total Solved**: 125
- **Easy**: 45
- **Medium**: 60
- **Hard**: 20

### 📊 StrataScratch
- **Problems Solved**: 32

### 🏆 HackerRank
- **Problems Solved**: 87
- **Expert Badges**: 3
```

## 🐛 Troubleshooting

### Workflow not running?
- Check if secrets are added correctly
- Go to **Actions** tab to see logs
- Try manually triggering the workflow

### Stats not updating?
- Verify usernames in secrets match exactly
- Check if platforms' APIs are accessible
- Review workflow logs for error messages

### Need to change platforms?
- Edit `.github/workflows/sync-coding-progress.yml`
- Modify `scripts/fetch_stats.py` to add/remove platforms
- Update the secrets accordingly

## 🎯 Benefits

- 📊 Complete coding history in one place
- 🔄 Zero manual effort
- 📈 Track progress over time
- 🎉 Motivate yourself with daily commits
- 💾 Git-backed backup of your journey

## 📞 Support

If you encounter issues:
1. Check GitHub Actions logs in the **Actions** tab
2. Verify all usernames and secrets are correct
3. Make sure your profiles are public on each platform

---

**Happy Coding! 💻**

