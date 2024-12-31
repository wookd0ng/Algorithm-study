# 일단 조각수와 사람의 명수를 입력받음
# 그래서 처음에 조각수 * 명수 하고, 판마다 자를수있는 조각의 최대개수 10으로 나누면 될거같은?
# def solution(slice, n):
#     pan = (slice * n) / 10
#     if abs((slice * n) % 10):
#         pan+=1
#     return pan
# 잘못 생각함
# 10명이 7조각으로 자른 피자를 몇판을 시켜야 최소 한 조각씩 먹을 수 있냐는 거였음
def solution(slice, n):
    return n//slice + (1 if n%slice else 0)