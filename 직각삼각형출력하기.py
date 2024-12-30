 # 높이와 너비 값으로 사용되는 n 값 받기
# n이 3이면 첫번째줄에 한개 두번째 줄에 한개 세번째 줄에 세개
# print('*')
# for i in range(n)
# 만약에 n값으로 6이 들어와도 결국엔 첫번째엔 1개를 출력해야되는데
# printf('*',i)
# i+=1

n=int(input())
i=0
while i<=n:
   print('*'*i)
   i+=1