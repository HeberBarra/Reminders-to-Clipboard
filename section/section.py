import dataclasses


@dataclasses.dataclass
class Section:
    title: str
    messages: list[str]

    def __init__(self, title: str, messages: list[str] = None):
        if messages is None:
            messages = []

        self.title = title
        self.messages = messages

    def get_dict(self):
        return {'Title': self.title, 'Messages': self.messages}

    def __str__(self):
        return f'{{"Title": {self.title}, "Messages": {self.messages}}}'
