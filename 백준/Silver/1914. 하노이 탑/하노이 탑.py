import sys
memo = dict() # 연산 결과를 저장할 딕셔너리

def hanoi(bot, now, sub, tar):
    # tar가 결정되는 경우 sub는 자동으로 결정되므로 key값에 포함될 필요는 없습니다.
    key = (bot, now, tar)
    # 저장된 동일한 연산결과가 있는 경우 해당 결과 반환
    if key in memo:
        return memo[key]
    # 1번 원판은 현재 장대에서 목표 장대로 옮기기만 하면 됨
    if bot == 1:
        return f"{now} {tar}"
    else:
        # 위의 로직과 같은 과정입니다.
        output = "\n".join([hanoi(bot-1, now, tar, sub), 
                            f"{now} {tar}", 
                            hanoi(bot-1, sub, now, tar)])
        memo[key] = output
        return output

N = int(sys.stdin.readline())    
sys.stdout.write(f"{(1<<N) - 1}\n")
if N <= 20:
    sys.stdout.write(f'{hanoi(N, 1, 2, 3)}')