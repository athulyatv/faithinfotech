def rotate(l,n):
    if n==0:
        return
    if n>0:
        for i in range(n):
            x=l.pop()
            l.insert(0,x)
    else:
        for i in range(-n):

            x=l.pop(0)
            l.append(x)
            return
list=[1,2,3,4,5,6,7,8,9,10]
n=int(input("enter a number"))
rotate(list,n)
print(list)

#slicing
l=[1,2,3,45,6,7,9]
n=int(input("enter a no:"))
l1=(l[-n:]+l[:-n])
print(l1)