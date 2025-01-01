import dataclasses
import json


@dataclasses.dataclass
class RemindersData:
    json_data: dict
    reminders_filepath: str

    def __init__(self, json_data: any, reminders_filepath):
        self.json_data = json_data
        self.reminders_filepath = reminders_filepath

    def save(self):
        with open(self.reminders_filepath, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.json_data, ensure_ascii=False, indent=2))
