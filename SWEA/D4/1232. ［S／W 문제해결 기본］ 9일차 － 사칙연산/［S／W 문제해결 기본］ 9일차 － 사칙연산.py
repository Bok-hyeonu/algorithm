def postorder(p):
    if 0 < p < N:
        postorder(tree[p][0])   # 왼쪽 자식
        postorder(tree[p][1])   # 오른쪽 자식
        # 왼쪽 자식과 오른쪽 자식을 사칙연산하여 저장
        if tree[p][2] == '+':
            tree[p][2] = tree[tree[p][0]][2] + tree[tree[p][1]][2]
        elif tree[p][2] == '-':
            tree[p][2] = tree[tree[p][0]][2] - tree[tree[p][1]][2]
        elif tree[p][2] == '*':
            tree[p][2] = tree[tree[p][0]][2] * tree[tree[p][1]][2]
        elif tree[p][2] == '/':
            tree[p][2] = tree[tree[p][0]][2] / tree[tree[p][1]][2]


for tc in range(1, 11):
    N = int(input())                        # 노드의 수
    tree = [[0] * 3 for _ in range(N + 1)]  # 왼쪽, 오른쪽, 내 값

    for i in range(N):                      # 트리 정보 입력
        arr = input().split()               # 노드 번호, 값, 왼쪽 자식, 오른쪽 자식
        if arr[1].isdigit():                # 내 값이 숫자면(리프 노드이면)
            tree[int(arr[0])][2] = int(arr[1]) # 값을 정수 형태로 저장
        else:                               # 숫자가 아니면(연산자이면)
            tree[int(arr[0])][2] = arr[1]   # 연산자 저장
            tree[int(arr[0])][0] = int(arr[2])  # 왼쪽 자식 저장
            tree[int(arr[0])][1] = int(arr[3])  # 오른쪽 자식 저장

    postorder(1)                        # 루트는 무조건 1이므로
    print(f'#{tc}', int(tree[1][2]))    # 정수 자료형으로 출력