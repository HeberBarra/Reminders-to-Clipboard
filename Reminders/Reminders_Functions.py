# TODO: Add docstrings and comments

from msilib.schema import File
import sys
import json
import datetime
import logging
import webbrowser
import time
import asyncio
import re
import pyautogui
import openpyxl
from Reminders.Enhanced_Reminders_List import Enhanced_Reminders_List

logging.basicConfig(filename='remindersLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

WEEKDAYS_FOR_SCHEDULE = { # Equivalent weekdays to cells letters 
    'Sunday': None,
    'Monday': 'B',
    'Tuesday': 'C',
    'Wednesday': 'D',
    'Thursday': 'E',
    'Friday': 'F',
    'Saturday': None
}


def read_sheet_from_xlsx_file(xlsx_file: str):
    """
    Read a excel workbook and returns the active spreadsheet
    """
    book = openpyxl.load_workbook(xlsx_file)
    return book.active


def create_today_schedule_message(sheet, weekday: str) -> str:
    """
    Reads cells from a excel spredsheet and returns a string with all today classes
    """
    if WEEKDAYS_FOR_SCHEDULE[weekday] is None:
        return ''

    today_classes = ['_*Aulas de Hoje:*_']
    for row in range(2, sheet.max_row + 1):
        today_classes.append(f'\t* {row - 1}ª Aula: ' + sheet[f'{WEEKDAYS_FOR_SCHEDULE[weekday]}{row}'].value )
    
    return '\n'.join(today_classes)


def read_json_file(json_file: str):
    """
    Reads a JSON file and returns it after loading it
    """

    with open(json_file, encoding='utf-8') as reminders_file:
        logging.debug('Readging JSON file...')
        reminders_data = json.load(reminders_file)
    
    logging.debug('Reading finished!')
    return reminders_data


def get_date() -> str:
    """
    Returns the date that will be used to filter the messages, based wheter or not the
    user provided a date (dd/mm format) to the program
    """
    
    if len(sys.argv) == 1:
        program_date = datetime.datetime.now().strftime('%d/%m')

    else:
        program_date = sys.argv[1]

    return program_date


def get_reminders_from_json(file) -> str:
    """
    Analysis the JSON file and saves only the messages that were meant to be sent on
    the provided date, then returns a string of the joined messages
    """

    messages = Enhanced_Reminders_List()
    reminders_data = read_json_file(file)
    program_date = get_date()

    for title in reminders_data:
        if not title['Messages']:
            continue

        messages.append(title['Title'])            
        
        starting_len = len(messages)

        for reminder in title['Messages']:
            if program_date in reminder['dates'] or reminder['dates'] == 'ALWAYS':
                messages.append(reminder['message'], data=program_date)
        
        if starting_len == len(messages):
            messages.pop()

    return ('*[Por favor leiam até o final]*\n_Data do boletim de lembretes: %s_ \
     \nLembretes:\n%s' % (program_date, '\n'.join(messages),))


async def match_pixel(x, y, *color):
    """
    # TODO: Add docstring
    """
    while not pyautogui.pixelMatchesColor(x, y, color):
        await asyncio.sleep(1)


async def open_whatsapp_web() -> None:
    """
    Opens web.whatsapp.com on Google Chrome and wait til it loads
    """

    webbrowser.register(
        'chrome',
        None,
        webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    )
    webbrowser.get('chrome').open_new('web.whatsapp.com')

    match_color_task = asyncio.create_task(match_pixel(24, 399, 84, 114, 91))
    await match_color_task
    

def send_message() -> None: 
    """
    Request the opening of web.whatsapp.com and paste the clipboard content 
    on the desired group
    """

    asyncio.run(open_whatsapp_web())
    pyautogui.click(24, 399)
    time.sleep(0.5)
    pyautogui.click(638, 738)
    pyautogui.hotkey('ctrl', 'v')


async def close_link_popup(message: str) -> None:
    if not re.match('http*', message):
        return None

    match_color_task = asyncio.create_task(match_pixel(1331, 587, 134, 150, 160))
    await asyncio.sleep(0.5)
    await match_color_task
    pyautogui.click(1331, 587)
