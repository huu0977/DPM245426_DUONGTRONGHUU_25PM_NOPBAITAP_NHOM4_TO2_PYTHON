
t=int(input("moi ban nhap so giay bat ky de tinh gio: "))
hour=(t//3600)%24
minute=(t%3600)//60
second=(t%3600)%60
print(hour,";",minute,";",second)