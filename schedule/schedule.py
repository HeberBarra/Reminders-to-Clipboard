from config.configurator import Configurator
import openpyxl


def get_formatted_schedule(
    schedule_file: str, schedule_message: list[str], weekday: str
) -> str:
    worksheet = openpyxl.load_workbook(schedule_file).active
    weekdays_columns = Configurator('config/config.json').weekday_columns

    if weekdays_columns[weekday] is None:
        return ''

    for row in range(2, worksheet.max_row + 1):
        cell_value = worksheet[f'{weekdays_columns[weekday]}{row}'].value

        if cell_value is None:
            cell_value = 'EMPTY'

        schedule_message.append(f'  {row - 1}º: {cell_value}')

    return '\n'.join(schedule_message)
