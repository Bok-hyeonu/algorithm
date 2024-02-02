T = int(input()) # 테스트 케이스의 수
for tc in range(1, T + 1):
    # D : A, B간 거리, A : A의 속력, B : B의 속력, F : 파리의 속력
    D, A, B, F = map(int, input().split())
    # 파리의 이동 거리는 A와 B가 부딪힐 때까지 이동한 거리
    # (거리) = (속력) * (시간)
    # (속력) = F
    # (시간) = A와 B가 부딪히는 시간
    #        = (A, B간 거리) / (A, B 속력 합)
    d_f = (D / (A + B))*F
    print(f'#{tc}', d_f)