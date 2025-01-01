from section.section import Section
from data.reminders_data import RemindersData


class SectionDAO:
    def __init__(self, reminders_data: RemindersData):
        self._reminders_data = reminders_data

    def _get_sections_json(self) -> list:
        return self._reminders_data.json_data['reminders']

    def create(self, section: Section):
        for i in range(len(self._reminders_data.json_data['reminders'])):
            if self._reminders_data.json_data['reminders'][i]['Title'] == section.title:
                print('The specified section already exists.')
                return None

        self._reminders_data.json_data['reminders'].append(section.get_dict())
        self._reminders_data.save()

    def list_sections(self) -> list[Section]:
        sections: list[Section] = []
        sections_json = self._get_sections_json()
        for i in range(len(sections_json)):
            section_data = sections_json[i]
            section = Section(section_data['Title'], section_data['Messages'])
            sections.append(section)

        return sections

    def find_by_title(self, section_title: str) -> Section | None:
        sections_json = self._get_sections_json()
        for i in range(len(sections_json)):
            if sections_json[i]['Title'] == section_title:
                return Section(sections_json[i]['Title'], sections_json[i]['Messages'])

        return None

    def update(self, section: Section):
        sections_json = self._get_sections_json()
        for i in range(len(sections_json)):
            if sections_json[i]['Title'] == section.title:
                updated_section = {'Title': section.title, 'Messages': section.messages}
                sections_json[i] = updated_section
                break

        self._reminders_data.save()

    def delete(self, section: Section):
        sections_json = self._get_sections_json()
        for i in range(len(sections_json)):
            if sections_json[i]['Title'] == section.title:
                section_dict = {'Title': section.title, 'Messages': section.messages}
                sections_json.remove(section_dict)
                self._reminders_data.save()
                return

        print(f'Section {section.title} not found!')
