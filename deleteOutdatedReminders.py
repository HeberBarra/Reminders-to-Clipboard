from Reminders import genericReminderFunctions
from Reminders import deleteReminder
import json

# Gets a dd/mm/yy date and converts to a dd/mm format
DATE = '/'.join(genericReminderFunctions.getDate()[0].split('/')[:2])
CONFIG_FILE = 'config.json'
CONFIG_DATA = genericReminderFunctions.readJsonFile(CONFIG_FILE)
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']


def main():
    json_data = genericReminderFunctions.readJsonFile(JSON_FILE)
    remaining_reminders = deleteReminder.getUndeletedRemindersData(json_data, DATE)
    print(remaining_reminders)
    with open(JSON_FILE, 'w+', encoding='UTF-8') as json_file:
        json.dump(remaining_reminders, fp=json_file, ensure_ascii=False)


if  __name__ == '__main__':
    main()
