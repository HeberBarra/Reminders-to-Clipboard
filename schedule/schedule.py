from utils import json_utils
import openpyxl


CONFIG_DATA = json_utils.read_json_file('config.json')
WEEKDAYS_COLUMNS = CONFIG_DATA['weekdayColumns']


def get_formatted_schedule(schedule_file: str, schedule_message: list[str], weekday: str) -> str:
    worksheet = openpyxl.load_workbook(schedule_file).active

    if WEEKDAYS_COLUMNS[weekday] is None:
        return ''

    for row in range(2, worksheet.max_row + 1):
        cell_value = worksheet[f'{WEEKDAYS_COLUMNS[weekday]}{row}'].value

        if cell_value is None:
            cell_value = 'EMPTY'

        schedule_message.append(f'  {row - 1}º: {cell_value}')

    return '\n'.join(schedule_message)
