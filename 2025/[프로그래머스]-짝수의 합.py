'''
정수 n이 주어질때, n 이하의 짝수를 모두 더한 값을 return 하도록
'''

def solution(n):
    answer=0
    for i in range(0,n+1): # n값만큼 반복
        if i % 2 ==0: # i가 짝수란 의미
            answer+=i
    return answer
