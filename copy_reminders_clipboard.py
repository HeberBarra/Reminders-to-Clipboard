from utils import json_utils
from utils import date_utils
from reminders.reminder_dao import ReminderDAO
from schedule import schedule
import pyperclip

CONFIG_FILE = 'config/config.json'
CONFIG_DATA = json_utils.read_json_file(CONFIG_FILE)
HEADER = CONFIG_DATA['headerMessage']
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']
XLSX_FILE = CONFIG_DATA['scheduleXlsxFilePath']
schedule_message = CONFIG_DATA['scheduleMessage']
json_data = json_utils.read_json_file(JSON_FILE)


def main():
    program_date, weekday = date_utils.get_current_date()
    original_clipboard_content = pyperclip.paste()
    reminder_dao = ReminderDAO(json_data)
    current_date = date_utils.get_current_day_month_date()

    reminders = (
        schedule.get_formatted_schedule(XLSX_FILE, schedule_message, weekday)
        + '\n'
        + reminder_dao.list_reminders_formatted(HEADER, current_date)
    )
    print(f'Preview: \n{reminders}')
    pyperclip.copy(reminders)
    pyperclip.copy(original_clipboard_content)


if __name__ == '__main__':
    main()
