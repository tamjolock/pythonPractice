# (문제7) 내가 태어난 후 ***일이 지났어요
import datetime

mybirthday=input("생년월일 입력>>(yyyy-mm-dd)")

mydate=datetime.datetime.strptime(mybirthday,"%Y-%m-%d")
# birthstr = mydate.strftime("%Y년 %m월 %d일")
today = datetime.date.today()

year = today.year - mydate.year
month = today.month - mydate.month
day = today.day - mydate.day

days = (year*365) + (month*30) + day

print(f" 내가 태어난 후 {days}일이 지났어요")