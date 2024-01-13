def fib(n):
   """
   Gives fibonnacci of nth term
   """
   if n==0 or n==1:
       return 1
   return fib(n-1)+fib(n-2)

def palindrome(s):
   """
   Returns palindrome for string s
   """
   if len(s)<=1:
       return True
   return (s[0]==s[-1] and palindrome(s[1:len(s)-1]))

def TowerofHanoi(src,dest,aux,n):
   """
   Returns the solution to a Tower of Hanoi problem with n discs
   """
   if n==1:
       print(src,'-->',dest)
       return
   TowerofHanoi(src,aux,dest,n-1)
   print(src,'-->',dest)
   TowerofHanoi(aux,dest,src,n-1)

def sorted(s):
   """
   checks if a string or list 's' is sorted
   """
    if len(s)<=1:
        return True
    return s[0]<=s[1] and sorted(s[1::])

def merge(s1,s2):
   """
   merges 2 sorted lists s1 and s2 so the resulting list is sorted
   """
    if not (sorted(s1) and sorted(s2)):
        return -1
    if len(s1)==0 or len(s2)==0:
        return s1+s2
    if s1[0]<s2[0]:
        return ([s1[0]]+merge(s1[1::],s2))
    if s1[0]>=s2[0]:
        return ([s2[0]]+merge(s2[1::],s1))

def pascalstriangle(n):
   """
   Prints out the Pascal's Triangle out to n rows
   """
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
        """
        searches the list data for element el
        lind and rind by default would be 0 and length of the list, respectively
        """
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
   """
   A sorting algorithm with time complexity O(n*log(n))
   """
    n=len(L)
    if n==1:
        return L
    m1=mergesort(L[0:n//2])
    m2=mergesort(L[n//2:])
    return merge(m1,m2)

def bubblesort(L):
   """
   A sorting algorithm with time complexity O(n*n)
   """
    for j in range(len(L)-1,0,-1):
        for k in range(0,j):
            if L[k]>L[k+1]:
                L[k],L[k+1]=L[k+1],L[k]
    return L
    
def selectionsort(L):
   """
   A sorting algorithm with time complexity O(n*n)
   """
    for i in range(len(L)):
        for k in range(i+1,len(L)):
            if L[i]>L[k]:
                L[i],L[k]=L[k],L[i]
    return L

def insertionsort(L):
   """
   A sorting algorithm with time complexity O(n*n)
   """
    for i in range(1,len(L)):
        el=L[i]
        j=i-1
        while L[j]>el and j>=0:
            L[j+1]=L[j]
            j-=1
        L[j+1]=el
    return L

def checkpower(a,b):
   """
   Checks if the number a is a power of the number b, returns a bool value
   """
    if a==b:
        return True
    return a%b==0 and checkpower(a/b,b)

def ceasar_encode(k,s):
   """ 
   Encodes the string s with the Ceaser cipher of shift k
   """
    if len(s)==0:
        return '' 
    if not (0<k<26):
        return "Invalid input"
    if not (s.isupper()) or not (s.isalpha()):
        return "Invalid Input"
    t=''
    for ch in s:
        neword=ord(ch)+k
        if neword>90:
            neword=neword-26
        newchr=chr(neword)
        t+=newchr
    return t

def ceaser_decode(k,t):
   """ 
   Decodes the string s with the Ceaser cipher of shift k
   """
    if len(t)==0:
        return '' 
    if not (0<k<26):
        return "Invalid input"
    if not (t.isupper()) or not (t.isalpha()):
        return "Invalid Input"
    s=''
    for ch in t:
        neword=ord(ch)-k
        if neword<65:
            neword=neword+26
        newchr=chr(neword)
        s+=newchr
    return s

def variable_len_repr(n):
   """
   Variable length representation in binary (base 2) of a decimal (base 10) number n
   """
    bin=''
    while n>1:
        bit=n%2
        bin=str(bit)+bin
        n=n//2
    bin=str(n)+bin
    return bin

def fixed_len_repr(n):
   """
   Fixed 8-bit representation in binary (base 2) of a decimal (base 10) number n
   """
    if n<0 or n>=256:
        return 'invalid'
    a=variable_len_repr(n)
    req_zeroes=8-len(a)
    extended_bin='0'*req_zeroes+a
    return extended_bin




                   



    
    

