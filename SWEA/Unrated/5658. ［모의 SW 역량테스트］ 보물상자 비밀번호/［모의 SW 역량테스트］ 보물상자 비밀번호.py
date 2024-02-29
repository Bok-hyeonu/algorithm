T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) # N은 4의 배수, K 몇 번째로 큰 수인지
    hexs = list(input()) # 수열
    nums = set() # 중복 제거를 위해 집합 생성

    for i in range(N//4): # 4로 나눈 몫만큼
        for j in range(4): # 4분할한 수열
            # 숫자로 바꿔 집합에 추가
            nums.add(int('0x'+''.join(hexs[j*N // 4:j*N//4 + N // 4]), 16))
        t = hexs.pop(0) # 하나씩 회전
        hexs.append(t) # 회전
    nums = list(nums) # 정렬을 위해 리스트화
    nums.sort() # 정렬
    print(f'#{tc}', nums[-K]) # 오름차순이므로 뒤에서 K번째 값이 원하는 결과