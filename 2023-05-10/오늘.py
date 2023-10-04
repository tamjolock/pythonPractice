# (문제1) 오늘 날짜를 출력하세요
# 예 : **** 년 **** 월 ****일 (**요일)

import datetime

weeknames = ["월","화","수","목","금","토","일"]

today = datetime.datetime.now() #today()

today_year = today.year
today_month = today.month
today_day = today.day
today_weekname = today.weekday()

# print(f"{today}, {type(today)}")
# print(f"**today_weekname{today_weekname}")
print(f"오늘은 {today_year}년 {today_month}월 {today_day}일 {weeknames[today_weekname]}요일 ",end="")

ampm = "오전"

today_hour = today.hour

if today_hour > 12:
    ampm = "오후"
    today_hour = today_hour - 12

today_minute = today.minute
today_second = today.second

print(f"{ampm}{today_hour}시 {today_minute}분 {today_second}초 입니다.")
