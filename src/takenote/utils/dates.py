from datetime import date, timedelta


def get_monday(the_date: date):
    return the_date - timedelta(days=(the_date.isoweekday()-1))
