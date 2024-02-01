num = int(input())
rate = 18541 / 30000
most_list = []
most_num = 0
for j in range(-1,2):
    sec_num = round(num*rate) + j
    num_list = [num, sec_num]
    while num_list[-2] - num_list[-1] >= 0:
        num_list.append(num_list[-2]-num_list[-1])
    if len(num_list) > most_num:
        most_num = len(num_list)
        most_list = num_list

print(most_num)
for i in range(most_num):
    print(most_list[i], end=' ')