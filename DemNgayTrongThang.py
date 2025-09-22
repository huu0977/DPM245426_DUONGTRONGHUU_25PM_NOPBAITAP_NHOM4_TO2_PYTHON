print("chuong trinh dem ngay trong thang")

Thang=int(input("nhap vao 1 thang: "))
if Thang in (1,3,5,7,8,10,12):
    print("thang ", Thang ," co 31 ngay")
elif Thang in (4,6,9,11):
    print("thang ", Thang ," co 30 ngay")
elif Thang == 2:
    Nam=int(input("moi ban nhap vao nam"))
    if(Nam % 4 == 0 and Nam %100 !=0) or Nam %100 == 0:
        print("thang ", Thang ,"co 29 ngay")
    else:
        print("thang ", Thang ,"co 28 ngay")
else:
    print("Thang ",Thang," khong hop le")


