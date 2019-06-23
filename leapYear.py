# B_R_R
# M_S_A_W


""" 
This funciton defines if given year is leap year and tells how many days it has.
We can further work on this program which could include two function, first prompts to enter a number until twelve and prints out
the name of that month.
Second asks year and tells if it is leap_year

"""
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year%4==0 and year%100!=0


def days_in_month(year, month):

    if not 1<=month<=12:
        return "Invalid Month"
    if month==2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 3))
