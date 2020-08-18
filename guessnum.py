import random

n = random.randint(1,10)

i = 1
print(n)
while i<6:   
    a = int(input("num:"))  
    if n == a:
        print("yes",i,'次')
        break
    else:   
        if a > n:
            print("Ans>Num")
        else:
            print("Ans<Num")
        print('no')
    i+=1