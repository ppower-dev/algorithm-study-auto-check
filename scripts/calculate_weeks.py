from datetime import datetime, timedelta

def calculate_week(year, month, day):
    """
    월요일을 기준으로 주차를 계산합니다.
    예: 2024년 2월 15일 → '202402_3'
    """
    date = datetime(year, month, day)
    first_day_of_month = date.replace(day=1)
    monday = date - timedelta(days=date.weekday())
    week_number = ((monday - first_day_of_month).days // 7) + 1
    # 0주차 방지: 최소 주차는 1부터 시작
    if week_number == 0:
        week_number = 1

    return f"{date.strftime('%Y%m')}_{week_number}"

def get_previous_and_current_week():
    # 한국 시간(UTC+9)을 고려
    now = datetime.utcnow() + timedelta(hours=9)

    current_week = calculate_week(now.year, now.month, now.day)
    last_week = now - timedelta(days=7)
    previous_week = calculate_week(last_week.year, last_week.month, last_week.day)

    return previous_week, current_week

if __name__ == "__main__":
    p, c = get_previous_and_current_week()
    print("지난 주:", p)
    print("이번 주:", c)
