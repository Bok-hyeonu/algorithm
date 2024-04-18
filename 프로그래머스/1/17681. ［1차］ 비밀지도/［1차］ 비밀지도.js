function solution(n, arr1, arr2) {
        // binary : 십진수를 이진수로 변환하는 함수
        binary = (digit) => {
          let bin = [];
          for (i = 0; i < n; i++) {
            // 나머지
            div = digit % 2;
            // 몫
            digit = Math.floor(digit / 2);
            bin.unshift(div);
          }
          return bin;
        };

        // makeMap : arr1, arr2를 각각 이진수로 변환하고,
        // 두 수 중 하나라도 벽이면 벽으로 써서 총 배열을 정답 배열로 반환
        makeMap = () => {
          const bin1 = arr1.map((arr) => binary(arr));
          const bin2 = arr2.map((arr) => binary(arr));
          let answer = [];
          // 이중반복문 사용
          for (i = 0; i < n; i++) {
            let sharps = "";
            for (j = 0; j < n; j++) {
              if (bin1[i][j] == 1 || bin2[i][j] == 1) {
                sharps += "#";
              } else {
                sharps += " ";
              }
            }
            answer.push(sharps);
          }
          return answer;
        };

        return makeMap();
      }