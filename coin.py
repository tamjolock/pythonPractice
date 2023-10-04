# 동전게임. 컴퓨터 앞 뒤 랜덤 지정
# 사람이 정한 앞뒤 중 하나와 비교 승패 출력
import random as rr

while True :
    comp = rr.randrange(0,2)
    person = input("앞 뒤 중에서 고르시오>>")
    cho = ''

    if person not in ['앞','뒤','p']:
        raise IOError("앞 뒤 p중에 골라주세요")

    if comp == 0:
        cho = '뒤'

    elif comp == 1:
        cho = '앞'

    if person == 'p' :
        break

    elif person == cho :
        print(f"{cho},your win")
       
    elif person != cho :
        print(f"{cho},lose")
    continue
   