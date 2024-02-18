M = int(input()) # 시작
N = int(input()) # 종료
st = int(M**0.5) # 탐색 시작 자연수
ed = int(N**0.5) # 탐색 종료 자연수
result = [] # 결과 저장을 위한 리스트
for num in range(st, ed+2):
    if M<=num**2<=N:
        result.append(num**2)
if len(result) == 0:
    print(-1)
else:
    print(sum(result)) # 합
    print(result[0]) # 최소값