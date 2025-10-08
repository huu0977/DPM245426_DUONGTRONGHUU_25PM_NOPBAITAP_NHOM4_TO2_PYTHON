print("VE HINH BANG DAU *")
n=int(input("nhập chiều cao n="))
for i in range(n):
    for j in range(n):
        if i ==0 or i==n-1 or j==0 or j==n-1:
            print("*", end="")
        else:
            print(" ",end="")
    print()
print()
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)