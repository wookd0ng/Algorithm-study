# 입력받는 매개변수는 도화지의 세로크기, 가로크기
# 결과 값으로 출력해야 할 것은 그림의 개수와, 가장 넓은 그림의 넓이
# 1로 연결된 게 한 그림이고, 대각선으로 연결된건 인정 못함
# 하나씩 검사해야 하고 가까운거부터 검사하니까 BFS로 해야 함 -> 큐
# 0과 1이 공백을 두고 주어짐
# 세로는 공백 없어서 상관없고 가로가 공백으로 주어지니까

"""
자료구조
그래프 전체 지도 int [][]
방문여부 bool[][]
queue(BFS)
"""
import sys
from collections import deque
input = sys.stdin.readline

s, g = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(s)]
chk = [[False] * g for _ in range(s)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    q = deque() # deque()는 기본 함수야? 이렇게 q=deque()를 하면 무슨일이 일어나는거야
    q.append((y, x)) # 초기의 y와 x의 값이 뭔지 어떻게 알고 추가해?
    chk[y][x] = True
    area = 1

    while q:
        ey, ex = q.popleft() #ex와 ey가 어딘줄 알고 탐색을 시작해
        for k in range(4):
            ny = ey + dy[k] #dy와 dx는 알겠는데 ey, ex는 뭐야
            nx = ex + dx[k]
            if 0 <= ny < s and 0 <= nx < g and not chk[ny][nx] and graph[ny][nx] == 1:
                chk[ny][nx] = True
                q.append((ny, nx))
                area += 1
    return area

cnt = 0
maxv = 0

for j in range(s):
    for i in range(g):
        if graph[j][i] == 1 and not chk[j][i]:
            area = bfs(j, i)
            cnt += 1
            maxv = max(maxv, area)

print(cnt)
print(maxv)