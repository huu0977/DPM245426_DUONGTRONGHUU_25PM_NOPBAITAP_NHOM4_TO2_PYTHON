

print("CHƯƠNG TRÌNH KIỂM TRA QUÝ TRONG NĂM")

#nhập từ bàn phím
thang=int(input("Nhập vào một tháng: "))

if thang>12 or thang<1:
    print("tháng không hợp lệ")
else:
    match thang:
        case 1|2|3:
            print("Quý 1")
        case 4|5|6:
            print("Quý 2")
        case 7|8|9:
            print("Quý 3")
        case 10|11|12:
            print("Quý 4")