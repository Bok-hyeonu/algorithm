N = int(input()) # 입력

if N < 100:
    print(N)
else:
    cnt = 99
    # 각 수 탐색
    for num in range(100, N + 1):
        nums = list(map(int, str(num)))
        diff = nums[1] - nums[0]    # 차이 지정
        isHansu = True              # 한수 여부 판단
        # 마지막 자릿수까지
        for i in range(2, len(nums)):
            # 차이가 같지 않으면(등차수열이 아니면)
            if nums[i] - nums[i - 1] != diff :
                isHansu = False
                break
        # 한수인 경우 개수 추가
        if isHansu:
            cnt += 1
    print(cnt)