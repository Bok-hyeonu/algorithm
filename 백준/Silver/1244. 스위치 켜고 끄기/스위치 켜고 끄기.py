cnt = int(input()) # 스위치의 수
switch_list = list(map(int, input().split())) # 스위치의 상태
peo = int(input()) # 입력 사람의 수
while peo > 0: 
    sex, num = list(map(int, input().split())) # 성별과 스위치 번호
    if sex == 1: # 남자라면
        num2 = num 
        while num2 <= cnt: # 인덱스에 다다를 동안
            if switch_list[num2-1]==0: 
                switch_list[num2-1] = 1
            else:
                switch_list[num2-1] = 0
            num2 += num
    else:
        if switch_list[num-1] == 0:
            switch_list[num-1] = 1
        else:
            switch_list[num-1] = 0
        for i in range(1, num):
            if num-1-i == -1 or num+i > cnt or switch_list[num-1-i] != switch_list[num-1+i]:
                break
            else:
                if switch_list[num-1-i] == 1:
                    switch_list[num-1-i] = 0
                    switch_list[num-1+i] = 0
                else:
                    switch_list[num-1-i] = 1
                    switch_list[num-1+i] = 1
                
    peo -= 1

for j in range(cnt):
    print(switch_list[j], end=' ')
    if (j+1)%20 == 0:
        print()