function solution(friends, gifts) {
  const gifted = {}; // 친구A : {A가 선물 준 B : B에 준 선물 개수}
  const gift_idx = {}; // 선물 인덱스(준 개수 - 받은 개수)
  // 딕셔너리 초기화
  // 친구들에 딕셔너리 부여
  for (const elem of friends) {
    gifted[elem] = {};
    gift_idx[elem] = 0;
  }

  for (const elem of gifts) {
    // t : 선물을 준 사람, f : 선물을 받은 사람
    const [t, f] = elem.split(" ");
    // 선물 준 적 있으면 + 1
    if (f in gifted[t]) {
      gifted[t][f] += 1;
    } else {
      // 선물 준 적 없으면 생성
      gifted[t][f] = 1;
    }
    // 준 사람 + 1, 받은 사람 - 1
    gift_idx[t] += 1;
    gift_idx[f] -= 1;
  }
  // 전체 인원 만큼 0 배열 생성
  const will_get = Array.from({ length: friends.length }, () => 0);
  //
  for (let i = 0; i < friends.length; i++) {
    const curr = friends[i]; // 친구 A
    for (let j = i + 1; j < friends.length; j++) {
      const another = friends[j]; // 친구 B
      // A가 B에게 준 개수
      const a = another in gifted[curr] ? gifted[curr][another] : 0;
      // B가 A에게 준 개수
      const b = curr in gifted[another] ? gifted[another][curr] : 0;
      if (a > b) {
        // A가 더 많이 주면 A가 받을 개수 + 1
        will_get[i] += 1;
      } else if (a < b) {
        // B가 더 많이 주면 B가 받을 개수 + 1
        will_get[j] += 1;
      } else {
        // 주고받은 개수가 같으면
        const ai = gift_idx[curr];
        const bi = gift_idx[another];
        // 선물 지수가 큰 사람 받을 개수 + 1
        if (ai > bi) {
          will_get[i] += 1;
        } else if (ai < bi) {
          will_get[j] += 1;
        }
      }
    }
  }
  // 최대 반환
  const answer = Math.max(...will_get);

  return answer;
}
