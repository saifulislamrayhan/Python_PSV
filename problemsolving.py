import calendar
m1,d1,y1=input().split()
m=int(m1)
d=int(d1)
y=int(y1)
if((y>2000) & (y<3000)):
    day=calendar.weekday(y,m,d)
    m=calendar.month_name[m]
    val=calendar.day_name[day]
    val=val.upper()
    print("The day on",m,d1,"th was",val)

else:
    quit()

