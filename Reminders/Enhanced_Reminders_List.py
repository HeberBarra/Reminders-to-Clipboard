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

    def append(self, object, /, data=None):

        if not isinstance(object, str):
            return super().append(object)  
        
        if data is None:
            return super().append(object)

        # Date related 
        
        day = datetime.datetime.now().strftime('%d')
        month = datetime.datetime.now().strftime('%B')
        month_name = self.month_en_to_pt[month]

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

        if datetime.datetime.now().strftime('%d/%m') in data:
            object = object.replace(data, 'hoje')

        return super().append(object)
