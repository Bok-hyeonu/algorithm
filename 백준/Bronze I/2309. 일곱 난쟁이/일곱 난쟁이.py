hei_list= [int(input()) for _ in range(9)]

for i in range(1, 1<<9): # 공집합을 제외하고 부분집합 순회
    tot = 0 # 합
    leng = 0 # 길이
    result = [] # 부분집합 리스트
    for j in range(9):
        if i & (1<<j): 
            tot += hei_list[j]
            leng += 1
            result += [hei_list[j]]
            if leng == 7 and tot == 100: # 부분집합 길이가 7이고 합이 100일 때
                break # 종료
    if leng == 7 and tot == 100:
        break
result.sort() # 키 순 정렬
for k in range(7): # 출력
    print(result[k])