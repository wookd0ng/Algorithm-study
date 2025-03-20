# P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2
# [2, 5, 1, 4, 3] 순서
#  1 2 3 3 4
#  2번째 사람은 1분
#  3번째 사람은 3분
#  4번째 사람은 6분
#  5번째 사람은 9분

def solution(N,P):
    P.sort()
    wait=0
    total=0
    for time in P: # 리스트 P의 값들을 하나씩 가져옴
        wait+=time# 소요되는 시간들을 모두 wait 변수에 더함
        total+=wait# 누적이 되어야 해서
    return total

