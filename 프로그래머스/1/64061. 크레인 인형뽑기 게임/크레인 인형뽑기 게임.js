function solution(board, moves) {
    const N = board.length;  // 보드의 크기
    const bucket = [0];      // 바구니 역할을 할 배열(비교 작업을 용이하게 하기 위해 빈 공간을 넣었습니다.)
    let answer = 0;          // 터뜨린 인형의 수
    
    for (let num of moves) {  // num 열에 해당하는 인형을 뽑는다.
        for (let i = 0; i < N; i++) {  // 해당 열의 상단부터 탐색
            if (board[i][num - 1] !== 0) {  // 인형이 있으면
                const pick = board[i][num - 1];  // 인형을 뽑고
                board[i][num - 1] = 0;           // 해당 위치 0으로 초기화
                
                if (pick === bucket[bucket.length - 1]) {  // 뽑은 것이 바구니의 가장 최근에 뽑은 것과 같다면
                    bucket.pop();  // 해당 인형을 터뜨림 
                    answer += 2;   // 터뜨린 인형 수 2 증가
                } else {            // 같지 않으면 
                    bucket.push(pick);  // 뽑은 인형을 바구니에 추가
                }
                break;  // 다음 줄로 이동
            }
        }
    }
    
    return answer;
}
