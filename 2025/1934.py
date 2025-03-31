
import sys
input=sys.stdin.readline

t=int(input())
# 유클리드 호제법
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# 최소공배수 =  a * b / 최대공약수

for i in range(t):
    a, b = map(int, input().split())
    result = a*b / gcd(a, b)
    print(int(result))