import math

print("Tính diện tích tam giác")

a=float(input("Nhập cạnh a:"))
b=float(input("Nhập cạnh b:"))
c=float(input("Nhập cạnh c:"))

while(a<=0 or b<=0 or c<=0) or (a+b)<=c or (a+c)<=b or (c+b)<=a:
    print("mời nhập lại")
    a = float(input("Nhập cạnh a:"))
    b = float(input("Nhập cạnh b:"))
    c = float(input("Nhập cạnh c:"))
else:
    cv=a+b+c
    p=cv/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("diện tích tam giác =",s)
