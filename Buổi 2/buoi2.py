print("Nhập điểm tổng kết của 3 môn")
toan = float(input("Toán:"))
van = float(input("Văn:"))
anh = float(input("Anh:"))
dtb = ((toan + van + anh)/3)
print("Học lực của bạn:")
if dtb >= 9:
    print("Bạn rất xuất sắc")
elif dtb >= 8:
    print("Đạt học sinh giỏi")
elif dtb >= 7:
    print("Bạn học khá")
elif dtb >= 5:
    print("Bạn học trung bình")
else:
    print("Bạn học kém")
