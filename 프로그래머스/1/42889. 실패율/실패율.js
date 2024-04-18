function solution(N, stages) {
    let cnt = stages.length; // 각 스테이지 도달자 수, 처음은 전체 이용자 수
    let answer = []; // 실패율과 스테이지 번호가 담길 배열
    
    for (let i = 1; i <= N; i++) { // 각 스테이지 번호에 대해        
        if (cnt !== 0) { // 도달한 사람이 있으면
            let stay = stages.filter(stage => stage === i).length; // 해당 스테이지 정체자 수
            answer.push([stay / cnt, i]); // 실패율과 스테이지 저장
            cnt -= stay; // 해당 스테이지 정체자수를 뺀 값이 다음 스테이지 도달자
        } else { // 도달한 사람이 없다면
            answer.push([0, i]); // 해당 스테이지 실패율은 0
        }
    }
    
    answer.sort((a, b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1]; // 실패율이 같으면 스테이지 번호 기준으로 오름차순 정렬
        }
        return b[0] - a[0]; // 실패율을 기준으로 내림차순 정렬
    });
    
    let final = answer.map(ans => ans[1]); // 스테이지 번호를 배열로 저장
    
    return final;
}