from utils import json_utils
from reminders import reminders_list
import openpyxl
import webbrowser
import pyautogui
import sys
import time


config_data = json_utils.read_json_file('config.json')
schedule_message = config_data['scheduleMessage']
WEEKDAYS_COLUMNS = config_data['weekdayColumns']
HEADER_MESSAGE = config_data['headerMessage']
REMINDERS_MESSAGE = config_data['remindersMessage']


def getScheduleFromFile(xlsx_file: str, weekday: str) -> str:
    global schedule_message

    sheet = openpyxl.load_workbook(xlsx_file).active

    if WEEKDAYS_COLUMNS[weekday] is None:
        return ''

    for row in range(2, sheet.max_row + 1):
        schedule_message.append(
            f'\t* {row - 1} - : ' + sheet[f'{WEEKDAYS_COLUMNS[weekday]}{row}'].value
        )

    return '\n'.join(schedule_message)


def getRemindersFromJson(file_path: str, program_date: str) -> str:
    reminders_json_data = json_utils.read_json_file(file_path)
    messages = remindersList.RemindersList()

    # Converts date from dd/mm/yy to dd/mm format
    program_date = '/'.join(program_date.split('/')[:2])

    for title in reminders_json_data:
        if not title['Messages']:
            continue

        messages.append(title['Title'])
        starting_len = len(messages)

        for reminder in title['Messages']:
            if not reminder:
                continue

            if program_date in reminder['dates'] or reminder['dates'] == 'ALWAYS':
                messages.append(reminder['message'], date=program_date)

        if starting_len == len(messages):
            messages.pop()

    message = f'{HEADER_MESSAGE} {program_date} {REMINDERS_MESSAGE} \n'

    # Example: "Good morning beautiful people! Here are the reminders for today: {messages}"
    return message


def openWhatsappWeb(
    x: int, y: int, browser: str, browser_name: str, color: tuple[int]
) -> None:
    webbrowser.register(browser_name, None, webbrowser.BackgroundBrowser(browser))

    webbrowser.get(browser_name).open_new('web.whatsapp.com')
    while not pyautogui.pixelMatchesColor(x, y, color):
        pass


def sendMessage(
    contact_coordinates: tuple[int],
    message_field_coordinates: tuple[int],
    color: tuple[int],
    browser: str,
    browser_name: str,
) -> bool:
    pass

    if sys.argv[-1] == 'dontsend':
        return True

    if sys.argv[-1] == 'copyonly':
        return False

    openWhatsappWeb(
        x=contact_coordinates[0],
        y=contact_coordinates[1],
        browser=browser,
        browser_name=browser_name,
        color=color,
    )
    pyautogui.click(x=contact_coordinates[0], y=contact_coordinates[1])

    time.sleep(1.2)

    pyautogui.click(x=message_field_coordinates[0], y=message_field_coordinates[1])
    time.sleep(0.4)
    pyautogui.hotkey('ctrl', 'v')

    return True
