from os import stat, path


def format_title(title: str) -> str:
    special_parts = ['\n', '*', '_', ':']

    for part in special_parts:
        title = title.replace(part, '')

    return title


def create_reminders_file(reminders_file: str):
    base_data = {'$schema': 'reminders/reminders.schema.json', 'reminders': []}

    if path.isfile(reminders_file) and stat(reminders_file).st_size != 0:
        return

    with open(reminders_file, 'w', encoding='utf-8') as file:
        file.write(base_data.__str__().replace("'", '"'))
