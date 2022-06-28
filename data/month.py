

class FantasyMonths:

    def __init__(self):
        self.is_holy_month = False
        self.month_id = "#YYYYMMMMDDDD"
        self.month_name = ""

        self.days = []

    @property
    def is_holy_month(self):
        return self.is_holy_month

    @is_holy_month.setter
    def is_holy_month(self, value):
        self.is_holy_month = value

    @property
    def month_id(self):
        return self.month_id

    @month_id.setter
    def month_id(self, value):
        self.month_id = value

    @property
    def month_name(self):
        return self.month_name

    @month_name.setter
    def month_name(self, value):
        self.month_name = value

    def list_days(self):
        return self.days

    def count_days(self):
        return len(self.days)

    def add_day(self, day):
        self.days.insert(day)

    def remove_day(self, day):
        self.days.remove(day)
