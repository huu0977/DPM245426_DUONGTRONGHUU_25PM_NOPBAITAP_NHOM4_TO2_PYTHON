print("Chương trình đọc số:")

n=int(input("Nhập một số n có tối đa 2 chữ số: "))
SoHangChuc=n//10
SoHangDonVi=n%10
if n>100:
    print("ERROR")
elif n==0:
    print("không")
elif n<10:
    match n:
      case 1:
          result="một"
      case 2:
          result="hai"
      case 3:
          result="ba"
      case 4:
          result="bốn"
      case 5:
          result="năm"
      case 6:
          result="sáu"
      case 7:
          result="bảy"
      case 8:
          result="tám"
      case 9:
          result="chín"
    print(result)
elif n>=10:
    #đọc số hàng chục
    match SoHangChuc:
      case 1:
         result ="mười"
      case 2:
         result = "hai mươi"
      case 3:
         result = "ba mươi"
      case 4:
         result = "bốn mươi"
      case 5:
         result = "năm mươi"
      case 6:
         result = "sáu mươi"
      case 7:
         result = "bảy mươi"
      case 8:
         result = "tám mươi"
      case 9:
         result = "chín mươi"

    #đọc số hàng đơn vị
    if SoHangDonVi!=0:
     match SoHangDonVi:
      case 1:
           result +=" mốt"
      case 2:
           result += " hai"
      case 3:
           result += " ba"
      case 4:
           result += " bốn"
      case 5:
           result += " lăm"
      case 6:
           result += " sáu"
      case 7:
           result += " bảy"
      case 8:
           result += " tám"
      case 9:
           result += " chín"
     print(result)