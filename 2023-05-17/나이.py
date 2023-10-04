# (문제4) 생년월일을 입력 받아 나이 출력
# 1.생년월일 입력
# 2.date타입으로 변환
# 3.오늘 날짜 설정
# 4.오늘 - 생년

import datetime
mybirthday=input("생년월일 입력>>(yyyy-mm-dd)")

mydate=datetime.datetime.strptime(mybirthday,"%Y-%m-%d")

today = datetime.date.today()

if today.year<mydate.year:
    print("입력오류")
else:
    age = today.year-mydate.year
    print(age,type(mydate))
    





