import sys
N = int(sys.stdin.readline())   # 연산의 수
heap = [0]*(N+1)                # 몫 연산 활용을 위해 0번 인덱스는 사용하지 않음
end = 0
for _ in range(N):
    x = int(sys.stdin.readline())   # 0인 경우 삭제, 이외의 자연수인 경우 삽입 연산
    
    if x == 0:                      # 삭제 연산
        if end == 0:                # 힙이 비어 있는 경우 0 반환
            sys.stdout.write('0\n')
        else:                       # 힙에 원소가 있는 경우
            sys.stdout.write(f'{heap[1]}\n') # 루트 노드 제거
                                    # 가장 마지막 노드를 루트 노드로
            heap[1] = heap[end]
            end -= 1 
            par = 1                 # 부모 노드
            while par*2 <= end:     # 자식 노드가 없을 때까지
                chi = par*2         # 기본 비교 대상은 왼쪽 자식  
                # 단, 자식이 둘이고 오른쪽 자식이 더 큰 경우             
                if par*2 != end and heap[par*2] > heap[par*2+1]:  
                    chi += 1 # 오른쪽 자식과 비교
                # 부모 - 자식 비교
                # (부모가 더 큰 경우 부모 - 자식 변경) 후 다음 검색 대상으로
                if heap[par] > heap[chi]: 
                    heap[par], heap[chi] = heap[chi], heap[par] 
                    par = chi        
                # 아니면 반복 종료
                else: break 

    else: # 삽입 연산
        end += 1
        heap[end] = x # 힙을 확장하여 마지막 노드에 삽입
        chi = end # 자식 인덱스
        while chi > 1: # 루트 노드에 도달할 때까지
            if heap[chi] < heap[chi//2] : # 자식 노드가 부모 노드보다 더 큰 경우
                heap[chi], heap[chi//2] = heap[chi//2], heap[chi] # 두 값 변경
                chi //= 2
            else: # 부모가 더 크다면
                break # 그 자리가 자식 노드의 자리