T = int(input())

for _ in range(T):
    s, p = map(str, input().split())

    cnt = 0
    # s내에 word가 포함되어 있다면, 횟수 증가
    cnt = s.count(p)

    # word에 해당하는 단어 삭제
    replaced_s = s.replace(p, "")
    print(cnt + len(replaced_s))
