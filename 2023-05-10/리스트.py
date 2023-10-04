import random as rr

nums = []

for i in range(10):
    nums.append(rr.randrange(100))

print(f"*****{nums}")

for i in range(len(nums)):
    if nums[i]>nums[i+1]:
        temp = nums[i]
        n1 = nums[i+1]
        n2 = temp

print(f"*****{nums}")

# 기말 평가
# 1.데이터의 갯수입력
# 2.리스트의 저장
# 3.오름차순으로 리스트 정렬
# 4.출력

# while True:
#     numdata = int(input("데이터 갯수입력>>"))
#     L1 = []

#     L1 = numdata
#     for i in range(len(L1)):
#         if 





