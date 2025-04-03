def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i ==0:
            answer+=1
    return answer

'''
두개의 숫자를 순서를 정하여 나타낸 쌍 (a,b)로 표기
n이 매개변수로 주어지면 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return

예를 들면 20이 n으로 주어지면 순서쌍은 1,20 / 2,10 / 4,5 이런식으로 해서 총 6개


'''