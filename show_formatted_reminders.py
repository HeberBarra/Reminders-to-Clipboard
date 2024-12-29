from utils import json_utils
from reminders import reminder_json

CONFIG_FILE = 'config/config.json'
CONFIG_DATA = json_utils.read_json_file(CONFIG_FILE)
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']
json_data = json_utils.read_json_file(JSON_FILE)


def main():
    for section in json_data:
        reminder_json.print_section(section, section == json_data[-1])


if __name__ == '__main__':
    main()
