N = int(input()) # 소인수분해할 수
insu = 2 # 인수가 될 수(가장 작은 2부터 시작)
while N>1: # N이 1보다 큰 동안
    if N%insu==0: # N이 insu를 가지면
        print(insu) # insu 출력
        N //= insu # insu로 나눠 줌
    else: # insu를 가지지 않으면
        insu += 1 # 다음 insu 탐색