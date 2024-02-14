def solution(answers):
    answer = []
    fir = sec = thr = 0
    firs = list(range(1, 6))
    secs = [2,1,2,3,2,4,2,5]
    thrs = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == firs[i%5]:
            fir += 1
        if answers[i] == secs[i%8]:
            sec += 1
        if answers[i] == thrs[i%10]:
            thr += 1
            
    max_v = max(fir, sec, thr)
    if max_v == fir:
        answer.append(1)
    if max_v == sec:
        answer.append(2)
    if max_v == thr:
        answer.append(3)
            
    return answer