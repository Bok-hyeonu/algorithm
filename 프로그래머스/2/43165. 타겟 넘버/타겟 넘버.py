def solution(numbers, target):
    N = len(numbers)
    total = sum(numbers)

    answer = f(-1, N, 0, target, total, numbers)

    return answer

def f(i, N, s, t, r, arr):  # s : 현재까지의 합, t : 타겟, r : 잔여 합, arr : 배열

    i += 1
    if i == N and s == t:  # 끝까지의 합이 일치하는 경우
        return 1
    elif i == N and s != t:  # 불일치
        return 0
    elif s + r < t or s - r > t:  # 남은 원소 미고려
        return 0
    else:  # 추가 탐색이 필요한 경우
        return f(i, N, s + arr[i], t, r - arr[i], arr) + f(i, N, s - arr[i], t, r - arr[i], arr)