def solution(age):
    result=''
    # 처음에 입력받은 숫자를 하나씩 문자로 바꿔야 하는데 숫자는 한칸씩 입력받기 힘드니까 문자로 변환
    for digit in str(age):
        # 만약에 23을 입력받았으면 2,3 이렇게 문자 취급하여 하나씩 받은걸 digit에 넣고 다시 int로 변환시킴
        # 그리고 ord를 통해서 초기값을 'a' 즉 97로 해놓음
        # 그래서 ord('a')+int(digit) 은 ord('a')+입력값임
        # 이렇게 되면 숫자+숫자 니까 마지막에 chr로 감싸서 return 해버림
        result+=chr(ord('a')+int(digit))
    return result