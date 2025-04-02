'''
일단 정수 배열을 받고
slice로 num1 부터 num2 까지 자르면 될거 같은데
정수 배열을 어떻게 받지
numbers=int(input().slice())
배열이니까 인덱싱을 해야되는데
'''


def solution(numbers, num1, num2):
    return numbers[num1:num2+1]