# 실패율 : 해당 스테이지 정체자 수 / 해당 스테이지 도달자 수
# count 메서드를 이용해 해당 스테이지 정체자 수를 해당 스테이지 도달자 수로 나눠준 실패율을 계산하여
# 실패율과 해당 스테이지 번호를 리스트에 추가한다.
# 실패율은 내림차순, 실패율이 같다면 스테이지 번호를 오름차순 정렬한 후
# 스테이지 번호만 새로운 리스트로 작성한다.
def solution(N, stages): 
    cnt = len(stages) # 각 스테이지 도달자 수 처음은 전체 이용자 수
    answer = [] # 실패율과 스테이지 번호가 담길 리스트
    
    for i in range(1, N+1): # 각 스테이지 번호에 대해        
        if cnt != 0: # 도달한 사람이 있으면
            stay = stages.count(i) # 해당 스테이지 정체자 
            answer.append([stay/cnt, i]) # 실패율과 스테이지 저장
            cnt -= stay # 해당 스테이지 정체자수를 뺀 값이 다음 스테이지 도달자
        else: # 도달한 사람이 없다면
            answer.append([0, i]) # 해당 스테이지 실패율은 0
        
    
    answer.sort(key = lambda x: (-x[0], x[1])) # 실패율을 정렬
    
    final = [ans[1] for ans in answer] # 스테이지 번호를 리스트로 저장
    
    return final