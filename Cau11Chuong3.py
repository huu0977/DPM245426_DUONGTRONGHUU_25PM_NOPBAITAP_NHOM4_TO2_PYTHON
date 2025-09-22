print("Kiểm tra số nguyên tố")
while True:
    n = int(input("Nhập một số nguyên dương: "))
    dem=0
    for i in range(1,n+1):
        if n%i==0:
            dem+=1
    if dem==2:
        print(n,"là một số nguyên tố")
    else:
        print(n,"không là một số nguyên tố")
        hoi=input("Có muốn tiếp tục không (yes/no):")
        if hoi == "no":
            break


