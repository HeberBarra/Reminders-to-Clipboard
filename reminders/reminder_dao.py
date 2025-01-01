from reminders.reminder import Reminder
from reminders.reminders_list import RemindersList
import dataclasses


@dataclasses.dataclass()
class ReminderDAO:
    json_data: dict

    def __init__(self, json_data: dict):
        self.json_data = json_data

    def create(self, reminder: Reminder) -> None:
        reminders = self.json_data['reminders'][reminder.section_index]['Messages']

        if len(reminders) == 0:
            last_id = 0
        else:
            last_id = reminders[-1]['localID']

        self.json_data['reminders'][reminder.section_index]['Messages'].append(
            {
                'localID': last_id + 1,
                'dates': reminder.calculate_date_interval(),
                'message': reminder.adjust_message()
            }
        )

    def list_reminders_formatted(self, header: str, current_date: str) -> str:
        reminders_list = RemindersList()

        for section in self.json_data['reminders']:
            if not section['Messages']:
                continue

            reminders_list.append(f'[{section['Title']}]')
            starting_len = len(reminders_list)

            for reminder in section['Messages']:
                if (current_date == 'ALWAYS') or (current_date in reminder['dates']):
                    reminders_list.append(reminder['message'], current_date)

            if starting_len == len(reminders_list):
                reminders_list.pop()

        return f'{header} {current_date}\n{'\n'.join(reminders_list)}'

    def list_valid_reminders_json(self, current_date: str) -> list:
        valid_reminders = []
        section_index = 0

        for section in self.json_data['reminders']:
            valid_reminders.append({'Title': section['Title'], 'Messages': []})
            for reminder in section['Messages']:
                if (reminder['dates'] == 'ALWAYS') or (
                    current_date in reminder['dates']
                ):
                    valid_reminders[section_index]['Messages'].append(reminder)

            section_index += 1

        return valid_reminders

    def update(self, reminder: Reminder) -> None:
        pass

    def delete(self, reminder: Reminder) -> None:
        pass
