from month import FantasyMonth


class FantasyYear:

    def __init__(self):
        self.is_leap_year = False
        self.year_id = "#YYYYMMMMDDDD"
        self.year_name = ""

        self.months = []

    @property
    def is_leap_year(self):
        return self.is_leap_year

    @is_leap_year.setter
    def is_leap_year(self, value: bool):
        self.is_leap_year = value

    @property
    def year_id(self):
        return self.year_id

    @year_id.setter
    def year_id(self, value: str):
        self.year_id = value

    @property
    def year_name(self):
        return self.year_name

    @year_name.setter
    def year_name(self, value: str):
        self.year_name = value

    def list_months(self):
        return self.months

    def count_months(self):
        return len(self.months)

    def add_month(self, month: FantasyMonth):
        self.months.insert(len(self.months), month)

    def remove_month(self, month: FantasyMonth):
        self.months.remove(month)
