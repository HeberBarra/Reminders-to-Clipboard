import json

from utils import json_utils
from os import stat, path
import dataclasses


@dataclasses.dataclass()
class Configurator:
    _config_data: dict
    _config_file: str
    schedule_message: str
    header_message: str
    reminders_message: str
    reminders_json_filepath: str
    schedule_xlsx_filepath: str
    weekday_columns: dict

    def __init__(self, config_file: str):
        self._config_file = config_file
        self._create_default_config_file()
        self._read_config()

    def _read_config(self):
        try:
            self._config_data = json_utils.read_json_file(self._config_file)
            self.schedule_message = self._config_data['scheduleMessage']
            self.header_message = self._config_data['headerMessage']
            self.reminders_message = self._config_data['remindersMessage']
            self.reminders_json_filepath = self._config_data['remindersJsonFilePath']
            self.schedule_xlsx_filepath = self._config_data['scheduleXlsxFilePath']
            self.weekday_columns = self._config_data['weekdayColumns']
        except KeyError:
            print('Configuration contains errors! Terminanting the program')
            exit(1)

    def _create_default_config_file(self):
        default_config = {
            '$schema': 'config.schema.json',
            'scheduleMessage': [],
            'headerMessage': '',
            'remindersMessage': '',
            'remindersJsonFilePath': 'reminders.json',
            'scheduleXlsxFilePath': 'schedule.xlsx',
            'weekdayColumns': {
                'Sunday': 'A',
                'Monday': 'B',
                'Tuesday': 'C',
                'Wednesday': 'D',
                'Thursday': 'E',
                'Friday': 'F',
                'Saturday': 'G',
            },
        }

        if path.isfile(self._config_file) and stat(self._config_file).st_size != 0:
            return

        with open(self._config_file, 'w', encoding='utf-8') as file:
            file.write(json.dumps(default_config, indent=2, ensure_ascii=False))
