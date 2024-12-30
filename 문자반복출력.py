#     문자열에서 한글자씩 가져와야함. 그 다음 n만큼 한글자 * 3 해야함
#   근데 정수가 아니라 문자열이라 char으로 해야함

def solution(my_string, n):
    res = []
    for char in my_string:
        res.append(char*n)
    return ''.join(res)

# 결국에 문자열을 받아서 한글자씩 *n하고 리스트에 넣어둔 뒤, 그 리스트를 또 문자열로 바꿔주는 작업