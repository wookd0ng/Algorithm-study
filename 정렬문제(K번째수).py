

    # array =[1,5,2,6,3,7,4]
    # i=2, j=5, k=3
    # array에 2번째부터 5번째까지 자르면 5,2,6,3
    # 이걸 정렬하면 2,3,5,6
    # 여기서의 3번째 숫자는 5
    # for i in range(len(array)):
# def solution(array,commands):
#         result =[]
#         new_array=list(range(commands[0],commands[1]+1,1))
#         result=new_array[commands[2]]
#         return result

def solution(array,commands):
    result=[]
    # 이제 여기서 commands가 이중 리스트니까
    for command in commands:
        i,j,k=command # 분리
        sliced=sorted(array[i-1:j]) # 문제는 1 based라 -1함
        # 이제 i번재부터 j번째 까지 잘랐으니까 k에 있는 수 출력해야 함
        result.append(sliced[k-1])
    return result
