# 1~50까지 출력 

""" for i in range(1,51):

    if i % 10 == 1:
        print(f"\n")

    if i<10:
        print(f"{i}",end=" ")

    else:
        print(f"{i}",end=" ")

print(f"\n")
 """
# 1~100 사이의 짝수 출력, (5의 배수 출력), 한줄에 데이터 10개씩 출력

# even = 0
# count = 0

# for i in range(1,101):

#     if i%2==0 or i%5==0:

#         print(i,end=" ")
#         count += 1

#     if count%10 == 0 :
#         print(f"{count}",end="\n")
   

#3,6,9 게임.

""" for i in range(1,101):
    if i%10 == 1:
        print("\n")
    if i in (3,6,9) or i%10 in(3,6,9) or i//10 in (3,6,9):
        print(f"음",end=" ")
    else:
        print(f"{i}",end=" ") """


# 컴퓨터와 가위바위보 게임
""" import random as rr
user = input("가위 바위 보 중 입력하세요>>").strip(" ")
data = ["가위","바위","보"]
com = rr.choice(data)

if user not in ("가위","바위","보"):
    print("잘못입력됨")
    exit()

print(f"컴퓨터:{com} , 사용자:{user}")

# whowin = ""

if com == user:
    print("비겼다")

elif com== "가위":
    if user == "바위":
        print("유저 : 승")
    else:
        print("컴퓨터 : 승")

elif com== "바위":
    if user == "보":
        print("유저 : 승")
    else:
        print("컴퓨터 : 승")

elif com== "보":
    if user == "가위":
        print("유저 : 승")
    else:
        print("컴퓨터 : 승") """



