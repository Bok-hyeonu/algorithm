T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    a1,b1=a,b
    while a%b!=0: # 최대공약수 알고리즘
        a,b=b,a%b # 나머지로 나눔
    print(a1*b1//b)