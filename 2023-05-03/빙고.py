# 컴퓨터 : 0~10 사이 임의 숫자(random) 
# 사람 : 숫자 입력 0~10이 아니면 오류체크
# 컴퓨터숫자와 사람숫자비교 
# 컴퓨터왈 “더크다“/ “더 작다” / ‘빙고!!’(두 수가 같다 사람이 1점 획득)
# 사용자가 ‘quit’를 입력하면 프로그램 종료(exit())
# 비교 횟수, 컴퓨터 와 사용자의 점수 출력 

import random as rr

com = rr.randint(0,10)
user = int(input("0~10 숫자 입력>>"))
score = 0

if user<0 or user > 10:
    print("입력오류")
    exit()

if com==user :
    score += 1


    
 