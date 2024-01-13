def fib(n):
   """
   Gives fibonnaic of nth term
   """
   if n==0 or n==1:
       return 1
   return fib(n-1)+fib(n-2)

def palindorme(s):
   if len(s)<=1:
       return True
   return (s[0]==s[-1] and palindorme(s[1:len(s)-1]))

def TowerofHanoi(src,dest,aux,n):
   if n==1:
       print(src,'-->',dest)
       return
   TowerofHanoi(src,aux,dest,n-1)
   print(src,'-->',dest)
   TowerofHanoi(aux,dest,src,n-1)

def sorted(s):
    if len(s)<=1:
        return True
    return s[0]<=s[1] and sorted(s[1::])

def merge(s1,s2):
    if not (sorted(s1) and sorted(s2)):
        return -1
    if len(s1)==0 or len(s2)==0:
        return s1+s2
    if s1[0]<s2[0]:
        return ([s1[0]]+merge(s1[1::],s2))
    if s1[0]>=s2[0]:
        return ([s2[0]]+merge(s2[1::],s1))

def pascalstriangle(n):
    def pt(n):
        l=[]
        if n==0:
            return [1]
        if n==1:
            return [1,1]
        l.append(1)
        x=pt(n-1)
        for i in range(n-1):
            l.append(x[i]+x[i+1])
        l.append(1)
        return l
    n=int(input())
    for i in range(n+1):
        print((n-i)*' ',end='')
        for j in pt(i):
            print(j,end=' ')
        print()

def binarysearch (data,lind,rind,el):
        
        if lind>rind:       #check if the index is in the right order
                return (-1)
        m=int((lind+rind)//2)
        if el==data[m]:
                return m
        elif el<data[m]:
                rind=m-1
        elif el>data[m]:
                lind=m+1
        return binarysearch(data,lind,rind,el)

def mergesort(L):
    n=len(L)
    if n==1:
        return L
    m1=mergesort(L[0:n//2])
    m2=mergesort(L[n//2:])
    return merge(m1,m2)

def bubblesort(L):
    for j in range(len(L)-1,0,-1):
        for k in range(0,j):
            if L[k]>L[k+1]:
                L[k],L[k+1]=L[k+1],L[k]
    return L
    
def selectionsort(L):
    for i in range(len(L)):
        for k in range(i+1,len(L)):
            if L[i]>L[k]:
                L[i],L[k]=L[k],L[i]
    return L

def insertionsort(L):
    for i in range(1,len(L)):
        el=L[i]
        j=i-1
        while L[j]>el and j>=0:
            L[j+1]=L[j]
            j-=1
        L[j+1]=el
    return L



                   



    
    

