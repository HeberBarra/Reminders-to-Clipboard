#! python3
# RemindersToClipboard.py - analyses a JSON file and then copy to clipboard every message that was meant to be send today or to a specific date (day/month/year | 00/00/00)

import time
import pyperclip
from Reminders import Reminders_Functions

JSON_FILE = 'reminders.json'
XLSX_FILE = 'Horário.xlsx'


def main():
    # Register the starting time
    start = time.perf_counter()

    # Gets the date and weekday
    program_date, weekday = Reminders_Functions.get_date()  

    # Saves the original clipboard content so I don't lose any important thing that was there, well it only works with strings/texts
    original_clipboard_content = pyperclip.paste()

    # Creates the message string and sends it to through whatsapp web
    spreadsheet = Reminders_Functions.read_sheet_from_xlsx_file(XLSX_FILE)
    message = [Reminders_Functions.create_today_schedule_message(spreadsheet, weekday)]
    message.append(Reminders_Functions.get_reminders_from_json(JSON_FILE, program_date))
    message = '\n'.join(message)

    print(f'Preview: \n{message}')
    pyperclip.copy(message)
    Reminders_Functions.send_message(24, 399, 638, 738)

    # Restores the original clipboard content to my clipboard
    pyperclip.copy(original_clipboard_content)

    # Prints out how many seconds it took to run all the program
    print(f'\n{time.perf_counter() - start = :.2f}')


if __name__ == '__main__':
    main()
