lan, need = map(int, input().split())
len_list = []
for _ in range(lan):
    len_list.append(int(input()))
    
min_len = 1
max_len = max(len_list)
now = (min_len + max_len) // 2
# 이진 탐색
while min_len <= max_len:
    cnt = 0
    for leng in len_list:
        cnt += leng // now
    if cnt >= need:
        min_len = now + 1
        now = (min_len+max_len) // 2
    else:
        max_len = now - 1
        now = (min_len + max_len) // 2
    
print(now)