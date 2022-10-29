from Reminders import Reminders_Functions

def main():
    first_date = input('Digite a primeira data: '.strip())
    second_date = input('Digite a segunda data: '.strip())
    dates = Reminders_Functions.date_interval(first_date, second_date)
    print('[', end='')
    for date in dates:
        print(f'"{date}", ' if date != dates[-1] else f'"{date}"', end='')
    print(']')

if __name__ == '__main__':
    main()
