def solution(edges):
    answer = []
     
    # 각 노드의 진입차수를 저장하는 딕셔너리
    dict_in = {}
     
    # 각 노드의 진출차수를 저장하는 딕셔너리
    dict_out = {}
     
    # 각 에지의 진입차수와 진출차수를 카운트하여 딕셔너리에 저장
    for e in edges:
        try:
            dict_in[e[0]] += 1
        except KeyError:
            dict_in[e[0]] = 1
        try:
            dict_out[e[1]] += 1
        except KeyError:
            dict_out[e[1]] = 1
     
    total = 0  # 에지 총 개수
    e_cnt = 0  # 8자 도넛 개수
    stick = 0  # 스틱 노드 개수
     
    # 각 노드의 진입차수를 확인하여 이중 연결 에지와 스틱 노드 개수를 세는 과정
    for k, v in dict_in.items():
        if v >= 2 and dict_out.get(k) is None:
            answer.append(k)
            total = v
        if v >= 2 and dict_out.get(k, 0) >= 2:
            e_cnt += 1
     
    # 스틱 노드 개수 계산
    for k, v in dict_out.items():
        if dict_in.get(k) is None:
            stick += 1
     
    # 답안 리스트에 도넛 개수, 스틱 노드 개수, 8자 도넛 개수 추가
    answer.append(total - (stick + e_cnt))
    answer.append(stick)
    answer.append(e_cnt)
    return answer