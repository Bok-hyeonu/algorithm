def solution(array, commands):
    answer = []
    for com in commands: # 매 지시에 대해
        arr = array[com[0]-1:com[1]] # 원하는 배열을 자르고
        arr.sort() # 정렬
        answer.append(arr[com[2]-1]) # 원하는 순서의 값을 리스트에 append
    return answer # 반환