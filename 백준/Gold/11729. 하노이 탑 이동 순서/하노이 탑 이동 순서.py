import sys
# 현재 장대(now)에 있는 원판을 목표 장대(tar)로 옮기기 위해서는
# 가장 아래에 있는 원판(bot)을 목표 장대로 옮겨야 합니다.
# 그러기 위해서는 가장 아래에 있는 원판보다 하나 위에 있는 원판을 
# 목표 장대가 아닌 다른 장대(sub)로 옮긴 후, 가장 아래에 있는 원판을 목표 장대로
# 옮깁니다. 그리고 다른 장대에 옮겨뒀던 원판을 목표 장대로 옮기면 됩니다.
def hanoi(bot, now, sub, tar):
    if bot > 0:
        # 가장 아래 있는 원판보다 하나 위에 위치한 원판을 sub 장대로 옮긴다.
        hanoi(bot-1, now, tar, sub)
        # 가장 아래 있던 원판을 tar 장대로 옮긴다.
        sys.stdout.write(f'{now} {tar}\n')
        # sub 장대로 옮겨뒀던 가장 아래 원판보다 하나 위 원판을 tar 장대로 옮긴다.
        hanoi(bot-1, sub, now, tar)
    
N = int(sys.stdin.readline())
K = (1 << N) - 1        # 이동 횟수는 2의 N승 - 1
sys.stdout.write(f'{K}\n')
hanoi(N, 1, 2, 3)