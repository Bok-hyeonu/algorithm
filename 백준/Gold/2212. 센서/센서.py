# 1. 각 센서들을 K개 조로 묶는 문제입니다. 
# 2. 집중국의 수신가능영역의 거리 합이 최소가 되게 묶는 문제입니다.
# 3. 즉, 각 센서 간의 거리 차를 구한 다음, K - 1개 만큼의 거리 차를 제거해 준 후
# 4. 그 합을 구하면 됩니다.
# 5. 센서와 집중국 간 거리 합이 아닌 수신 가능 영역의 거리 합이므로 센서의 중복은 고려 X
# 6. set을 이용해 중복을 제거한 후 분석을 진행
N = int(input()) # 센서의 수
K = int(input()) # 집중국의 수
sensors = list(map(int, input().split()))   # 센서들의 위치
sensors = list(set(sensors))                # 수신 가능 영역의 거리합이므로 중복되는 위치의 센서는 고려 X
sensors.sort(reverse=True)                  # 위치를 정렬

# 센서의 위치가 하나이거나, 집중국의 수가 센서의 위치들의 수 이상인 경우
if len(sensors) == 1 or len(sensors) <= K:
    print(0)    # 해당 위치에 설치하면 되므로 거리합은 0
else:
    diff = [0]*(len(sensors)-1) # 거리 차 배열
    for i in range(1, len(sensors)):
        diff[i-1] = sensors[i-1]-sensors[i]
    diff.sort()                 # 거리 차 정렬
    print(sum(diff[:(len(sensors)-1-(K-1))])) # 거리차가 큰 K - 1개의 거리 차를 제외한 합 출력