import random as rr

#0임의 수를 입력 받아 
# 짝수 또는 0 또는 홀수임을 출력

""" num = int(input("임의의 수 입력>>"))

if num ==type(int):
    if num%2:
        print("짝수")
    elif num == 0:
        print("0 입력")
    else:
        print("홀수")
else:
    print("숫자를 입력하세요") """


#아이디와 암호를 입력 받아 
# 각각이 sweet / love24@이면 “환영합니다” 
# 아니면 “아이디 또는 암호를 확인하세요” 출력
""" 
iid,password = input("아이디와 비밀번호 입력>>").split(",")

if iid == "sweet" or password == "love24@" :
    print("환영합니다.")
else:
    print("꺼지십쇼") """

#입력 받은 수에  20을 더한 값을 출력
# 단 입력 값과 20을 더한 계산 값이
# 255를 초과하는 경우 
# 255를 출력해야 한다.

""" num = int(input("수를 입력>>"))

if num+20>255:

    num = 255
    print(num)

else:
    print(num+20) """

#점수를 입력 받아 
# 90점 이상이면 “A학점“,
#  80점 이상이면 “B학점“,
#  70점 이상이면 “C학점“, 
# 60점 이상이면 “D학점“, 
# 0~59이면 “F 학점” 출력
""" 
score = int(input("점수를 입력>>"))

if score > 90:
    print("A학점")
elif score > 80:
    print("B학점")
elif score > 70:
    print("C학점")
elif score > 60:
    print("D학점")
else:
    print("F학점")
 """

#0~100 사이의 수를 입력 받아 
#2의 배수 여부를 출력🡪무작위수 발생.


""" num = int(input("0~100 사이의 수를 입력>> "))

if num < 100:

    if num%2==0:
        print(f"{num}\n2의 배수")

    else:
        print(f"{num}\n2의 배수가 아님")

 """
 
#(문제) 이름씨의 BMI(신체 비만 지수)를 사용한 비만 상태 계산 후 출력

#이름 입력
#키 입력(cm)   ** cm>>m 
#몸무게 입력(kg)
#BMI = 몸무게 / 키 ** 2
#BMI가 18미만 : 저체중 / 18이상 23미만 : 정상 / 23이상 25미만 : 과체중 / 25이상 : 비만

""" name,lengh,weight = input("이름,키,몸무게 입력하세요>>").split(" ")

weight = int(weight)
lengh = int(lengh)


BMI = weight / lengh**2

print(f"{BMI:.2f}" )
print (f"{name} 씨 ")
if BMI<18:
    print(f"{BMI}저체중")
elif 23>BMI>18:
    print(f"{BMI}정상")
else:
    print(f"{BMI}과체중") """




#로또 3 숫자 반복문 쓰지않고 만들기
while True:
    numbers=list(range(1,10))
    numbers=rr.sample(numbers, 3) 

    n1 = numbers[0]
    n2 = numbers[1]
    n3 = numbers[2]

    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    a1,a2,a3 = input("숫자를 입력>>").split(" ")

    a1 = int(a1)
    a2 = int(a2)
    a3 = int(a3)

    print(n1,n2,n3)


    if (n1==a1 or n1==a2 or n1==a3) and (n2==a1 or n2==a2 or n2==a3)  and (n3==a1 or n3==a2 or n3==a3) :
        print("상금 1억")
        continue

    elif (n1==a1 or n1==a2 or n1==a3) and (n2==a1 or n2==a2 or n2==a3):
        print("1천만원")
    elif (n2==a1 or n2==a2 or n2==a3) and (n3==a1 or n3==a2 or n3==a3):
        print("1천만원")
    elif (n1==a1 or n1==a2 or n1==a3) and (n3==a1 or n3==a2 or n3==a3):
        print("1천만원")
        continue

    elif (n1==a1 or n1==a2 or n1==a3) or (n2==a1 or n2==a2 or n2==a3) or (n3==a1 or n3==a2 or n3==a3):
        print("1만원")

    else:
        print("다음기회에")

    if a1== 100 :
        break 