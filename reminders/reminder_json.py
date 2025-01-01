from os import stat
import os.path


def show_section(index: int, json_data: dict) -> None:
    for item in json_data['reminders'][index]['Messages']:
        print(item['dates'])
        print(f'{item['message']}\n')


def format_title(title: str) -> str:
    special_parts = ['\n', '*', '_', ':']

    for part in special_parts:
        title = title.replace(part, '')

    return title


def print_reminder(reminder, last=False):
    if not reminder:
        return

    print(
        f"""    {{
      "dates": {reminder['dates']},
      "message": "{reminder['message']}" 
    }}{',' if not last else ''}
        """,
        end='',
    )


def print_reminders(section: dict) -> None:
    for reminder in section['Messages']:
        is_last = reminder == section['Messages'][-1]
        print_reminder(reminder, is_last)


def print_section(section: dict, is_last=False) -> None:
    print('{')
    print(f'  "Title": "{format_title(section['Title'])}",')
    print('  "Messages": [')
    print_reminders(section)
    print('\r  ]')
    print('}', end='')
    print('' if is_last else ',')


def create_reminders_file():
    reminders_file = 'reminders.json'
    base_data = {"$schema": "reminders/reminders.schema.json","reminders": []}

    if os.path.isfile(reminders_file) and stat(reminders_file).st_size != 0:
        return

    with open(reminders_file, 'w',encoding='utf-8') as file:
        file.write(base_data.__str__().replace('\'', '"'))

