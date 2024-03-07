import sys
memo = dict()

def hanoi(bot, now, sub, tar):
    key = (bot, now, sub, tar)
    if key in memo:
        return memo[key]
    if bot == 1:
        return f"{now} {tar}"
    else:
        output = "\n".join([hanoi(bot-1, now, tar, sub), f"{now} {tar}", 
                            hanoi(bot-1, sub, now, tar)])
        memo[key] = output
        return output

N = int(sys.stdin.readline())    
sys.stdout.write(f"{(1<<N) - 1}\n")
sys.stdout.write(f'{hanoi(N, 1, 2, 3)}')
