def solution(p, s): # 작업 진행 상황, 작업 속도
    top = 1 # 배포 가능 개수(최소 배포 개수 1)
    # 작업 진행일
    day = (100-p[0])//s[0] if (100-p[0])%s[0]==0 else (100-p[0])//s[0] + 1 
    answer = [] # 배포당 배포 수 리스트
    for i in range(1, len(p)): # 작업 순서대로
        if s[i]*day>=(100-p[i]): # 현재 시점에서 작업이 완료되어 배포 가능하다면
            top += 1 # 배포개수 증가
        else: # 불가능하다면
            answer.append(top) # 지금까지 완료된 것 배포
            top = 1 # 배포 초기화
            # 현재 작업에 필요한 작업일수만큼 진행
            if (100-p[i]-day*s[i]) % s[i]==0: 
                day += (100-p[i]-day*s[i]) // s[i]  
            else:
                day += (100-p[i]-day*s[i]) // s[i] + 1 
    answer.append(top) # 최종작업 완료 후 배포
    
    return answer # 배포당 배포 수 리스트 반환
