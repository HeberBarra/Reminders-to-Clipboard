from utils import input_utils
from utils import json_utils
from reminders import createReminder
from reminders import reminder_json
import json

config_data = json_utils.read_json_file('config.json')
JSON_FILE = config_data['remindersJsonFilePath']
json_data = json_utils.read_json_file(JSON_FILE)


def main():
    chosen_section = input_utils.choose_section(json_data)
    reminder_json.show_section(chosen_section, json_data)

    start_date = input_utils.is_option_right(
        "What's the first date?: ", 'Is it right?: '
    )
    end_date = input_utils.is_option_right("What's the last date?: ", 'Is it right?: ')
    new_message = input_utils.is_option_right(
        "What's the new message?: ", 'Is it right?: '
    )
    date_interval = createReminder.getDateInterval(start_date, end_date)
    json_data[chosen_section]['Messages'].append(
        {
            'dates': date_interval,
            'message': new_message.replace('\\n', '\n').replace('\\t', '\t'),
        }
    )

    with open(JSON_FILE, 'w', encoding='utf-8') as j_file:
        json.dump(json_data, fp=j_file, ensure_ascii=False)


if __name__ == '__main__':
    main()
