from Reminders import genericReminderFunctions
from Reminders import showReminder

CONFIG_FILE = 'config.json'
CONFIG_DATA = genericReminderFunctions.readJsonFile(CONFIG_FILE)
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']


def printReminder(reminder, last=False):
    if not reminder:
        return

    print("""
    \t\t{
    \t\t\t"dates": %s,
    \t\t\t"message": "%s" 
    \t\t}%s
    """ % (
        reminder['dates'],
        reminder['message'],
        ',' if not last else ''
    )
    )


def getReminders(section):
    for reminder in section['Messages']:
        printReminder(reminder, last=reminder == section['Messages'][-1])


def printSection(section, last=False):
    print('{')
    print(f'\t"Title": "{showReminder.removeTitleSpecialParts(section["Title"])}",')
    print('\t"Messages": [')
    getReminders(section)
    print('\t]')
    print('}', end='') 
    print(',' if not last else '')


def main():
    json_data = genericReminderFunctions.readJsonFile(JSON_FILE)
    
    for section in json_data:
        printSection(section, last=section == json_data[-1])

if __name__ == '__main__':
    main()
