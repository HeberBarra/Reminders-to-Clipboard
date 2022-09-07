import logging
import datetime
logging.basicConfig(filename='remindersLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

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


class Enhanced_Reminders_List(list):

    def append(self, object, /, data=None):

        if not isinstance(object, str):
            return super().append(object)  
        
        if data is None:
            return super().append(object)

        # Date related 
        
        day = datetime.datetime.now().strftime('%d')
        month = datetime.datetime.now().strftime('%B')
        month_name = MONTH_EN_TO_PT[month]

        if f'dia: {day}/{month}' in object:
            logging.debug('Date matches! | dia: dd/mm')
            object = object.replace(f'dia: {day}/{month}', 'hoje')

        if f'Dia: {day}/{month}' in object:
            logging.debug('Date matches! | Dia: dd/mm')
            object = object.replace(f'Dia: {day}/{month}', 'hoje')

        if f'dia: {day} de {month_name}' in object.lower():
            logging.debug('Date matches! | dia: dia de mês')
            object = object.replace(f'dia: {day} de {month_name}', 'hoje')

        if f'Dia: {day} de {month_name}' in object:
            logging.debug('Date matches! | Dia: dia de mês')
            object = object.replace(f'Dia: {day} de {month_name}', 'hoje')

        if f'{day} de {month_name}' in object.lower():
            logging.debug('Date matches! | dia de mês')
            object = object.replace(f'{day} de {month_name}', 'hoje')

        if datetime.datetime.now().strftime('%d/%m') in data:
            logging.debug('Date matches! | %d/%m')
            object = object.replace(data, 'hoje')

        return super().append(object)
