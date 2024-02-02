import sys
def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
N = int(sys.stdin.readline()) # 난이도의 수
if N == 0:
    print(0)
else:        
    lev_list = [] # 난이도 리스트
    for i in range(N): # 난이도 받음
        lev_list.append(int(sys.stdin.readline())) # 난이도 리스트에 하나씩 추가
    lev_list.sort() # 오름차순 정렬
    out = my_round(N*0.15) # 절사로 제거할 각 양 끝 값의 수
    print(my_round(sum(lev_list[out:N-out])/(N-out*2))) 
    # 양 끝 값을 제거한 후 평균을 구해 출력