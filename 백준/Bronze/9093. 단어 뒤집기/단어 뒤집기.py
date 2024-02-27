import sys

T = int(sys.stdin.readline()) # 테스트 케이스(문장의 수)
for _ in range(T):
    sent = list(sys.stdin.readline().split())
    result = [se[::-1] for se in sent] # 뒤집어서 저장
    print(*result) 