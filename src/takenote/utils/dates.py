from datetime import date, timedelta


def get_monday(the_date: date):
    return the_date - timedelta(days=(the_date.isoweekday()-1))

def format_header_date(the_date: date):
    return the_date.strftime("%A %d %B %Y")

def format_file_date(the_date: date):
    return the_date.strftime("%Y-%m-%d")
