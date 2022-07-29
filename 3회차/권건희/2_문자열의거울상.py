import sys

sys.stdin = open("_문자열의거울상.txt")
T= int(input())
for i in range(T):
    words=input()
    sdrow=words[::-1]
    if 'q' in sdrow:
        sdrow=sdrow.replace('q','*')
    if 'p' in sdrow:
        sdrow=sdrow.replace('p','@')
    if 'd' in sdrow:
        sdrow=sdrow.replace('d','?')
    if 'b' in sdrow:
        sdrow=sdrow.replace('b','-')
    if '*'in sdrow:
         sdrow=sdrow.replace('*','p')
    if '@'in sdrow:
         sdrow=sdrow.replace('@','q')
    if '?'in sdrow:
         sdrow=sdrow.replace('?','b')
    if '-'in sdrow:
         sdrow=sdrow.replace('-','d')                  
    print(f'#{i+1} {sdrow}')           