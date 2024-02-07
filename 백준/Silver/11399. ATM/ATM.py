N = int(input()) # 사람의 수
waiting = list(map(int, input().split())) # 소요시간
waiting.sort() # 정렬
wait = 0 # 각 사람의 작업 마무리까지의 시간
result = 0 # 대기 시간 합
for time in waiting: # 각 사람마다
    # 앞 사람의 마무리 시간이 본인의 대기시간
    wait += time # 그 시간에 본인의 소요시간을 더함
    result += wait # 그 소요시간을 총합에 더함

print(result) # 출력