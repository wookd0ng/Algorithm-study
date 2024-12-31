
# 일단 가로 세로에 대한 최대값을 각각 찾고
# 찾았으면 세로의 순서에 있는 최대값 원소 순서에 가서 가로세로 바꿨을때 가로 크기에 세로가 들어가면 뒤집었을때 들어간다는거니까 취소

def solution(sizes):
    # 각 명함을 회전시켜 항상 큰 값을 가로로 설정 -> 이게 천재인듯
    sizes = [sorted(size, reverse=True) for size in sizes]

    # 최대 가로와 최대 세로 찾기
    max_width = max(size[0] for size in sizes)
    max_height = max(size[1] for size in sizes)

    # 지갑 크기 반환
    return max_width * max_height

