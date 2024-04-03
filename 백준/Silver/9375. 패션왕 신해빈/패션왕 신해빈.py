for tc in range(1,1+int(input())):
    n = int(input())

    # 종류 : 이름
    closet = {}

    # n 번
    for _ in range(n): 

        # 이름, 종류
        name, j = map(str, input().split())

        # 딕셔너리에 그 종류가 없다면 키 생성하고, 밸류는 리스트에.
        if j not in closet:
            closet[j] = [name]

        # 이미 그 종류가 있다면, 리스트에 추가
        else:
            closet[j].append(name)
    
    # 결과를 1로 잡고 곱해나감
    result = 1
    for key in closet:
        result *= (len(closet[key])+1)


    # 최종 결과는 마지막에 1을 뺀다 (아무것도 선택 안한 경우)
    print(result-1)