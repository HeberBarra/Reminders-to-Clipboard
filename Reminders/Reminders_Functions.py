import sys
import json
import datetime
import logging
import webbrowser
import time
import asyncio
import pyautogui
import openpyxl
from Reminders.Enhanced_Reminders_List import Enhanced_Reminders_List

logging.basicConfig(filename='remindersLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

WEEKDAYS_FOR_SCHEDULE = { 
    # Equivalent weekdays to cells letters 
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
    Reads cells from a .xlsx spreadsheet and returns a string with all today classes
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


def get_date() -> tuple[str]:
    """
    Returns the date that will be used to filter the messages, based whether or not the
    user provided a date (dd/mm/yy format) to the program
    """
    
    if len(sys.argv) == 1:
        program_date = datetime.datetime.now().strftime('%d/%m/%y')

    else:
        program_date = sys.argv[1]

    weekday = datetime.datetime.strptime(program_date, '%d/%m/%y').strftime('%A')
    return program_date, weekday


def get_reminders_from_json(file, program_date: str) -> str:
    """
    Analyses the JSON file and saves only the messages that were meant to be sent on
    the provided date, then returns a string of the joined messages
    """

    messages = Enhanced_Reminders_List()
    reminders_data = read_json_file(file)
    program_date = '/'.join(program_date.split('/')[:2])
    logging.debug(program_date)
    
    for title in reminders_data:
        if not title['Messages']:
            continue

        messages.append(title['Title'])            
        
        starting_len = len(messages)

        for reminder in title['Messages']:
            if program_date in reminder['dates'] or reminder['dates'] == 'ALWAYS':
                messages.append(reminder['message'], date=program_date)
        
        if starting_len == len(messages):
            messages.pop()

    return ('Bom dia, que a paz possa ser convosco! *[Por favor leiam até o final]*\n_Data do boletim de lembretes: %s_ \
     \nLembretes:\n%s' % (program_date, '\n'.join(messages),))


async def match_pixel(x, y, *color):
    """
    Loops untial the pixel in the provided x, y position matches the provided color
    """
    while not pyautogui.pixelMatchesColor(x, y, color):
        await asyncio.sleep(1)


async def open_whatsapp_web(x, y, *color) -> None:
    """
    Opens web.whatsapp.com on Google Chrome and wait til it loads
    """

    webbrowser.register(
        'chrome',
        None,
        webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    )
    webbrowser.get('chrome').open_new('web.whatsapp.com')

    match_color_task = asyncio.create_task(match_pixel(x, y, *color))
    await match_color_task
    

def send_message(contact_x: int, contact_y: int, message_field_x: int, message_field_y: int) -> None: 
    """
    Request the opening of web.whatsapp.com and paste the clipboard content 
    on the desired group
    """
    if len(sys.argv) == 3 and sys.argv[2] == "dontsend":
        return

    asyncio.run(open_whatsapp_web(24, 399, 84, 114, 91))
    pyautogui.click(contact_x, contact_y)
    time.sleep(1)
    pyautogui.click(message_field_x, message_field_y)
    pyautogui.hotkey('ctrl', 'v')


def date_interval(start, end):
    date = datetime.datetime.strptime(start, '%d/%m/%y')
    end_date = datetime.datetime.strptime(end, '%d/%m/%y')
    date_interval = []
    while end_date >= date:
        date_interval.append('"' + datetime.datetime.strftime(date, '%d/%m') + '"')
        date += datetime.timedelta(days=1) 
    
    return '[' + ', '.join(date_interval) + ']'
