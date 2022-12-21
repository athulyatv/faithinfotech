def findfeb(n):
    f=0
    s=1
    t=0
    if(n>0):
        if(n==1):
            print(f)
        elif(n==2):
            print(f,s)
        else:
            print(f,s,end=" ")
            for i in range(3,n+1):
                t=f+s
                print(t,end=" ")
                f=s
                s=t
n=int(input("enter the limit"))
findfeb(n)

# using list
def fib(n):
    l=[0]
    a,b=0,1
    for i in range(n):

        a,b=b,a+b
        l.append(a)
    return l
print(fib(20))

# def findpal(n):
#     org=n
#     rev=0
#     while(n>0):
#         r=n%10
#         rev=(rev*10)+r
#         n=n//10
#     if(org==rev):
#         print("it is a palindrom")
#     else:
#         print("not a palindrom")
# n=int(input("enter a number:"))
# findpal(n)
#
#
# def rotate(l,n):
#     if n==0:
#         return
#     if n>0:
#         for i in range(n):
#             x=l.pop()
#             l.insert(0,x)
#     else:
#         for i in range(-n):
#
#             x=l.pop(0)
#             l.append(x)
#             return
# list=[1,2,3,4,5,6,7,8,9,10]
# n=int(input("enter a number"))
# rotate(list,n)
# print(list)

#slicing
l=[1,2,3,45,6,7,9]
n=int(input("enter a no:"))
l1=(l[-n:]+l[:-n])
print(l1)
print(l[-n:])
print(l[:-n])

