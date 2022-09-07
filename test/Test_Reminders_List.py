import datetime
from Reminders.Enhanced_Reminders_List import Enhanced_Reminders_List


MONTH_EN_TO_PT = {
    'January': 'janeiro',
    'Febuary': 'fevereiro',
    'March': 'março',
    'April': 'abril',
    'May': 'maio',
    'June': 'junho',
    'July': 'julho',
    'August': 'agosto',
    'September': 'setembro',
    'October': 'outubro',
    'November': 'november',
    'December': 'dezembro'
}
DATE_DD_MM = datetime.datetime.now().strftime('%d/%m') # dd/mm
DAY = datetime.datetime.now().strftime('%d') # dd
MONTH = MONTH_EN_TO_PT[datetime.datetime.now().strftime('%B')] # month name in portuguese
DAY_OF_MONTH = f'{DAY} de {MONTH}' # dd de (month_name in portuguese)
ALTERNATIVE_DAY_OF_MONTH = f'dia: {DAY} de {MONTH}'

class TestRemindersList:
    
    def test_change_dd_mm_format(self):
        test_list = Enhanced_Reminders_List()
        test_list.append(DATE_DD_MM, data=DATE_DD_MM)
        assert test_list[0] == 'hoje'

    def test_change_day_of_month(self):
        test_list = Enhanced_Reminders_List()
        test_list.append(DAY_OF_MONTH, data=DATE_DD_MM)
        test_list.append(ALTERNATIVE_DAY_OF_MONTH, data=DATE_DD_MM)
        test_list.append(ALTERNATIVE_DAY_OF_MONTH.capitalize(), data=DATE_DD_MM)
        assert test_list[0] == 'hoje'
        assert test_list[1] == 'dia: hoje'
        assert test_list[2] == 'Dia: hoje'
