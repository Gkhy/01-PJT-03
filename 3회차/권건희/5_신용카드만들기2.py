import sys

sys.stdin = open("_신용카드만들기2.txt")
T=int(input())
for i in range(T):
    number=input()
    if '-' in number:
        number=number.replace('-','')    
    if number[0] in ['3','4','5','6','9']:
        if len(number)==16:
            print(f'#{i+1} 1')
        else: print(f'#{i+1} 0')   
    else: print(f'#{i+1} 0')    