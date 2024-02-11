def solution(nums):
    N = len(nums) # 총 포켓몬의 수
    answer = 0
    bags = [] # 포켓몬을 담을 가방
    for num in nums: # 포켓몬을 순회하며
        if num not in bags: # 다른 종류라면
            answer += 1 # 담음
            bags.append(num) 
            # 담을 수 있는 최대 개수에 도달한 경우
            if answer == N/2: 
                break # 종료
    # 최대 개수에 도달하지 못한 경우, 어떤 방식으로 포켓몬을
    # 담더라도, 현재 개수가 포켓몬 종류의 최대 수이다.
                
    return answer