from reminders.reminder import Reminder
from reminders.reminder_dao import ReminderDAO
from reminders import reminder_json
from utils import input_utils
from utils import json_utils
import datetime
import json

CONFIG_DATA = json_utils.read_json_file('config.json')
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']
json_data = json_utils.read_json_file(JSON_FILE)


def main():
    section_index = input_utils.choose_section(json_data)
    reminder_json.show_section(section_index, json_data)
    start_date = input_utils.is_option_right("What's the first date?: ")
    end_date = input_utils.is_option_right("What's the last date?: ")
    message = input_utils.is_option_right("What's the new message?: ")

    initial_date = datetime.datetime.strptime(start_date, '%d/%m/%y')
    last_date = datetime.datetime.strptime(end_date, '%d/%m/%y')
    section = json_data[section_index]['Title']
    reminder = Reminder(initial_date, last_date, section, section_index, message)
    reminder_dao = ReminderDAO(json_data)
    reminder_dao.create(reminder)

    with open(JSON_FILE, 'w', encoding='utf-8') as file:
        file.write(json.dumps(reminder_dao.json_data, ensure_ascii=False))


if __name__ == '__main__':
    main()
