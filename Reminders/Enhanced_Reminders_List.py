import datetime

class Enhanced_Reminders_List(list):
    month_en_to_pt = {
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

    def append(self, object, /, date=None):

        if not isinstance(object, str):
            return super().append(object)  
        
        if date is None:
            return super().append(object)

        # Date related 
        
        day = date.split('/')[0]
        month = date.split('/')[1]
        month_name = self.month_en_to_pt[datetime.datetime.now().strftime('%B')]

        if f'dia: {day}/{month}' in object:
            object = object.replace(f'dia: {day}/{month}', 'hoje')

        if f'Dia: {day}/{month}' in object:
            object = object.replace(f'Dia: {day}/{month}', 'hoje')

        if f'dia: {day} de {month_name}' in object.lower():
            object = object.replace(f'dia: {day} de {month_name}', 'hoje')

        if f'Dia: {day} de {month_name}' in object:
            object = object.replace(f'Dia: {day} de {month_name}', 'hoje')

        if f'{day} de {month_name}' in object.lower():
            object = object.replace(f'{day} de {month_name}', 'hoje')

        if f'{day}/{month}' in object:
            object = object.replace(f'{day}/{month}', 'hoje')

        return super().append(object)
