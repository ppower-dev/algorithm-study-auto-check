from datetime import datetime, timedelta

def calculate_week(year, month, day):
    """
    일요일을 기준으로 주차를 계산합니다.
    예: 2024년 2월 15일 → '202402_3'
    """
    date = datetime(year, month, day)
    first_day_of_month = date.replace(day=1)
    
    # 첫 날의 요일 (월=0, ..., 일=6)
    first_day_weekday = first_day_of_month.weekday()

    # 첫 번째 일요일 찾기
    if first_day_weekday != 6:
        first_sunday = first_day_of_month + timedelta(days=(6 - first_day_weekday))
    else:
        first_sunday = first_day_of_month
    
    # 주차 계산 (일요일이 포함된 주 기준)
    if date < first_sunday:
        week_number = 1
    else:
        week_number = ((date - first_sunday).days // 7) + 2  # 첫 주차는 1로 시작

    return f"{date.strftime('%Y%m')}_{week_number}"

def get_previous_and_current_week():
    now = datetime.utcnow() + timedelta(hours=9)

    # 일요일이면 토요일로 조정
    if now.weekday() == 6:
        now -= timedelta(days=1)
    elif now.weekday() == 0:
        now -= timedelta(days=2)

    current_week = calculate_week(now.year, now.month, now.day)
    previous_week = calculate_week((now - timedelta(days=7)).year, (now - timedelta(days=7)).month, (now - timedelta(days=7)).day)

    return previous_week, current_week

if __name__ == "__main__":
    p, c = get_previous_and_current_week()
    print("지난 주:", p)
    print("이번 주:", c)
