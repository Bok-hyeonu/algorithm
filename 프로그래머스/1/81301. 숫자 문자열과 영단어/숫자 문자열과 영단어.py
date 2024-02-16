
def solution(s):
    num_dict = {'zero': '0','one':'1', 'two':'2', 'three':'3', 'four':'4',
               'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    answer = ''
    while s:
        if s[0].isdigit():
            answer += s[0]
            s = s[1:]
        elif s[0]=='z':
            answer += '0'
            s = s[4:]
        elif s[0] == 'n':
            answer += '9'
            s = s[4:]    
        elif s[0] == 'e':
            answer += '8'
            s = s[5:]
        elif s[0] == 's':
            if s[1] == 'e':
                answer += '7'
                s = s[5:]
            else:
                answer += '6'
                s = s[3:]
        elif s[0] == 'f':
            answer += '5' if s[1] == 'i' else '4'
            s = s[4:]
        elif s[0] == 't':
            if s[1] == 'h':
                answer += '3'
                s = s[5:]
            else:
                answer += '2'
                s = s[3:]
        else:
            answer += '1'
            s = s[3:]
                
    return int(answer)