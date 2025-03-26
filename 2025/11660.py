import sys
input = sys.stdin.readline

n,m=map(int,input().split())

# 원본 리스트 저장 (1차원 배열)
A=[[0]*(n+1)]
# 합 배열 저장 (2차원 배열)
D= [[0]*(n+1) for _ in range(n+1)]

# 원본 배열 받기
for i in range(n):import sys
input = sys.stdin.readline

n,m=map(int,input().split())

# 원본 리스트 저장 (1차원 배열)
A=[[0]*(n+1)]
# 합 배열 저장 (2차원 배열)
D= [[0]*(n+1) for _ in range(n+1)]

# 원본 배열 받기
for i in range(n): # 리스트 크기 만큼 n만큼 반복을 할 예정
    '''
    이렇게 하면 input.split() 한거를 x에 담음. 근데 x는 앞에서 int(x)로 선언해놔서 int형으로 바뀌고 이 식을 감싸고 있던 []로 인해서 리스트 형식으로됨
    그 다음 앞에 [0]을 더해서 [0,1,2,3,,,]이런 형식으로 1번 인덱스부터 사용하기 위해서 이렇게 함
    '''
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 합 배열 만들기
for i in range(1,n+1): # 1부터 n+1까지 반복
    for j in range(1,n+1): # 1부터 n+1까지 반복
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 마지막 질의에 대한 결과 출력
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2[y1-1]+D[x1-1][y1-1]]

print(result)