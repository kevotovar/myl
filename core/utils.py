import collections
import datetime
from calendar import monthrange

from django.utils import timezone


def get_duplicates_from_list(list_to_be_checked):
    return [
        item for item, count in collections.Counter(list_to_be_checked) if count > 1
    ]


def count_duplicates(list_to_be_counted):
    return len(list_to_be_counted) - len(set(list_to_be_counted))


def get_current_time_with_tz():
    return timezone.now()


def get_start_date_and_end_date_from_datetime(
    datetime_obj: datetime.datetime
) -> (datetime.datetime, datetime.datetime):
    month = datetime_obj.month
    year = datetime_obj.year
    datetime_monthrange = monthrange(month=month, year=year)
    return (
        datetime.datetime(month=month, year=year, day=datetime_monthrange[0]),
        datetime.datetime(
            month=month,
            year=year,
            day=datetime_monthrange[1],
            hour=11,
            minute=59,
            second=59
        ),
    )
