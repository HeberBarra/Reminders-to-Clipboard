import datetime
import re
import sys


def get_current_date() -> tuple[str, str]:
    current_date: str
    # Simplified date regex
    date_pattern = re.compile('[0-9]{2}/[0-9]{2}/[0-9]{2}')

    if len(sys.argv) == 1 or not re.match(date_pattern, sys.argv[1]):
        current_date = datetime.datetime.now().strftime('%d/%m/%y')
    else:
        current_date = sys.argv[1]

    weekday = datetime.datetime.strptime(current_date, '%d/%m/%y').strftime('%A')

    return current_date, weekday


def get_current_day_month_date() -> str:
    return '/'.join(get_current_date()[0].split('/')[:2])
