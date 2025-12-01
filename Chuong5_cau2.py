#Câu 2: Viết chương trình tối ưu chuỗi

def ToiUuChuoi(s):
    s2 = s.strip()            # Bỏ khoảng trắng ở đầu & cuối
    arr = s2.split(' ')       # Tách các phần của chuỗi theo dấu cách
    s2 = ""
    for x in arr:
        word = x.strip()
        if len(word) != 0:    # Bỏ qua từ rỗng (do có nhiều dấu cách)
            s2 = s2 + word + " "
    return s2.strip()         # Xóa khoảng trắng dư ở cuối

s = "   Trần    Duy    Thanh   "
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))