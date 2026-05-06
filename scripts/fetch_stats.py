import os
import json
import requests
from datetime import datetime


# ─── LEETCODE ───────────────────────────────────────────
def fetch_leetcode_stats():
    username = os.environ.get("LEETCODE_USERNAME")
    session  = os.environ.get("LEETCODE_SESSION")
    csrf     = os.environ.get("LEETCODE_CSRF_TOKEN")

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={session}; csrftoken={csrf}",
        "x-csrftoken": csrf,
        "Referer": "https://leetcode.com"
    }

    query = {
        "query": """
        query getUserProfile($username: String!) {
            matchedUser(username: $username) {
                submitStats {
                    acSubmissionNum {
                        difficulty
                        count
                    }
                }
                profile {
                    ranking
                }
            }
        }
        """,
        "variables": {"username": username}
    }

    try:
        response = requests.post(
            "https://leetcode.com/graphql",
            headers=headers,
            json=query,
            timeout=10
        )
        data = response.json()
        stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]
        ranking = data["data"]["matchedUser"]["profile"]["ranking"]

        result = {"ranking": ranking}
        for item in stats:
            result[item["difficulty"].lower()] = item["count"]
        return result
    except Exception as e:
        print(f"LeetCode fetch failed: {e}")
        return {"all": 0, "easy": 0, "medium": 0, "hard": 0, "ranking": 0}


# ─── HACKERRANK ─────────────────────────────────────────
def fetch_hackerrank_stats():
    username   = os.environ.get("HACKERRANK_USERNAME")
    session_id = os.environ.get("HACKERRANK_SESSION_ID")
    mixpanel   = os.environ.get("HACKERRANK_MIXPANEL_TOKEN")

    headers = {
        "Cookie": f"session_id={session_id}; hackerrank_mixpanel_token={mixpanel}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Referer": "https://www.hackerrank.com"
    }

    try:
        url = f"https://www.hackerrank.com/rest/hackers/{username}/submission_histories"
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        total = sum(data.values()) if isinstance(data, dict) else 0

        return {
            "total_solved": total,
            "rank": "N/A"
        }
    except Exception as e:
        print(f"HackerRank fetch failed: {e}")
        return {"total_solved": 0, "rank": "N/A"}


# ─── STRATASCRATCH ──────────────────────────────────────
def fetch_stratascratch_stats():
    # No public API available — manually update strata_total in update_progress.py
    return {"total_solved": 0, "easy": 0, "medium": 0, "hard": 0}


# ─── MAIN ───────────────────────────────────────────────
if __name__ == "__main__":
    stats = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "leetcode": fetch_leetcode_stats(),
        "hackerrank": fetch_hackerrank_stats(),
        "stratascratch": fetch_stratascratch_stats()
    }

    with open("stats.json", "w") as f:
        json.dump(stats, f, indent=2)

    print("Stats fetched successfully!")
    print(json.dumps(stats, indent=2))