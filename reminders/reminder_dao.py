import dataclasses

from reminders.reminder import Reminder


@dataclasses.dataclass()
class ReminderDAO:
    json_data: list

    def __init__(self, json_data: list):
        self.json_data = json_data

    def create(self, reminder: Reminder) -> None:
        self.json_data[reminder.section_index]['Messages'].append(
            {
                'dates': reminder.calculate_date_interval(),
                'message': reminder.adjust_message()
            }
        )

    def list(self) -> list[Reminder]:
        pass

    def update(self, reminder: Reminder) -> None:
        pass

    def delete(self, reminder: Reminder) -> None:
        pass
