import sys

def preorder(t): # 전위
    # 0이 아니면 전위 순회 진행
    if t != 0:
        sys.stdout.write(f'{chr(t+64)}')
        preorder(cl[t])
        preorder(cr[t])

def inorder(t): # 중위
    if t != 0:
        inorder(cl[t])
        sys.stdout.write(f'{chr(t+64)}')
        inorder(cr[t])

def postorder(t): # 후위
    if t != 0:
        postorder(cl[t])
        postorder(cr[t])
        sys.stdout.write(f'{chr(t+64)}')

N = int(sys.stdin.readline())
cl = [0]*27 # 왼쪽 자식 노드
cr = [0]*27 # 오른쪽 자식 노드
# 왼쪽 자식과 오른쪽 자식에 저장
for _ in range(N):
    # 아스키 코드를 이용한 인덱스 형태로 변환
    p, c1, c2 = map(lambda x: ord(x) - 64, sys.stdin.readline().split())
    if c1 >= 0:
        cl[p] = c1
    if c2 >= 0:
        cr[p] = c2

preorder(1)
sys.stdout.write('\n')
inorder(1)
sys.stdout.write('\n')
postorder(1)
sys.stdout.write('\n')