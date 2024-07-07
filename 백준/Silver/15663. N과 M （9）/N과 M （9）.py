# 15663. N과 M (9)

N, M = map(int, input().split())        # 수의 수, 수열의 길이
nums = sorted(list(map(int, input().split())))  # 숫자 배열

visited = [0]*N     # 사용 여부 배열
used = []           # 사용 배열

def dfs():
    if len(used) == M:
        print(*used)
        return
    # 중복 수열 방지
    rem = 0
    for i in range(N):
        # 방문하지 않았으면서 중복된 것이 아니면
        if not visited[i] and rem != nums[i]:
            visited[i] = 1          # 방문 표시
            used.append(nums[i])    # 현재 배열에 추가
            rem = nums[i]           # 중복 수열로 저장
            dfs()                   # 다음 호출
            visited[i] = 0          # 방문 초기화
            used.pop()              # 현재 배열에서 제거

dfs()