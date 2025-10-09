n = int(input(":Nhap n: "))
print("hộp")
print("* " * n)
for i in range(n - 2):
    print("* " + "  " * (n - 2) + "*")
print("* " * n)

print("tam giác")
for i in range(n):
        print("  "* (n - i) + "* "* (i))

print("zigzac")
j = n-1
print("* ")
for i in range(j):
    print("*" + "  "*(j - (j - i)) + " *")
print("* " * ((2*n)+1))
for i in range(j):
    print("  "*(2*j - (j-i)+2)+ "*"+"  "* (j-i-1)+ " *")
print("  "* (2*n) +"*")