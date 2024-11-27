import datetime
cd=datetime.datetime.today()
print(f"current date={cd}")
d=datetime.date.today()
print(f"date={d}")
e=cd=datetime.datetime.now().time()
print(f"time={e}")
sp=datetime.date(2023,9,23)
print(f"specific time:{sp}")
sp1=datetime.time(14,30,45)
print(f"specific time:{sp1}")
sp2=datetime.datetime(2024,9,23,14,30,45)
print(f"specific time:{sp2}")
#formatting
formatting_date=cd.strftime("%Y-%m-%d %H:%M:%S")
print(f"date and time:",formatting_date)
#Parsing
date_string="2024-09-23 14:30:45"
parsed_date=datetime.datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S")
print("Parsed datetime object:",parsed_date)
#Timedate
#create
ten_days=datetime.timedelta(days=10)
#subtract
date_10_days_ago=cd-ten_days
print("Date 10 days ago:",date_10_days_ago)
#add
date_10_days_later=cd+ten_days
print("Date 10 days later:",date_10_days_later)



