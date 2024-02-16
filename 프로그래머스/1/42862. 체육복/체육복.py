def solution(n, lost, reserve):
    
    res_lost = set(lost)&set(reserve)
    
    lost = sorted(list(filter(lambda x : x not in res_lost, lost)))
    reserve = sorted(list(filter(lambda x : x not in res_lost, reserve)))
    for ls in lost:
        # 앞 번호의 여벌옷의 경우에는 굳이 remove 사용할 필요 없음
        # lost의 다음 원소가 빌릴 수는 없기 때문
        if ls-1 in reserve:
            reserve.remove(ls-1)
        # 단 뒷 번호의 여벌 옷의 경우에는 remove를 사용해 주어야 함
        elif ls+1 in reserve:
            reserve.remove(ls+1) 
        
        else:
            n -= 1
    
    return n