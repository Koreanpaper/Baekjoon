'''#10807번
n=int(input()) # 정수의 개수를 입력
n_list=list(map(int,input().split())) # 입력받은 정수들의 리스트
v=int(input()) # 찾고자 하는 정수 입력
print(n_list.count(v)) # 리스트에서 찾고자 하는 정수 v의 개수를 출력

#10871번
N,X=map(int,input().split()) # N은 정수 N개의 값을 입력받음
A=list(map(int,input().split()))
for i in range(N):
    if A[i]<X:
        print(A[i], end=" ")'''

#10818번
N=int(input())
A=list(map(int,input().split()))
max=A[0]
min=A[0]
for i in A[1:]:
    if i>max: #리스트 첫번째 요소와 현재 i번째에 있는 요소와 비교
        max=i
    elif i<min:
        min=i
print(min,max)
