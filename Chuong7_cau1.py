#Câu 1: Quản lý Sản phẩm- Text File

#Bước 1: Tạo 1 Python XuLyFile.py :

def LuuFile(path,data):
 file=open(path,'a',encoding='utf-8')
 file.writelines(data)
 file.writelines("\n")
 file.close()

def DocFile(path):
 arrProduct=[]
 file=open(path,'r',encoding='utf-8')
 for line in file:
  data=line.strip()       # ⚙️ Lùi vào trong vòng for
  arr=data.split(';')
  arrProduct.append(arr)
 file.close()
 return arrProduct


 #Bước 2: Tạo 1 file TestLuuFile.py
 from XuLyFile import *
masp=input("nhập mã SP:")
tensp=input("nhập tên sp:")
dongia=float(input("nhập giá:"))
line=masp+";"+tensp+";"+str(dongia)
LuuFile("database.txt",line)

#Bước 3: Tạo 1 file TestDocFile.py
from XuLyFile import *
dssp=DocFile("database.txt")
#print(dssp)

def XuatSanPham(dssp):
 for row in dssp:
  for element in row:
   print(element,end='\t')
  print()
 print()

XuatSanPham(dssp)

def SortSp(dssp):
 for i in range(len(dssp)):
  for j in range(i+1,len(dssp)):          # ⚙️ không cần so sánh với chính mình
   a=dssp[i]
   b=dssp[j]
   if float(a[2]) < float(b[2]):          # ⚙️ đổi dấu để sắp xếp giảm dần
    dssp[i]=b
    dssp[j]=a

SortSp(dssp)
print("Sản phẩm sau khi sắp xếp giá:")
XuatSanPham(dssp)
