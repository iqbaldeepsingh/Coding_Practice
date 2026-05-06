import os
import requests
import json
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
    username = os.environ.get("HACKERRANK_USERNAME")
    password = os.environ.get("HACKERRANK_PASSWORD")

    session = requests.Session()

    try:
        login_url = "https://www.hackerrank.com/auth/login"
        session.get(login_url, timeout=10)

        csrf = session.cookies.get("_csrf_token")

        payload = {
            "login": username,
            "password": password,
            "remember_me": False,
            "_csrf_token": csrf
        }

        headers = {
            "Content-Type": "application/json",
            "X-CSRF-Token": csrf,
            "Referer": login_url
        }

        session.post(login_url, json=payload, headers=headers, timeout=10)

        profile_url = f"https://www.hackerrank.com/rest/hackers/{username}/scores_elo"
        response = session.get(profile_url, timeout=10)
        data = response.json()

        return {
            "total_solved": data.get("total", 0),
            "rank": data.get("rank", "N/A")
        }
    except Exception as e:
        print(f"HackerRank fetch failed: {e}")
        return {"total_solved": 0, "rank": "N/A"}


# ─── STRATASCRATCH ──────────────────────────────────────
def fetch_stratascratch_stats():
    username = os.environ.get("STRATASCRATCH_USERNAME")
    password = os.environ.get("STRATASCRATCH_PASSWORD")

    session = requests.Session()

    try:
        login_url = "https://platform.stratascratch.com/auth/login"
        session.get(login_url, timeout=10)

        payload = {
            "username": username,
            "password": password
        }

        session.post(login_url, json=payload, timeout=10)

        profile_url = f"https://platform.stratascratch.com/api/user/{username}/stats"
        response = session.get(profile_url, timeout=10)
        data = response.json()

        return {
            "total_solved": data.get("solved", 0),
            "easy": data.get("easy", 0),
            "medium": data.get("medium", 0),
            "hard": data.get("hard", 0)
        }
    except Exception as e:
        print(f"StrataScratch fetch failed: {e}")
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