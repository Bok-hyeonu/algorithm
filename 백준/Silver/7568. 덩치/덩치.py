# 덩치. 7568. S5. 정렬
import sys
N = int(sys.stdin.readline()) # 정렬하고자 하는 사람의 수
sizes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 각 사람들의 덩치(몸무게, 키)
result = [0]*N                                      # 각 사람들의 덩치가 몇 등에 해당하는지
for i in range(N):                                  # 각 사람에 대해
    cnt = 0                                         # 본인보다 덩치가 큰 사람의 수
    for j in range(N):                              # 모든 사람을 찾아보며 체중과 신장이 모두 크면
        if sizes[j][0] > sizes[i][0] and sizes[j][1] > sizes[i][1]:     
            cnt += 1                                # 덩치 1 증가
    result[i] = cnt+1                               # 등수 기록
print(*result)