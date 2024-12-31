def solution(n):
    # 홀수만 출력하는거라서 n-2해서 짝수면
    if n%2==0:
        for i in range(1,n,2):
            print([i])

    else :
        for i in range(1,n+1,2):
            print([i])

# for i in range(시작점, 정지점, 간격)