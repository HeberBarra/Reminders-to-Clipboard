from reminders import genericReminderFunctions
from reminders import showReminder

CONFIG_FILE = 'config.json'
CONFIG_DATA = genericReminderFunctions.readJsonFile(CONFIG_FILE)
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']


def main():
    json_data = genericReminderFunctions.readJsonFile(JSON_FILE)
    
    for section in json_data:
        showReminder.printSection(section, last=section == json_data[-1])

if __name__ == '__main__':
    main()
