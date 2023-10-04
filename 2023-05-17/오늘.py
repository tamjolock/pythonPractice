import datetime 
days7 = ["월","화","수","목","금","토","일"]

today = datetime.date.today()

todaystr = today.strftime("%Y년%m월%d일")

todayname = days7[today.weekday()]

print(f"{todaystr} {todayname}요일")


