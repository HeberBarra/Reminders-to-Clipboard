from reminders import showReminder
import datetime
import sys
import json


def isOptionRight(message: str, confirm_mesage: str) ->str:
    while True:
        chosen_option = input(message)
        is_right = input(confirm_mesage).lower()[0]

        if is_right in 'ysapc':
            return chosen_option


def chooseSection(json_data: list) -> int:
    for index in range(len(json_data)):
        print(f'[{index}]{showReminder.removeTitleSpecialParts(json_data[index]["Title"])}')
    
    while True:
        chosen_section = int(isOptionRight('Choose a section: ', 'Is the selection right?: '))
        if chosen_section in [number for number in range(len(json_data))]:
            return chosen_section
        
        print('Type a valid section!')


def getDate() -> tuple[str]:
    if len(sys.argv) == 1:
        program_date = datetime.datetime.now().strftime('%d/%m/%y')

    else:
        program_date = sys.argv[1]

    weekday = datetime.datetime.strptime(program_date, '%d/%m/%y').strftime('%A')

    return program_date, weekday


def readJsonFile(file_path: str):
    with open(file_path, encoding='utf-8') as file:
        json_data = json.load(file)
    
    return json_data
