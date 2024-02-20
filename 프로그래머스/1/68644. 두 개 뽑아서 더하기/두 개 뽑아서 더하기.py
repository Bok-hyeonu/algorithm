def solution(numbers):
    answer = set()                              # 수가 담길 리스트
    for i in range(len(numbers)):               # 모든 조합에 대해 수행
        for j in range(i+1, len(numbers)):      
            answer.add(numbers[i] + numbers[j]) # 두 수의 합으로 만들어진 값을 추가
    answer = list(answer)                       # 정렬을 위해 리스트로
    answer.sort()                               # 정렬
    return answer