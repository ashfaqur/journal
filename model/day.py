class Day:

    def __init__(self, date):
        self.date = date
        self.notes = []

    def get_notes(self):
        return self.notes

    def display_date(self):
        return self.date.strftime('%d %B %Y')

    def __str__(self):
        return self.display_date()

    def print_notes(self):
        [print(note) for note in self.notes]

    def add_content(self, content):
        self.notes.append(content)
