def solution(num_list):
    answer = 0

    for i in range(len(num_list)):
        while True:
            if num_list[i]%2 == 0:
                num_list[i]=num_list[i]/2
                answer += 1
                continue
            elif num_list[i]%2==1:
                num_list[i] = num_list[i]-1
                continue
        
    return answer



a_list=[1,40,24,3]

print(solution(a_list))

print(solution)