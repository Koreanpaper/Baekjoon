
#01
print('Hello world')

#02
A,B=input().split() #split()는 띄어쓰기 기준으로 구분 가능
A=int(A)
B=int(B)
print(A+B)

C,D=map(int,input().split()) #map(적용할 함수, 반복 가능한 자료형)
print(C+D)

a,b=map(int,input().split())
print(a-b)

#03
A,B=map(int, input().split())
if A>B: #조건식이 참일 때
    print('>')
elif A<B:   #if 조건식이 참이 아닌 경우, elif 조건식이 참일 때 문장
    print('<')
else:   #위의 모든 조건이 거짓일 때 문장
    print('==')

print('>') if A>B else print('<') if A<B else print('==')

#04
score=int(input())
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else: print('F')

#05 현재 시간에서 45분 뺀 시간 출력하기
H,M=map(int,input().split())
if H<45: #45분 보다 작을 경우
    if H==0: #시간이 0시일 경우
        H=23
        M+=60
    else: #그 외 경우
        H-=1
        M+=60
print(H,M-45)

#06 현재 시간에서 특정 시간(분단위) 더하기
h,m=map(int,input().split())
t=int(input())
h+=t//60
m+=t%60
if (m>=60):
    h+=1
    m-=60
if (h>=24):
    h-=24
print(h,m)

#07 구구단
n=int(input())
for i in range(1,10):
    print(n,'*',i,'=',n*i)

#08
T=int(input())
for i in range(T):
    s,d=map(int,input().split())
    print(s+d)