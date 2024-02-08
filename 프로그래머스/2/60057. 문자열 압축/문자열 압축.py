def solution(s):
    result = len(s)  # 최종 문자열의 길이(최소 : 입력 문자열의 길이)

    for i in range(1, len(s) + 1):  # i : 압축단위

        result_s = ''  # i 압축 문자열
        search = s[:i]  # 검색하려는 문자열
        cnt = 1  # search에 해당하는 개수

        for j in range(1, len(s) // i + 1):  # 압축 단위 크기로 분할한 문자열에 대해

            if s[i * j:i * j + i] == search:  # j번째 문자열과 검색 문자열이 같으면
                cnt += 1  # 카운트 상승

            else:  # 다르면
                if cnt == 1:  # 이전 검색까지의 cnt가 1이면
                    result_s += search  # 문자열만 추가
                else:  # 1보다 크면
                    result_s += str(cnt) + search  # 해당하는 개수만큼 숫자도 추가
                cnt = 1  # cnt 초기화
                search = s[i * j:i * j + i]  # 검색 대상 문자열도 j번째 문자열로 초기화

        else:  # 정상적으로 탐색을 종료한 경우에도 최종 문자열까지의 압축 결과를 추가

            if cnt == 1:
                result_s += search
            else:
                result_s += str(cnt) + search

        if len(result_s) < result:  # 압축 문자열이 기존의 문자열 최소 길이보다 짧으면
            result = len(result_s)  # 문자열 최소 길이 변경
    return result