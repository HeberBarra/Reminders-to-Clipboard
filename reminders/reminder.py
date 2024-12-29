import dataclasses
from datetime import date, timedelta


@dataclasses.dataclass()
class Reminder:
    initial_date: date
    last_date: date
    section: str
    section_index: int
    message: str

    def __init__(
        self,
        initial_date: date,
        last_date: date,
        section: str,
        section_index: int,
        message: str,
    ):
        self.initial_date = initial_date
        self.last_date = last_date
        self.section = section
        self.section_index = section_index
        self.message = message

    def calculate_date_interval(self) -> list[str]:
        current_date = self.initial_date
        date_interval = []

        while self.last_date >= current_date:
            date_interval.append(date.strftime(current_date, '%d/%m'))
            current_date += timedelta(days=1)

        return date_interval

    def check_if_outdated(self, current_date: date) -> bool:
        return self.last_date < current_date

    def adjust_message(self):
        return self.message.replace('\\n', '\n').replace('\\t', '\t')

    def print(self, is_last=False):
        print(
            f"""
        \t\t{{
        \t\t\t"dates": {self.calculate_date_interval()}
        \t\t\t"message": "{self.message}"
        \t\t}}{'' if is_last else ','}
        """.replace("'", '"')
        )
