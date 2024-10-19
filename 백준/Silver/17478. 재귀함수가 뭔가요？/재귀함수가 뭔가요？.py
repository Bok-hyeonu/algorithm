# 17478. 재귀함수가 뭔가요?

ques = '\"재귀함수가 뭔가요?\"'
line1 = '\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
line2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
line3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"'
final = '\"재귀함수는 자기 자신을 호출하는 함수라네\"'
answer = '라고 답변하였지.'
indent = '____'

def recursion_func(depth):
    que = indent*depth + ques
    print(que)
    
    if depth != N:
        fir = indent*depth + line1
        sec = indent*depth + line2
        thi = indent*depth + line3
        print(fir)
        print(sec)  
        print(thi)
        recursion_func(depth + 1)
        
    else:
        fin = indent*depth + final
        print(fin)
        
    ans = indent*depth + answer
    print(ans)

N = int(input())

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recursion_func(0)