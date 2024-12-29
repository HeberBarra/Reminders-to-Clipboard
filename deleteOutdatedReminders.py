from utils import date_utils
from utils import json_utils
from reminders import deleteReminder
import json

# Gets a dd/mm/yy date and converts to a dd/mm format
DATE = '/'.join(date_utils.get_current_date()[0].split('/')[:2])
CONFIG_FILE = 'config.json'
CONFIG_DATA = json_utils.read_json_file(CONFIG_FILE)
JSON_FILE = CONFIG_DATA['remindersJsonFilePath']


def main():
    json_data = json_utils.read_json_file(JSON_FILE)
    remaining_reminders = deleteReminder.getUndeletedRemindersData(json_data, DATE)
    print(remaining_reminders)
    with open(JSON_FILE, 'w+', encoding='UTF-8') as json_file:
        json_file.write(json.dumps(remaining_reminders, ensure_ascii=False))


if __name__ == '__main__':
    main()
