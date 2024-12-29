from typing import Any
import json


def read_json_file(json_filepath: str) -> Any:
    with open(json_filepath, encoding='utf-8') as file:
        json_data = json.load(file)

    return json_data
