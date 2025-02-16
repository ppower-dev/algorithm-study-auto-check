import os
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from github import Github
from scripts.calculate_weeks import get_previous_and_current_week

ORG_NAME = "SSAFY-while-true"

def main():
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
    MATTERMOST_WEBHOOK_URL = os.getenv("MATTERMOST_WEBHOOK_URL")

    if not GITHUB_TOKEN:
        print("Error: Missing GITHUB_TOKEN")
        return

    # 이번 주 폴더 계산
    _, curr_week = get_previous_and_current_week()

    # 메시지 작성
    reminder_message = (
        f"🔔**Reminder!**🔔\n\n"
        f"이번 주 폴더명은 `{curr_week}` 입니다.\n"
        f"문제 풀이 & 폴더 업로드 잊지 마세요!💪\n"
        f"모두 화이팅입니다!🚀"
    )

    # 웹훅 전송
    if DISCORD_WEBHOOK_URL:
        send_to_discord(DISCORD_WEBHOOK_URL, reminder_message)
    if MATTERMOST_WEBHOOK_URL:
        send_to_mattermost(MATTERMOST_WEBHOOK_URL, reminder_message)

def send_to_discord(webhook_url, message):
    try:
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code in [200, 204]:
            print("Discord reminder sent successfully!")
        else:
            print(f"Failed to send Discord reminder. Status: {response.status_code}")
    except Exception as e:
        print(f"Error sending Discord reminder: {e}")

def send_to_mattermost(webhook_url, message):
    payload = {"text": message}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("Mattermost reminder sent successfully!")
        else:
            print(f"Failed to send Mattermost reminder. Status: {response.status_code}")
    except Exception as e:
        print(f"Error sending Mattermost reminder: {e}")

if __name__ == "__main__":
    main()