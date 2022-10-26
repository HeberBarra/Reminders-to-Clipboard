from Reminders import Reminders_Functions

def main():
    first_date = input('Digite a primeira data: '.strip())
    second_date = input('Digite a segunda data: '.strip())
    print(Reminders_Functions.date_interval(first_date, second_date))


if __name__ == '__main__':
    main()
