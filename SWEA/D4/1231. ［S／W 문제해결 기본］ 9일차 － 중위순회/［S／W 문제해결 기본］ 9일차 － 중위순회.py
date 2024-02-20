def inorder(p):                     # 중위 순회
    if p <= N:                      # 마지막 노드까지
        inorder(p * 2)              # 왼쪽 자식 노드 순회
        print(T[p], end='')         # 현재 노드 작업 진행
        inorder(p * 2 + 1)          # 오른쪽 자식 노드 순회
 
 
for tc in range(1, 11):
    N = int(input())                    # 트리의 정점의 총 수
    T = [0] * (N + 1)                   # 완전 이진트리이므로 N개(편의상 N+1개)의 노드만 필요. 추가 삽입 과정이 없다는 가정
    for _ in range(N):                  # 트리에 저장.
        inputs = input().split()        # 완전 이진트리이므로 자식 노드를 지칭하는 정보는(3, 4번째 원소) 필요 없음
        T[int(inputs[0])] = inputs[1]   # 원소의 첫 번째값(노드 번호)을 인덱스로 하는 리스트(트리)에 두 번째 값을 저장
    print(f'#{tc}', end = ' ')
    inorder(1)                          # 순회 결과 출력
    print()                             # 개행을 반드시 해줘야 한다.