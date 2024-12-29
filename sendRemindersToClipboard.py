from utils import json_utils
from utils import date_utils
from reminders import sendReminder
import pyperclip

CONFIG_FILE = 'config.json'
CONFIG_DATA = json_utils.read_json_file(CONFIG_FILE)
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']
XLSX_FILE = CONFIG_DATA['scheduleXlsxFilePath']
CONTACT_COORDINATES = CONFIG_DATA['contactCoordinates']
MESSAGE_FIELD_COORDINATES = CONFIG_DATA['messageFieldCoordinates']
COLOR = CONFIG_DATA['color']
BROWSER_NAME = CONFIG_DATA['browserName']
BROWSER_PATH = CONFIG_DATA['browserPath']


def main():
    program_date, weekday = date_utils.get_current_date()
    original_clipboard_content = pyperclip.paste()
    reminders = (
        sendReminder.getScheduleFromFile(XLSX_FILE, weekday)
        + '\n'
        + sendReminder.getRemindersFromJson(JSON_FILE, program_date)
    )
    print(f'Preview: \n{reminders}')
    pyperclip.copy(reminders)

    restore_content = sendReminder.sendMessage(
        CONTACT_COORDINATES,
        MESSAGE_FIELD_COORDINATES,
        COLOR,
        BROWSER_PATH,
        BROWSER_NAME,
    )

    if restore_content:
        pyperclip.copy(original_clipboard_content)


if __name__ == '__main__':
    main()
