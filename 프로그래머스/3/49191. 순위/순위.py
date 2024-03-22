def solution(n, results):
    lost = [[0, []] for _ in range(n+1)]
    won = [[0, []] for _ in range(n+1)]
    # 경기결과 등록
    for result in results:
        won[result[0]][0] += 1
        won[result[0]][1].append(result[1])
        lost[result[1]][0] += 1
        lost[result[1]][1].append(result[0])
    
    decided = [0]*(n+1)
    for i in range(1, n+1):
        # 내가 이긴 놈 중 이미 이긴 놈 제외한 이긴 놈의 수
        decided[i] = won[i][0]
        for bab in won[i][1]:
            for babbab in won[bab][1]:
                if babbab not in won[i][1]:
                    decided[i] += 1
                    won[i][1].append(babbab)
        # 내가 진 놈 중 이미 진 놈 제외한 이긴 놈의 수
        decided[i] += lost[i][0]
        for god in lost[i][1]:
            for godgod in lost[god][1]:
                if godgod not in lost[i][1]:
                    decided[i] += 1
                    lost[i][1].append(godgod)
    
    answer = decided.count(n-1)     # 결과 횟수가 n-1인 것의 수가 승부가 정해진 것의 수
    return answer