def solution(participant, completion):
    participant.sort() # 두 목록 정렬
    completion.sort()
    for part, comp in zip(participant, completion): # 순서대로 비교하며
        if part != comp: # 해당 참가자가 완주 실패한 경우
            return part # 해당 참가자 반환
    else: # 모든 완주자에 대해 확인한 경우
        return participant[-1]  # 마지막 참가자가 완주 실패