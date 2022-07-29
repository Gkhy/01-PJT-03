import sys

sys.stdin = open("_소득불균형.txt")
T=int(input())
for i in range(T):
    N=int(input())
    cnt=0
    numbers=list(map(int,input().split()))
    pg=sum(numbers)/N
    for n in numbers:
        if n- pg<=0:
            cnt+=1
    print(f'#{i+1} {cnt}')        