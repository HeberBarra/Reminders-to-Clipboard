def showSection(index: int,  json_data: list) -> None:
    for item in json_data[index]['Messages']:
        print(item['dates'])
        print(rf"{item['message']}", '\n')


def removeTitleSpecialParts(string: str) -> str:
    special_parts = ['\n', '*', '_', ':']

    for part in special_parts:
        string = string.replace(part, '')

    return string


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
    print(f'\t"Title": "{removeTitleSpecialParts(section["Title"])}",')
    print('\t"Messages": [')
    getReminders(section)
    print('\t]')
    print('}', end='') 
    print(',' if not last else '')
