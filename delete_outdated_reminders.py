from reminders.reminder_dao import ReminderDAO
from utils import date_utils
from utils import json_utils
import json

CONFIG_FILE = 'config/config.json'
CONFIG_DATA = json_utils.read_json_file(CONFIG_FILE)
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']
json_data = json_utils.read_json_file(JSON_FILE)


def main():
    current_date = date_utils.get_current_day_month_date()
    reminder_dao = ReminderDAO(json_data)
    remaining_reminders = reminder_dao.list_valid_reminders_json(current_date)
    print(remaining_reminders)

    with open(JSON_FILE, 'w+', encoding='UTF-8') as json_file:
        json_file.write(json.dumps(remaining_reminders, ensure_ascii=False))


if __name__ == '__main__':
    main()
