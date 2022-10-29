from Reminders import Reminders_Functions
import json

JSON_FILE = 'reminders.json' 
json_lines = Reminders_Functions.read_json_file(JSON_FILE)


def isOptionRight(message: str):
    while True:
        chosenOption = input(message)
        isRight = input('A escolha está correta?: ').lower()[0]

        if isRight in 'ysapc':
            return chosenOption 


def chooseSection() -> int:
    for index in range(len(json_lines)):
        print(f'[{index}] {Reminders_Functions.remove_title_special_parts(json_lines[index]["Title"])}')
    while True:
        chosen_section = int(isOptionRight('Escolha um seção: '))
        if chosen_section in [number for number in range(len(json_lines))]:
            return chosen_section
        
        print('Digite uma seção válida')


def showSection(index: int, file: list) -> None:
    for item in file[index]['Messages']:
        print(item['dates'])
        print(rf"{item['message']}", '\n')


def main():
    chosen_section = chooseSection()
    showSection(chosen_section, json_lines)
    
    # Reminder info
    start_date = isOptionRight('Qual a primeira data?: ')
    end_date = isOptionRight('Qual a última data?: ')
    new_message = isOptionRight('Qual a nova messagem?: ')
    date_interval = Reminders_Functions.date_interval(start_date, end_date)

    # Add reminder to json
    json_lines[chosen_section]["Messages"].append({"dates": date_interval, "message": new_message.replace('\\n', '\n').replace('\\t', '\t')})

    with open(JSON_FILE, 'w', encoding='utf-8') as j_file:
        json.dump(json_lines, fp=j_file, ensure_ascii=False)

if __name__ == '__main__':
    main()
