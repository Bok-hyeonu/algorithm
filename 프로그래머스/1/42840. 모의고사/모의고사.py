# 각 수포자들은 일정한 주기로 값을 반복한다.
# i번째 답이 각 수포자의 i번째 답과 일치하면 해당 수포자가 맞춘 개수를 증가시킨다.
# 수포자가 맞춘 개수가 전체의 최댓값이면 해당 수포자를 반환 리스트에 추가한다.

def solution(answers):
    answer = []
    fir = sec = thr = 0 # 수포자가 맞춘 개수
    firs = list(range(1, 6)) # 1번 수포자 패턴
    secs = [2,1,2,3,2,4,2,5] # 2번 수포자의 패턴
    thrs = [3,3,1,1,2,2,4,4,5,5] # 3번 수포자의 패턴
    for i in range(len(answers)): # 정답들을 순회하며
        if answers[i] == firs[i%5]: # 1번 수포자와 같은지 확인
            fir += 1
        if answers[i] == secs[i%8]: # 2번과
            sec += 1
        if answers[i] == thrs[i%10]: # 3번과
            thr += 1
            
    max_v = max(fir, sec, thr) # 맞춘 최대 개수
    # 각 수포자의 최대 개수 여부 탐색하여 최대이면 append
    if max_v == fir: 
        answer.append(1)
    if max_v == sec:
        answer.append(2)
    if max_v == thr:
        answer.append(3)
            
    return answer
