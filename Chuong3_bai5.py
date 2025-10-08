i=float(input("nhập i: "))
j=float(input("nhập j: "))
k=float(input("nhập k: "))
if i<j:
     if j<k:
       i = j
     else:
       j = k
else:
     if j>k:
         j = i
     else:
         i = k
print("i= ",i,',j= ',j,",k= ",k)
#(a) i = 3, j = 5, and k = 7 ->i=  5.0 ,j=  5.0 ,k=  7.0
#(c) i = 5, j = 3, and k = 7 ->i=  7.0 ,j=  3.0 ,k=  7.0
#(d) i = 5, j = 7, and k =3 ->i=  5.0 ,j=  3.0 ,k=  3.0
#(e) i = 7, j = 3, and k = 5 ->i=  5.0 ,j=  3.0 ,k=  5.0
#(f) i =7, j = 5, and k = 3 ->i=  7.0 ,j=  7.0 ,k=  3.0