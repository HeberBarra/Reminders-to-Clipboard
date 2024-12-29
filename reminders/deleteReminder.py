def getUndeletedRemindersData(data, date, section_index=0, undeleted_data=None):
    if undeleted_data is None:
        undeleted_data = []

    for section in data:
        undeleted_data.append({'Title': section['Title'], 'Messages': []})

        for reminder in section['Messages']:
            if (reminder['dates'] == 'ALWAYS') or (date in reminder['dates']):
                undeleted_data[section_index]['Messages'].append(reminder)

        section_index += 1

    return undeleted_data
