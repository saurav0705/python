import calendar
def f_calender():
    #here sunday ,saturday is the moth from which calender has to be started
    #and 2024 is the year and 5 is the month
    cal=calendar.TextCalendar(calendar.SUNDAY)
    s=cal.formatmonth(2024,5)
    print (s)
    cal=calendar.TextCalendar(calendar.SATURDAY)
    s=cal.formatmonth(2024,4)
    print(s)
    #now thml calender
    #cal=calendar.HTMLCalendar(calendar.SUNDAY)
    #s=cal.formatmonth(2024,5)
    #print (s)
    #for i in cal.itermonthdays(2024,4):
        #print (i)
    for name in calendar.month_name:
        print (name)
    print ("\n")
    for weekday in calendar.day_name:
        print(weekday)

def example():
    for month in range(1,13):
        cal=calendar.monthcalendar(2025, month)
        week1=cal[0]
        week2=cal[1]
        if week1[calendar.MONDAY] != 0:
            auditday = week1[calendar.MONDAY]
        else:
             # if the second MONDAY isn't in the first week, it must be in the second week
            auditday = week2[calendar.MONDAY]
            print("%10s %2d" % (calendar.month_name[month],auditday))

f_calender()
example()