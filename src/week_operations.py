from datetime import datetime, timedelta


class WeekOperations:
    @classmethod
    def is_date_between_latest_weeks(cls, target_date, number_of_weeks):
        target_date = cls.flat_to_date_class(target_date)

        init, end = cls.latest_weeks_range(number_of_weeks)
        return init <= target_date and target_date <= end

    @classmethod
    def is_date_before_latest_weeks(cls, target_date, number_of_weeks):
        target_date = cls.flat_to_date_class(target_date)

        init, end = cls.latest_weeks_range(number_of_weeks)
        return init > target_date

    @classmethod
    def latest_weeks_range(cls, number_of_weeks):
        now = datetime.now().date()
        end = now - timedelta(days=((now.weekday() + 1) % 7))
        init = end - timedelta(weeks=number_of_weeks) + timedelta(days=1)
        return (init, end)

    @classmethod
    def flat_to_date_class(cls, target_date):
        if isinstance(target_date, datetime):
            target_date = target_date.date()
        return target_date
