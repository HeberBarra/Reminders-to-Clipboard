from reminders.reminder import Reminder
import dataclasses


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

    def list_all_reminders(self) -> list[Reminder]:
        pass

    def list_valid_reminders_json(self, current_date: str) -> list:
        valid_reminders = []
        section_index = 0

        for section in self.json_data:
            valid_reminders.append({'Title': section['Title'], 'Messages': []})
            for reminder in section['Messages']:
                if (reminder['dates'] == 'ALWAYS') or (current_date in reminder['dates']):
                    valid_reminders[section_index]['Messages'].append(reminder)

            section_index += 1

        return valid_reminders

    def update(self, reminder: Reminder) -> None:
        pass

    def delete(self, reminder: Reminder) -> None:
        pass
