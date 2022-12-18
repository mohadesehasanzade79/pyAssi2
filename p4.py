a=[]
while True:
    b=int(input("enter number: "))
    a.append(b)
    c=input("exit?")
    if c=="exit":
        break
s=sum(a)
print("sum",s)