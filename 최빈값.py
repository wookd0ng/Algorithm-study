import statistics
from collections import Counter
def solution(array):
    try:
        mode=statistics.mode(array)
        counter=Counter(array)
        if list(counter.values()).count(counter[mode])>1:
            return -1
        return mode
    except statistics.StatisticsError:
        return -1
