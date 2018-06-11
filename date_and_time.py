from datetime import date,time,datetime,timedelta

def f_date():
    #note:: if you want to print multiple values in
    #a single print statement you must convert the data type to string 
    today=date.today()
    print (date.today())
    print ("day::"+str(today.day))
    print ("month::"+str(today.month))
    print ("year::"+str(today.year))
    #print("day:: "+str(today.day)+"  month:: "+str(today.month))
    #weekdays(0==monday   6==sunday)
    print("weekday:: "+str(today.weekday()))


def f_datetime():
    #it gives us full info on current date and time
    print(datetime.now())
    print ("to print only current time "+str(datetime.time(datetime.now())))
    #strftime to format time output
    # [%y/%y--year]
    #[%a%A--weekday]
    #[%b/%B--month]
    #[%d--day of the month]
    print(datetime.now().strftime("%Y %d"))
    print (datetime.now().strftime("%c"))
    print (datetime.now().strftime("%X"))
    print (datetime.now().strftime("%x"))
    print (datetime.now().strftime("%I:%M:%S %p"))
    print (datetime.now().strftime("%H:%M"))

def f_timedelta():
    #basic function of timedelta is time calculation example--
    print("in 11 days 4hrs abd 36s from now\n::"+str(datetime.now()+timedelta(days=11,hours=4,seconds=6)))
    #we can also calculate  diff b/w current date and date entered in it example--
    day=date(date.today().year,1,1)
    day=(date.today()-day).days
    print ("new yr was %d days ago"%day)

f_date()
f_datetime()
f_timedelta()