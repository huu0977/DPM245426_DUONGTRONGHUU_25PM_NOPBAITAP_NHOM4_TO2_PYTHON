print("CHƯƠNG TRÌNH CHO BIẾT NGÀY TIẾP THEO")

print("Hãy nhập: ngày/tháng/năm ------->")
day=int(input("ngày: "))
month=int(input("tháng: "))
year=int(input("năm: "))
ngayke=day+1
thangke=month+1
namke=year+1

if day<1 or ngayke<1:
    print("không có ngày đó mời nhập lại")
elif (month in (4,6,9,11)):
      if day == 30:
        print("1","/",thangke,"/",year)
      elif day>30:
        print("ko có ngày này")
      else:
          print(ngayke, "/", month, "/", year)
elif month == 2 and day >29:
    print("không có ngày đó trong tháng 2 mời nhập lại ")
elif month == 2 and ngayke >29:
    print("không có ngày đó trong tháng 2 mời nhập lại ")
elif month in (1, 3, 5, 7, 8, 10) and day == 31 :
    print("1", "/", thangke, "/", year)
elif month == 12 and day == 31:
    print("1","/1/",namke)
elif day>31 or month>12:
    print("Không có ngày hoặc tháng đó mời nhập lại")
elif month<=12 and day<31:
    print(ngayke,"/",month,"/",year)

