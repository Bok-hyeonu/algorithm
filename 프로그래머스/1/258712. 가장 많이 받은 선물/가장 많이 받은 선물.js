function solution(friends, gifts) {
  let gifted = {}; // gifted = {"friend 이름": {"선물 준 친구 이름": 이 친구에게 준 선물 개수}}
  let gift_idx = {}; // 선물 지수
  // 딕셔너리 초기화
  for (const friend of friends) {
    gifted[friend] = {};
    gift_idx[friend] = 0;
  }

  for (const gift of gifts) {
    const temp = gift.split(" ");
    const t = temp[0]; // t: 선물을 준 사람, f: 받은 사람
    const f = temp[1]; // t: 선물을 준 사람, f: 받은 사람

    if (f in gifted[t]) {
      gifted[t][f] += 1;
    } else {
      gifted[t][f] = 1;
    }
    // 선물 지수 반영
    gift_idx[t] += 1;
    gift_idx[f] -= 1;
  }

  // 각자 받게 될 선물 개수
  let will_get = [];
  for (const _ in friends) {
    will_get.push(0);
  }
  // friends 리스트 순서대로 저장
  let len_friends = 0;
  for (const _ of friends) {
    len_friends += 1;
  }
  let a;
  let b;
  for (i = 0; i < len_friends; i++) {
    const curr = friends[i]; // 인덱스 i에 해당하는 친구
    for (j = i + 1; j < len_friends; j++) {
      const another = friends[j]; // 인덱스 j에 해당하는 친구
      // curr가 another에게 준 선물 개수
      if (another in gifted[curr]) {
        a = gifted[curr][another];
      } else {
        a = 0;
      }
      // another가 curr에게 준 선물 개수
      if (curr in gifted[another]) {
        b = gifted[another][curr];
      } else {
        b = 0;
      }

      if (a > b) {
        // curr가 선물을 더 많이 줬다면
        will_get[i] += 1;
      } else if (a < b) {
        // another가 선물을 더 많이 줬다면
        will_get[j] += 1;
      } else if (a === b) {
        // 둘이 선물을 주고 받은 개수가 같다면 선물 지수 확인
        const ai = gift_idx[curr];
        const bi = gift_idx[another];
        if (ai > bi) {
          will_get[i] += 1;
        } else if (ai < bi) {
          will_get[j] += 1;
        }
      }
    }
  }

  const answer = Math.max(...will_get);
  return answer;
}
