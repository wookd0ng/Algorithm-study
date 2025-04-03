'''
일단 시벌탱
입력받은 정수배열 emergency를 내림차순으로 정렬하고
그 안에서 순서 매겨서 리턴해야 할듯
'''

def solution(emergency):
    sorted_em=sorted(emergency, reverse=True)
    answer=[]
    for e in emergency:
        answer.append(sorted_em.index(e) +1 )
    return answer


'''그러니까 내림차순 정렬된걸 새로운 배열에 넣을때
answer.append(sorted_em.index(e) + 1)
이렇게 sorted_em.index(e) 하면
내림차순으로 정렬된 리스트에서 e가 몇번째에 있는지 알려줌

이해했음
-> sorted_em.index(e)
-> 이게 내림차순으로 정렬된 곳에서 원래의 emergency의 값은 몇번째 순서인지를 보는거임
'''


