print("SO DAU *")

dem=0
a=0
while a<100:
    b=0
    while b<40:
        if (a+b)%2==0:
            print("*", end='')
            dem+=1
        b+=1
    print()
    a+=1

print(dem)
#Số dấu "*" là 2000