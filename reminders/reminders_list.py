import datetime


class RemindersList(list):
    _month_en_to_pt = {
        'January': 'Janeiro',
        'February': 'Fevereiro',
        'March': 'Março',
        'April': 'Abril',
        'May': 'Maio',
        'June': 'Junho',
        'July': 'Julho',
        'August': 'Agosto',
        'September': 'Setembro',
        'October': 'Outubro',
        'November': 'Novembro',
        'December': 'Dezembro',
    }

    def append(self, value, /, date=None):
        if not isinstance(value, str):
            return super().append(value)

        if date is None:
            return super().append(value)

        # Date related

        day = date.split('/')[0]
        month = date.split('/')[1]
        month_name = self._month_en_to_pt[datetime.datetime.now().strftime('%B')]

        # This section of the class is meant for portuguese only
        if f'dia: {day}/{month}' in value:
            value = value.replace(f'dia: {day}/{month}', 'hoje')

        if f'Dia: {day}/{month}' in value:
            value = value.replace(f'Dia: {day}/{month}', 'hoje')

        if f'dia: {day} de {month_name}' in value.lower():
            value = value.replace(f'dia: {day} de {month_name}', 'hoje')

        if f'Dia: {day} de {month_name}' in value:
            value = value.replace(f'Dia: {day} de {month_name}', 'hoje')

        if f'{day} de {month_name}' in value.lower():
            value = value.replace(f'{day} de {month_name}', 'hoje')

        if f'{day}/{month}' in value:
            value = value.replace(f'{day}/{month}', 'hoje')

        return super().append(value)
