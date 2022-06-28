from common.enums import WeekHandle


class FantasyWeeks:

    def __init__(self):
        self.week_repeats = WeekHandle.CONTINUES

        self.is_holy_week = False
        self.week_id = "#YYYYMMMMDDDD"
        self.week_name = ""
        self.week_month_name = ""
        self.week_month_number = 0

    @property
    def week_repeats(self):
        return self.week_repeats

    @week_repeats.setter
    def week_repeats(self, value):
        self.week_repeats = value

    @property
    def is_holy_week(self):
        return self.is_holy_week

    @is_holy_week.setter
    def is_holy_week(self, value):
        self.is_holy_week = value

    @property
    def week_id(self):
        return self.week_id

    @week_id.setter
    def week_id(self, value):
        self.week_id = value

    @property
    def week_name(self):
        return self.week_name

    @week_name.setter
    def week_name(self, value):
        self.is_holy_week = value

    @property
    def week_month_name(self):
        return self.week_month_name

    @week_month_name.setter
    def week_month_name(self, value):
        self.week_month_name = value

    @property
    def week_month_number(self):
        return self.week_month_number

    @week_month_number.setter
    def week_month_number(self, value):
        self.week_month_number = value
