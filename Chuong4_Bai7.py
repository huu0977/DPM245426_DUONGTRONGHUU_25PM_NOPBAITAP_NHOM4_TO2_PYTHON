import math

print("TÍNH VÀ XUẤT ĐỘ DÀI ĐOẠN AB")

xA=float(input("Nhập tọa độ XA:"))
yA=float(input("Nhập tọa độ YA:"))
xB=float(input("Nhập tọa độ XB:"))
yB=float(input("Nhập tọa độ YB:"))

AB=math.sqrt(((xB-xA)**2) + ((yB-yA)**2))

print("|AB|=",AB)