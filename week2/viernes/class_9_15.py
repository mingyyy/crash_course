'''
9-15. Python Module of the Week: One excellent resource for exploring the Python standard library
is a site called Python Module of the Week . Go to http://pymotw.com/ and look at the table of contents .
Find a module that looks interesting to you and read about it,
or explore the documentation of the collections and random modules .
'''
import calendar
import datetime


c = calendar.TextCalendar(calendar.MONDAY)
c.prmonth(2019, 2)

c = calendar.LocaleTextCalendar(locale="es_ES")
c.prmonth(2019, 3)

d1 = datetime.date(2019, 2, 15)
print('d1:', d1.isoformat())


def num_days_after_date(start_date, num_of_days, including_ends=False):
    '''
    This function tells the date after certain number of days from the starting date you entered
    start_date: to be in a list [yyyy, mm, dd]
    num_of_days: an integer represent how many days after the current date
    including_ends: defaulted at False means only including the beginning or the end of the period, not both
    True would mean both ends are counted
    '''
    year = start_date[0]
    month = start_date[1]
    day = start_date[2]
    if including_ends is True:
        num_of_days -= 1

    d1 = datetime.date(year, month, day)
    n = datetime.timedelta(num_of_days)
    d2 = d1 + n
    return d2


leave_bali = num_days_after_date([2019, 2, 15], 30, True)
print(leave_bali)

leave_bali = num_days_after_date([2019, 3, 17], 30, True)
print(leave_bali)