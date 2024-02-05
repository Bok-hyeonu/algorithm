for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if x2 > x1 and y2 > y1: # x1, y1좌표를 원점으로 했을 때 기준 1사분면
        if x2 < p1 and y2 < q1: 
            print('a')
        elif x2 == p1 and y2 == q1:
            print('c')
        elif (x2 == p1 and y2 < q1) or (y2 == q1 and x2 < p1):
            print('b')
        else:
            print('d')
    elif x2 < x1 and y2 > y1: # 2사분면
        if p2 > x1 and y2 < q1:
            print('a')
        elif p2 == x1 and y2 == q1:
            print('c')
        elif (p2==x1 and y2<q1) or (y2==q1 and x1 < p2):
            print('b')
        else:
            print('d')
    elif x2 < x1 and y2 < y1: # 3 사분면
        if p2 > x1 and q2 > y1:
            print('a')
        elif p2 == x1 and q2 == y1:
            print('c')
        elif (p2==x1 and q2 > y1) or (q2 == y1 and p2 > x1):
            print('b')
        else:
            print('d')
    elif x2 > x1 and y2 < y1: # 4사분면
        if x2 < p1 and q2 > y1:
            print('a')
        elif x2 == p1 and q2 == y1:
            print('c')
        elif (x2==p1 and q2 > y1) or (q2==y1 and x2 < p1):
            print('b')
        else:
            print('d')
    elif x2 == x1 and y1 < y2: # 1, 2사분면 사이 y축
        if y2 < q1:
            print('a')
        elif y2 == q1:
            print('b')
        else:
            print('d')
    elif x2 == x1 and y1 > y2: # 3, 4사분면 사이 y축
        if q2 > y1:
            print('a')
        elif q2 == y1:
            print('b')
        else:
            print('d')
    elif y1==y2 and x1 < x2: # 1, 4사분면 사이 x축
        if x2 < p1:
            print('a')
        elif x2 == p1:
            print('b')
        else:
            print('d')
    elif y1==y2 and x1 > x2: # 2, 3사분면 사이 x축
        if x1 < p2:
            print('a')
        elif x1 == p2:
            print('b')
        else:
            print('d')
    else: # 원점
        print('a')
