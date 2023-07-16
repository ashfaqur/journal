class Month:

    def __init__(self, date, days):
        self.date = date
        self.days = days

    def get_days(self):
        return self.days

    def __str__(self):
        return self.date.strftime('%B %Y')
