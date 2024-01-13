def strt(r,c):
    posfw=[]
    posbw=[]
    posrt=[]
    poslf=[]
    i=r-1
    while i>0:
        posfw.append((i,c))
        i-=1
    i=r+1
    while i<9:
        posbw.append((i,c))
        i+=1
    j=c+1
    while j<9:
        posrt.append((r,j))
        j+=1
    j=c-1
    while j>0:
        poslf.append((r,j))
        j-=1
    poslf.reverse()
    posfw.reverse()
    return poslf,posrt,posfw,posbw
def diag(r,c):
    lfd=[]
    rfd=[]
    lbd=[]
    rbd=[]
    i,j=r+1,c+1
    while i<9 and j<9:
        rbd.append((i,j))
        j+=1
        i+=1
    i,j=r-1,c-1
    while i>0 and j>0:
        lfd.append((i,j))
        j-=1
        i-=1
    i,j=r-1,c+1
    while i>0 and j<9:
        rfd.append((i,j))
        j+=1
        i-=1
    i,j=r+1,c-1
    while i<9 and j>0:
        lbd.append((i,j))
        j-=1
        i+=1
    return lfd,rfd,lbd,rbd
n=input()
r=int(input())
c=int(input())
if n=='rook':#23176
    t=strt(r,c)
    txt=['left:','right:','forward:','backward:']
    for i in range(4):
        print(txt[i],end='')
        for j in range(len(t[i])-1):
            print(t[i][j],end=',')
        print(t[i][-1])
if n=='bishop':#chirag
    t=diag(r,c)
    txt=['left forward diagonal:','right forward diagonal:','left backward diagonal:','right backward diagonal:']
    for i in range(4):
        print(txt[i],end='')
        for j in range(len(t[i])-1):
            print(t[i][j],end=',')
        print(t[i][-1])
if n=='queen':#23176
    t=strt(r,c)
    txt=['left:','right:','forward:','backward:']
    for i in range(4):
        print(txt[i],end='')
        for j in range(len(t[i])-1):
            print(t[i][j],end=',')
        print(t[i][-1])
    t=diag(r,c)
    txt=['left forward diagonal:','right forward diagonal:','left backward diagonal:','right backward diagonal:']
    for i in range(4):
        print(txt[i],end='')
        for j in range(len(t[i])-1):
            print(t[i][j],end=',')
        print(t[i][-1])
if n=='pawn':#chirag
    print('forward:',(r-1,c))
    print('left forward diagonal:',(r-1,c-1))
    print('right forward diagonal:',(r-1,c+1))
if n=='king':#23176
    print('left:',(r,c-1))
    print('right:',(r,c+1))
    print('forward:',(r-1,c))
    print('backward:',(r+1,c))
    print('left forward diagonal:',(r-1,c-1))
    print('right forward diagonal:',(r-1,c+1))
    print('left backward diagonal:',(r+1,c-1))
    print('right backward diagonal:',(r+1,c+1))
