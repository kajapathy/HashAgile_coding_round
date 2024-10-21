#SOLUTION 1

def rotate(s,k):
    res=""
    k=k%len(s)
    for i in range(k,len(s)):
        res+=s[i]
    for i in range(k):
        res+=s[i]
    return res
s=input()
k=int(input())
final=rotate(s,k)
print(final)

# SOLUTION 2

def rotate(s,k):
    n=len(s)
    k=k%n

    left = ""
    right = ""
    for i in range(k,n):
        right+=s[i]

    for i in range(k):
        left+=s[i]

    return right+left
s=input()
k=int(input())
res=rotate(s,k)
print(res)


# SOLUTION 3

s=input()
k=int(input())
kj=list(s)
n=len(kj)

temp=kj[0:k]

for i in range(k,n):
    kj[i-k]=kj[i]
j=0
for i in range(n-k,n):
    kj[i]=temp[j]
    j+=1
print(''.join(map(str,kj)))
