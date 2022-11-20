from Reminders import genericReminderFunctions
from Reminders import deleteReminder
import json

DATE = genericReminderFunctions.getDate()[0]
CONFIG_FILE = 'config.json'
CONFIG_DATA = genericReminderFunctions.readJsonFile(CONFIG_FILE)
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']


def main():
    json_data = genericReminderFunctions.readJsonFile(JSON_FILE)
    remaining_reminders = deleteReminder.getUndeletedRemindersData(json_data, DATE)

    with open(JSON_FILE, 'w+', encoding='UTF-8') as json_file:
        json.dump(remaining_reminders, fp=json_file, ensure_ascii=False)


if  __name__ == '__main__':
    main()
