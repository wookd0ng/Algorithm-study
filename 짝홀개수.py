# def solution(num_list):
#     a=0
#     b=0
#     for i in range(num_list):
#         if num_list%2 == 0:
#             a+=1
#             return a
#         elif num_list%2 != 0:
#             b+=1
#             return b
#     answer=[a,b]
#     return answer

# 일단 range()이거는 정수를 요구해서 range가 아니라 애초에 num_list가 들어가야함

def solution(num_list):
    a=0
    b=0
    for i in num_list:
        if i%2==0:
            a+=1
        else:
            b+=1
    answer = [a,b]
    return answer