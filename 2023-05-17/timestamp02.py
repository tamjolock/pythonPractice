# 문제2) 1970년 1월 1일 이후 ** 년  ** 일 ** 시간 ** 분 ** 초가 지났습니다.
#1달을 30일로 가정한다.
import datetime

today = datetime.datetime.today()
manysec = today.timestamp()
print(f"****{manysec}타임 : {type(manysec)}")

second = int(manysec)%60
minute00 = int(manysec)//60#60으로 초를 나누어서 분으로 만든 모든것 (전부 분)

minute = int(minute00)%60 # 분들을 60으로 나누어서 남은 분
hours00 = int(minute00)//60# 모든 시

hours  = int (hours00)%24 #모든 시를 24로 나누어 남은 시간
days00 = int (hours00)//24 # 시간들을 날 모두 날로

days= int (days00)%30 # 모든 날을 한달에 30으로 나누어 남은 날
month00= int (days00)//30 # 모든날을 30으로 나누어 나온 달

month =int (month00)%12 # 달을 1년 12개월 로 나누어 남은 달
years=int(month00)//12 # 달을 넘어 년으로 남은 몇년




print (f"{years}년{month}달{days}날{hours}시{minute}분{second}초")