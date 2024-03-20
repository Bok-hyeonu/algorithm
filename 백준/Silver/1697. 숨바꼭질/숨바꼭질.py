from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    
    while queue:
        cur, c_time = queue.popleft()
        if cur > len(visited)-1 or cur < 0 or visited[cur] == 1:
            continue
        if cur == M:
            return c_time
        
        visited[cur] = 1
        queue.append((cur-1, c_time+1))
        queue.append((cur+1, c_time+1))
        queue.append((cur*2, c_time+1))
            
N, M = map(int, input().split())
visited = [0] * (max(N, M)*2+1)
print(bfs(N))