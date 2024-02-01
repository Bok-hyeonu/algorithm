for test_case in range(1, 11):
 
    bui_num = int(input())
    building_list = list(map(int, input().split()))
    cnt = 0
    for i in range(2, bui_num-2):
        buildings = building_list[i-2:i+3]
        if max(buildings) == building_list[i]:
            cnt += building_list[i] - sorted(buildings)[-2]
 
    print(f'#{test_case} {cnt}')