import datetime

mydatetime = datetime.datetime(1970,2,1,0,0,0)
print(f"{mydatetime} 타입 {type(mydatetime)}")

howmany = int(mydatetime.timestamp())
print(f"{howmany}초")

