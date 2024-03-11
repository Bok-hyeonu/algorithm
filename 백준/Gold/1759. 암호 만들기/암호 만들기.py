# Logic 
# 1. 사전 순으로 증가하는 순서대로 출력해야 한다. -> 정렬된 배열에서 진행
# 2. 최소 하나 이상의 모음과 두 개 이상의 자음 -> 자음 수와 모음 수 카운팅
# 3. 연산 속도를 위해 아스키 코드로 알파벳을 숫자로 바꾼 후 작업을 진행하고
# 출력 과정에서만 바꿔줌
import sys

def f(i, jj, k):
    if i == k:
        cnt = 0 # 문자열에서 모음의 수
        for l in P:
            if l in (1, 5, 9, 15, 21): cnt += 1
        # 모음의 수가 1 이상이고 자음의 수가 2 이상일 때만 문자열 조건 충족
        if cnt != 0 and k-cnt >= 2:    
            sys.stdout.write(f"{''.join(map(lambda x:chr(x+96), P))}\n")
    else:
        # 오름차순 증가하는 문자열 생성
        for j in range(jj+1, C-L+i+1):
            P[i] = letters[j]
            f(i+1, j, k)

# L : 암호 문자열의 길이, C : 주어진 알파벳의 수
L, C = map(int, sys.stdin.readline().split()) 
# 알파벳들을 입력으로 받음.
# 편리한 연산을 위해 아스키 코드 값을 이용해 변환 후 정렬
letters = list(map(lambda x:ord(x)-96, sys.stdin.readline().split()))
letters.sort()
P = [0]*L   # 순열 역할을 할 리스트
f(0, -1, L)