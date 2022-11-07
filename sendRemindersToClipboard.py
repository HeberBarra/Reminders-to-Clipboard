from Reminders import genericReminderFunctions
from Reminders import sendReminder
import pyperclip


config_data = genericReminderFunctions.readJsonFile('config.json')
JSON_FILE = config_data['remindersJsonFilePath']
XLSX_FILE = config_data['scheduleXlsxFilePath']
CONTACT_COORDINATES = config_data['contactCoordinates']
MESSAGE_FIELD_COORDINATES = config_data['messageFieldCoordinates']
COLOR = config_data['color']
BROWSER_NAME = config_data['browserName']
BROWSER_PATH = config_data['browserPath']


def main():
    program_date, weekday  = genericReminderFunctions.getDate()
    original_clipboard_content = pyperclip.paste()
    reminders = sendReminder.getScheduleFromFile(XLSX_FILE, weekday) + \
    '\n' + sendReminder.getRemindersFromJson(JSON_FILE, program_date)
    print(f'Preview: \n{reminders}')
    pyperclip.copy(reminders)

    restoreContent = sendReminder.sendMessage(
        CONTACT_COORDINATES,
        MESSAGE_FIELD_COORDINATES,
        COLOR,
        BROWSER_PATH,
        BROWSER_NAME
    )

    if restoreContent:
        pyperclip.copy(original_clipboard_content)



if __name__ == '__main__':
    main()
