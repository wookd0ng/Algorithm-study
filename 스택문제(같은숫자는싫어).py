# arr 주어짐
# 중복 제거.
# 중복 제거 후 원소들의 순서 유지해야 함

# def solution(arr):
#     return set(arr) # 중복제거 아까랑 같은 문제인줄 알고 문제 끝까지 안읽고 씀 ㅋㅋ
# 연속으로 나오는 같은 숫자만 중복제거하는건데 이거는 그냥 모든 범위에 있는 중복된 숫자 제거임
# 그리고 set은 순서 보장 안함.

def solution(arr):
    box=None
    result=[]
    for num in arr:
        if num !=box:
            result.append(num)
            box=num
    return  result

# def solution(arr):
#     stack = []
#     for num in arr:
#         if not stack or stack[-1] != num:
#             stack.append(num)
#     return stack