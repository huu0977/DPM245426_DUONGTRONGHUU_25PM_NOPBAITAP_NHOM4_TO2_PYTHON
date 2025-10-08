import math

print("Tinh gia tri bieu thuc S")

x=int(input('nhập vào một số x='))
n=int(input('nhập vào một số n='))
S=0

for i in range(n+1):
    mu =2*i+1
    S+=x**mu/math.factorial(mu)
print(S)


