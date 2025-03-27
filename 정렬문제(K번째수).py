

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

# def solution(array,commands):
#     result=[]
#     # 이제 여기서 commands가 이중 리스트니까
#     for command in commands:
#         i,j,k=command # 분리
#         sliced=sorted(array[i-1:j]) # 문제는 1 based라 -1함
#         # 이제 i번재부터 j번째 까지 잘랐으니까 k에 있는 수 출력해야 함
#         result.append(sliced[k-1])
#     return result
#

def solution(array,commands):
    for command in commands:
        result=[]
        i,j,k=command #commands 배열의 원소 값을 command로 접근해서 분리 시킴
        sliced=sorted(array[i-1:j]) # i번째 부터 j번째까지 자른뒤 정렬
        result.append(sliced[k-1])
        '''
        배열 순서
        1,5,2,6,3,7,4
        1,2,3,4,5,6,7
        i=2 j=5 k=3
        2번째 부터 5번째 까지 자름
        5,2,6,3
        정렬하면 2,3,5,6
        이중에 3번째 숫자를 고르면 5
        '''