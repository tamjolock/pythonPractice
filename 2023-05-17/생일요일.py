# (문제5) 나의 생일은 *** 요일 : datetime.weekday()

import datetime

days7 = ["월","화","수","목","금","토","일"]
mybirthday=input("생년월일 입력>>(yyyy-mm-dd)")

mydate=datetime.datetime.strptime(mybirthday,"%Y-%m-%d")
birthstr = mydate.strftime("%Y년 %m월 %d일")

myweek=days7[mydate.weekday()]
print(f"난 {birthstr} {myweek}요일에 태어남")


