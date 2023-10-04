# <컴퓨터 숫자 맞추기>
# 컴퓨터 : 0~10 사이 임의 숫자(random) 
# 사람 : 숫자 입력 0~10이 아니면 오류체크
# 컴퓨터숫자와 사람숫자비교 
# 컴퓨터왈 “더크다“/ “더 작다” / ‘빙고!!’(두 수가 같다 사람이 1점 획득)
# 사용자가 ‘quit’를 입력하면 프로그램 종료(exit())

import random as rr

com = rr.randint(0,10)
point = 0

while True:

    user = int(input("0~10 숫자 입력>>"))
    print({com})

    if user>10 or user<0 :
        print(f"숫자를 범위안에서 지정해주세요")
        exit()

    if user == "quit":
        break

    if user == com :
        point += 1
        print(f"빙고!! 점수:{point}")
        continue

    elif user < com :
        print("더 크다")
        continue
        
    elif user > com :
        print("더 작다")
        continue