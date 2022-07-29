import sys

sys.stdin = open("_신용카드만들기1.txt")

T=int(input())
for i in range(T):
    list_=list(map(int,input().split()))
    odd=[]
    even=[]
    for l in range(1,len(list_)+1):
        if l%2==0:
            even.append(list_[l-1])
        else:
            odd.append(2*(list_[l-1]))           
    a=(sum(odd)+sum(even))
    N=(10-(a%10))%10      
    print(f'#{i+1} {N}')

