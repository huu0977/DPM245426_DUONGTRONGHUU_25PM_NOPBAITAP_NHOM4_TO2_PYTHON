import math

print("Chương trình tính log")


a=float(input("Nhập lại a:"))
x=float(input("Nhập lại x:"))
while a<0 or x<0 or a==1:
    a = float(input("Nhập a:"))
    x = float(input("Nhập x:"))
kq=math.log(x)/math.log(a)
print("giá trị log_a(x)=",kq)