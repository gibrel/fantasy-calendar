

class FantasyDay:

    def __init__(self):
        self.is_holiday = False
        self.day_id = "#YYYYMMMMDDDD"
        self.day_name = ""
        self.day_month_name = ""
        self.day_month_number = 0
        self.day_week_name = ""
        self.day_week_number = 0

    @property
    def is_holiday(self):
        return self.is_holiday

    @is_holiday.setter
    def is_holiday(self, value: bool):
        self._is_holiday = value

    @property
    def day_id(self):
        return self.day_id

    @day_id.setter
    def day_id(self, value: str):
        self.day_id = value

    @property
    def day_name(self):
        return self.day_name

    @day_name.setter
    def day_name(self, value: str):
        self.day_name = value

    @property
    def day_month_name(self):
        return self.day_month_name

    @day_month_name.setter
    def day_month_name(self, value: str):
        self.day_month_name = value

    @property
    def day_month_number(self):
        return self.day_month_number

    @day_month_number.setter
    def day_month_number(self, value: int):
        self.day_month_number = value

    @property
    def day_week_name(self):
        return self.day_week_name

    @day_week_name.setter
    def day_week_name(self, value: str):
        self.day_week_name = value

    @property
    def day_week_number(self):
        return self.day_week_number

    @day_week_number.setter
    def day_week_number(self, value: int):
        self.day_week_number = value
