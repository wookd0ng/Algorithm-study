'''
그냥 거스름돈 문제임 ㄹㅇㅋㅋ
장군개미 5
병정개미 3
일개미 1

매개변수는 사냥감의 체력

만약 23이라고 예를 들면
23 % 5하고 그러면 나머지 3
3 % 3하면 나머지 0

나머지 먼저 확인하고 몫을 계산해서 마리수 계산해야되는데 더 효율적으로 구하는 거 없나?
어차피 총 마리수만 계산하면 되서 어느 개미가 몇 마리 필요한지는 필요 없는 듯

그러면 그냥 차례대로 몫먼저 계산하고 몫 res 값에 넣고 나머지는 계산해서 그 아래 계급 개미들에게 보내주는 형태로 하면 될듯
'''

def solution(hp):
    res=0

    if hp >=5:
        res += hp // 5
        hp%=5
    if hp >=3:
        res += hp //3
        hp%=3
    if hp>=1:
        res+=hp//1
    return res

'''
%=의 재발견
'''