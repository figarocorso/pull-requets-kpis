from datetime import datetime, timedelta

from src.week_operations import WeekOperations


def test_date_between_latest_weeks():
    now = datetime.now().date()
    target_date = now - timedelta(days=((now.weekday() + 1) % 7))
    assert WeekOperations.is_date_between_latest_weeks(target_date, 1)

    target_date = now - timedelta(days=((now.weekday() + 1) % 7)) - timedelta(days=6)
    assert WeekOperations.is_date_between_latest_weeks(target_date, 1)

    target_date = now - timedelta(days=((now.weekday() + 1) % 7)) - timedelta(days=5)
    assert WeekOperations.is_date_between_latest_weeks(target_date, 1)

    target_date = now - timedelta(days=((now.weekday() + 1) % 7)) - timedelta(days=7)
    assert WeekOperations.is_date_between_latest_weeks(target_date, 1) == False

    target_date = now
    assert WeekOperations.is_date_between_latest_weeks(target_date, 1) == False

def test_date_between_latest_weeks_datetime():
    now = datetime.now()
    target_date = now - timedelta(days=((now.weekday() + 1) % 7))
    assert WeekOperations.is_date_between_latest_weeks(target_date, 1)

def test_date_before_latest_weeks():
    now = datetime.now()
    target_date = now - timedelta(days=20)
    assert WeekOperations.is_date_before_latest_weeks(target_date, 1)

    target_date = now - timedelta(days=((now.weekday() + 1) % 7)) - timedelta(days=7)
    assert WeekOperations.is_date_before_latest_weeks(target_date, 1)

    target_date = now - timedelta(days=((now.weekday() + 1) % 7)) - timedelta(days=6)
    assert WeekOperations.is_date_before_latest_weeks(target_date, 1) == False

    target_date = now
    assert WeekOperations.is_date_before_latest_weeks(target_date, 1) == False
