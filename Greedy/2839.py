# 3과 5가 있는데 이 둘을 조합해서 주문에 따라 최소한의 봉지
# 최소공배수?
# 만약 18이라고 하면

import math
def answer(N):
 count = 0
 while N >=0:
     if N % 5 ==0: #N을 5로 나누었을때 나머지가 0일 경우
         count += N//5
         return count # 여기까지가 5로 나눠질 경우 나눈 횟수 리턴 해주는 거
     N-=3
     count +=1
 return -1

