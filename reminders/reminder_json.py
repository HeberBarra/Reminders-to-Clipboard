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
        f"""
    \t\t{{
    \t\t\t"dates": {reminder['dates']},
    \t\t\t"message": "{reminder['message']}" 
    \t\t}}{',' if not last else ''}
    """,
        end='',
    )


def print_reminders(section: dict) -> None:
    for reminder in section['Messages']:
        is_last = reminder == section['Messages'][-1]
        print_reminder(reminder, is_last)


def print_section(section: dict, is_last=False) -> None:
    print('{')
    print(f'\t"Title": "{format_title(section['Title'])}"')
    print('\t"Messages": [')
    print_reminders(section)
    print('\t]')
    print('}', end='')
    print('' if is_last else ',')
