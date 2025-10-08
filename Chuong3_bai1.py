print("chuong trinh kiem tra nam nhuan")
Nam=int(input("moi nhap vao mot nam: "))
if(Nam % 4 ==0 and Nam % 100 !=0) or Nam %400 == 0:
    print("nam ", Nam ,"la nam nhuan")
else:
    print("nam", Nam , " khong phai la nam nhuan")