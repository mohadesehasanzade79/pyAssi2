import random
pc_num= random.randint(0,20)
c=1
while True:
    user_num=int (input("enter number: "))
    if pc_num==user_num:
        print ("barande shod")
        print("count",c)
        break
    elif pc_num>user_num:
        print("boro balatar")
        c =c+1
    elif pc_num<user_num:
        print("boro paein tar")
        c=c+1