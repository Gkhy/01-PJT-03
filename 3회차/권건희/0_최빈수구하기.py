import sys
sys.stdin = open("_최빈수구하기.txt")
N=int(input())



for i in range(N):
    dic={}
    max_=0
    list_=[]
    score_=[]
    C=input()
    score_=list((map(int,input().split())))
    for n in score_:
        if n not in dic:
            dic[n]=1

        else:
            dic[n]+=1  

    for d in dic:
        if dic[d]>=max_:
            max_=dic[d]

    for a in dic:
        if dic[a]==max_:
            list_.append(a)
    ans=(max(list_))
    print(f'#{C} {ans}')        

