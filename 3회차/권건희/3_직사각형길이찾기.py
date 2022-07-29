import sys

sys.stdin = open("_직사각형길이찾기.txt")

T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())
    if a==c:
        print(f'#{i+1} {b}')
    else:
        if a==b:
             print(f'#{i+1} {c}')
        else: print(f'#{i+1} {a}')         