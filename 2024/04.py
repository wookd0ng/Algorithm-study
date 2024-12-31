def solution(numbers):

    for i in range(len(numbers)):
        numbers[i] = numbers[i]*2
        print(numbers)

# 내가 이해한건 solution 이라는 함수에 정수 배열 numbers라는 매개변수가 들어올 예정이고, 입력받은 numbers 배열을 split을 통해 받아주고
# answer에 저장할거야. 그 다음, for문을 통해 numbers[i]. 즉 0번째 배열의 값 부터 *2을 하고 그 값을 새롭게 numbers에 저장해서
# numbers를 출력할건데 뭐가 틀린거야?