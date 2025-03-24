def solution(numbers, target):
    def dfs(index, current_sum):
        # 종료 조건: 배열 끝까지 탐색했을 때
        if index == len(numbers):
            # 현재 합이 target과 같으면 경우의 수를 1 증가
            return 1 if current_sum == target else 0

        # 현재 숫자를 더하거나 빼는 두 가지 경우를 탐색
        return dfs(index + 1, current_sum + numbers[index]) + \
            dfs(index + 1, current_sum - numbers[index])

    # DFS 탐색 시작
    return dfs(0, 0)