# 정수 배열 numbers가 매개변수로 주어지고
# numbers의 원소의 평균값을 return하게

def solution(numbers):
    hap=0
    for i in range(len(numbers)):
        hap+=numbers[i]
    avg = hap/len(numbers)
    if avg % 1 ==0:
        return avg
    elif avg % 1 ==0.5:
        return avg
    else:
        return int(avg)