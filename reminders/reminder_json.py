def show_section(index: int, json_data: list) -> None:
    for item in json_data[index]['Messages']:
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
