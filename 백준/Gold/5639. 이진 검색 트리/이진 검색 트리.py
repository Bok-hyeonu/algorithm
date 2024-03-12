import sys

# 이진 탐색 트리의 전위 순회는 루트 노드 방문 후 루트 노드를 기준으로 작은 값들
# (왼쪽 서브트리)을 먼저 방문하고 큰 값(오른쪽 서브트리)을 그 후에 방문한다.
# 즉, 전위순회 리스트로부터 루트 노드보다 커지는 순간이 왼쪽 서브트리와
# 오른쪽 서브트리의 기준점이다.
sys.setrecursionlimit(1000000) # 최대 재귀 제한 연장

def postorder(tree):
    # 트리에 원소가 남았을 경우에만
    if tree:
        root = tree[0] # 트리의 루트 노드
        # 루트 노드보다 커지는 순간을 탐색
        for i in range(1, len(tree)):
            # 오른쪽 서브트리를 찾았다면 그 점을 기준으로 좌 우 서브트리 분할
            if tree[i] > root:
                Lsub = tree[1:i]
                Rsub = tree[i:]
                break
        else:
            # 좌측 서브트리만 존재하는 경우
            Lsub = tree[1:]
            Rsub = []
        
        # 후위 순회는 왼쪽, 오른쪽 서브트리를 방문한 후 자신을 방문
        postorder(Lsub)
        postorder(Rsub)
        sys.stdout.write(f'{root}\n')

# 전위순회를 입력으로 받음
preord = []
while True:
    try:
        preord.append(int(sys.stdin.readline()))
    except:
        break

postorder(preord) # 후위 순회 함수 호출