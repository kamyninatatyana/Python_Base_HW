
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        """ Takes date in format DD-MM-YYYY and extracts day, month and year in int format."""
        day, month, year = map(int, date.split("-"))
        return f"Day - {day}, month - {month}, year - {year}"

    @staticmethod
    def date_items_validation(day, month, year):
        """Check if all components of the date (day, month, year) are correct according to following criteria:
            1. Neither component can not be less or equal to zero.
            2. The day can not exceed the maximum number of days in the correspondence month.
            3. The month can not exceed the maximum number of days in the year."""

        day_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        print("Year OK") if year > 0 else print("Year should be above zero.")
        print("Month OK.") if 0 < month <= 12 else print("Month should be in range of 1 to 12.")
        print("Day OK.") if 0 < day <= day_in_month[month] else print("Day should be above zero and not exceed the "
                                                                      "maximum number of days in the month.")

