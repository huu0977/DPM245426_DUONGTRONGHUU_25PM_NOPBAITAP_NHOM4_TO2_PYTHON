print("CHƯƠNG TRÌNH TÍNH TOÁN")

a=int(input("Nhập vào một số a: "))
b=int(input("Nhập vào một số b: "))
n=input("Nhập vào phép toán cần tính: ")

match n:
    case "+":
        result= a+b
    case "-":
        result= a-b
    case "*":
        result= a*b
    case "/":
        if (b!=0):
           result= a/b
        else:
           print("không thể chia cho 0")

print("kết quả: ", result)