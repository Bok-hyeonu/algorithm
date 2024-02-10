a,b=map(int,input().split())
a1,b1=a,b # 기존 값 저장
while a%b!=0: # 최대공약수 알고리즘
    a,b=b,a%b # 나머지로 나눔
    
print(a1*b1//b)