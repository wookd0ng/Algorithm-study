
# 총 N/2마리의 폰켓몬만 가져가도 좋음
# 항상 짝수로 주어짐(총 폰켓몬의 개수)
# 번호로 종류 구분. 최대한 많은 종류를 원함
# 가질 수 있는 종류의 최댓값
# 폰켓몬의 종류번호가 담긴 배열 nums를 매개변수로 받았을 때, N/2 마리의 폰켓몬을 선택하는 방법
# 가장 많은 종류의 폰켓몬을 선택하는 방법
# 그때의 폰켓몬 종류 번호의 개수를 return 하는 solution 함수.
# def solution(nums):
#     answer = 0
#     for i in range(len(nums)):
#
#     return answer

def solution(nums):
    unique_nums = set(nums) # set으로 중복을 제거해서 고유종류수만 남김
    max_nums=len(nums)//2 # 총개수//2해서 가져갈 수 있는 개수가 확보
    return min(len(unique_nums),max_nums) # 둘 중의 최솟값을 골라서 출력(안전장치)

