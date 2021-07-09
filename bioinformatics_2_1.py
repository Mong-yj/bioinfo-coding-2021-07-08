num = int(input("Which times table: "))
if (num > 9) or (num < 1):
    print("What?")
    num = int(input("Wich times table: "))
for i in range(1,10):
    print("%d * %d = %d"%(num,i,num*i))

