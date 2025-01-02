from config.configurator import Configurator
from reminders.reminders_data import RemindersData
from utils import date_utils
from utils import input_utils
from utils import json_utils
from reminders import reminder_json
from reminders.reminder import Reminder
from reminders.reminder_dao import ReminderDAO
from section.section import Section
from section.section_dao import SectionDAO
from schedule import schedule
import datetime
import pyperclip


reminder_dao: ReminderDAO
section_dao: SectionDAO
configurator: Configurator
reminders_data: RemindersData

MENU_CREATE_SECTION = 0
MENU_LIST_SECTIONS = 1
MENU_DETAIL_SECTION = 2
MENU_CHANGE_SECTION_TITLE = 3
MENU_DELETE_SECTION = 4
MENU_CREATE_REMINDER = 5
MENU_LIST_REMINDERS = 6
MENU_COPY_REMINDERS = 7
MENU_DELETE_OUTDATED_REMINDERS = 8
EXIT = 9


def show_menu():
    print(f'[{MENU_CREATE_SECTION}] Create section')
    print(f'[{MENU_LIST_SECTIONS}] List sections')
    print(f'[{MENU_DETAIL_SECTION}] Detail section')
    print(f'[{MENU_CHANGE_SECTION_TITLE}] Change section title')
    print(f'[{MENU_DELETE_SECTION}] Delete selection')
    print(f'[{MENU_CREATE_REMINDER}] Create reminder')
    print(f'[{MENU_LIST_REMINDERS}] List reminders')
    print(f'[{MENU_COPY_REMINDERS}] Copy reminders')
    print(f'[{MENU_DELETE_OUTDATED_REMINDERS}] Delete outdated reminders')
    print(f'[{EXIT}] Exit')


def create_section():
    section_title = input_utils.is_option_right(
        "What's the title of the new section?: "
    )
    section_dao.create(Section(section_title))


def list_sections():
    sections = section_dao.list_sections()

    for section in sections:
        print(f'[ {section.title} ]')


def detail_section(section_index: int, section=None):
    if section is None:
        section = section_dao.find_by_id(section_index)

    print(f'Section: {section.title}')
    for message in section.messages:
        print(f'ID: {message['localID']}')
        print(f'Dates: {message['dates']}')
        print(f'Message: {message['message']}')
        print()


def change_section_title(old_title: str, new_title: str):
    section = section_dao.find_by_title(old_title)
    section.title = new_title
    section_dao.update_title(section, old_title)


def delete_section(section_index: int):
    section = section_dao.find_by_id(section_index)
    section_dao.delete(section)


def create_reminder(section_index: int):
    section = section_dao.find_by_id(section_index)

    if section is None:
        print('Invalid section! Cancelling operation')
        return

    date_format = '%d/%m/%y'
    detail_section(section_index)

    start_date = input_utils.is_option_right("What's the first date?: ")
    end_date = input_utils.is_option_right("What's the last date?: ")
    message = input_utils.is_option_right("What's the new message?: ")

    initial_date = datetime.datetime.strptime(start_date, date_format)
    last_date = datetime.datetime.strptime(end_date, date_format)

    reminder = Reminder(initial_date, last_date, section.title, section_index, message)
    reminder_dao.create(reminder)


def list_reminders():
    for section in section_dao.list_sections():
        detail_section(0, section)


def copy_reminders():
    program_weekday = date_utils.get_current_date()[1]
    original_clipboard_content = pyperclip.paste()
    current_date = date_utils.get_current_day_month_date()

    reminders_content = (
        schedule.get_formatted_schedule(
            configurator.schedule_xlsx_filepath,
            configurator.schedule_message,
            program_weekday,
        )
        + '\n'
        + reminder_dao.list_reminders_formatted(
            configurator.header_message, current_date
        )
    )

    print(f'Preview: \n{reminders_content}')
    pyperclip.copy(reminders_content)
    input('Press enter to restore original clipboard content...')
    pyperclip.copy(original_clipboard_content)


def delete_outdated_reminders():
    current_date = date_utils.get_current_day_month_date()
    reminders_data.json_data['reminders'] = reminder_dao.list_valid_reminders_json(current_date)
    reminders_data.save()


def main():
    global configurator
    global reminders_data
    global reminder_dao
    global section_dao

    configurator = Configurator('config/config.json')
    reminders_file = configurator.reminders_json_filepath
    reminder_json.create_reminders_file(reminders_file)
    reminders_data = RemindersData(
        json_utils.read_json_file(reminders_file), reminders_file
    )
    reminder_dao = ReminderDAO(reminders_data)
    section_dao = SectionDAO(reminders_data)

    while True:
        try:
            show_menu()
            chosen_option = int(input_utils.is_option_right('Choose a option: '))

            if chosen_option == MENU_CREATE_SECTION:
                create_section()
            elif chosen_option == MENU_LIST_SECTIONS:
                list_sections()
            elif chosen_option == MENU_DETAIL_SECTION:
                section_index = input_utils.choose_section(reminders_data.json_data)
                detail_section(section_index)
            elif chosen_option == MENU_CHANGE_SECTION_TITLE:
                old_section_index = input_utils.choose_section(reminders_data.json_data)
                new_title = input_utils.is_option_right("What's the new title?: ")
                old_section = section_dao.find_by_id(old_section_index).title
                change_section_title(old_section, new_title)
            elif chosen_option == MENU_DELETE_SECTION:
                section_index = input_utils.choose_section(reminders_data.json_data)
                delete_section(section_index)
            elif chosen_option == MENU_CREATE_REMINDER:
                section_index = input_utils.choose_section(reminders_data.json_data)
                create_reminder(section_index)
            elif chosen_option == MENU_LIST_REMINDERS:
                list_reminders()
            elif chosen_option == MENU_COPY_REMINDERS:
                copy_reminders()
            elif chosen_option == MENU_DELETE_OUTDATED_REMINDERS:
                delete_outdated_reminders()
            elif chosen_option == EXIT:
                exit(0)
            else:
                print('Invalid option! Please try again...')

        except ValueError:
            print('Invalid option! Please try again...')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram terminating...')
