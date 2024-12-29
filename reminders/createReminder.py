import datetime


def getDateInterval(start: str, end: str) -> list[str]:
    date = datetime.datetime.strptime(start, '%d/%m/%y')
    end_date = datetime.datetime.strptime(end, '%d/%m/%y')
    date_interval = []

    while end_date >= date:
        date_interval.append(datetime.datetime.strftime(date, '%d/%m'))
        date += datetime.timedelta(days=1)

    return date_interval
