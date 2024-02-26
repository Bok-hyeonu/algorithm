# 정렬 안 된 배열에서 하나씩 뽑아 정렬 완료된 배열에서의 자리를 찾아가는
# 삽입정렬 과정. heights : 정렬 미완료 배열, result : 정렬 완료 배열
import sys

P = int(sys.stdin.readline())
for i in range(P):
    tc, *heights = map(int, sys.stdin.readline().split()) # 20명
    result = [heights[0]]           # 키 순으로 학생을 세우며, 첫 번째 학생은 그냥 세웁니다.
    cnt = 0                         # 이동횟수
    # 2번째부터 20번째 학생들에 대해 
    for j in range(1, 20):
        # 키 순서로 선 학생들의 후방에서부터 키를 비교합니다.
        for k in range(j-1, -1, -1):
            # 제대로 선 학생의 키가 줄 세울 학생의 키보다 작으면
            if result[k] < heights[j]:
                # 줄 세우고자 하는 학생의 자리를 찾았습니다.
                result.insert(k+1, heights[j])
                break # 이 학생에 대해 줄을 세웠으므로 다음 학생을 줄 세웁니다. 
            else: # 제대로 선 학생이 크면
                # 그 앞에선 학생과 비교해야 하며, 제대로 선 학생은 한 칸 뒤로 갑니다.
                cnt += 1
        # 모든 학생보다 키가 작은 경우에는
        else:
            # 가장 앞에 서게 됩니다.
            result.insert(0, heights[j])
    
    print(tc, cnt)