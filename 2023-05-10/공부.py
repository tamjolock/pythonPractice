# 기말 평가
# 1.데이터의 갯수입력
# 2.리스트의 저장
# 3.오름차순으로 리스트 정렬
# 4.출력

#리스트 넣기
# rlist = list(map(int,input("값").split()))

llist = []
count = int(input("갯수>>>"))

# 리스트에 값 집어넣기
for i in range(count):
    PO =int(input("값>>>"))    
    llist.append(PO)

# 리스트  오름차순
for j in range(len(llist)):
    k = len(llist) - j
    for i in range(1, k):
        if llist[i-1] >= llist[i]:
            temp = llist[i-1]
            llist[i-1] = llist[i]
            llist[i] = temp

print(llist)








