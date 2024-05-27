# 입력의 수
N = int(input())
# 첫 입력
result = list(input())
# N-1개의 입력
for i in range(N-1):
    # 각 입력과 비교하여
    compare = list(input())
    
    for j in range(len(result)):
        # 하나라도 다른 문자가 있다면 ?로 변경
        if result[j] != compare[j]:
            result[j] = '?'
            
print(''.join(result))