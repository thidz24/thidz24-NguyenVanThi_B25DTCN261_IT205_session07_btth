raw_input = "   nGuyen vaN aN  ;  2004   "

while True:
    choice = int(input("""===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
=====================================
    Nhập lựa chọn của bạn(1-4): """))

    match choice:
        case 1:
            print("Chuỗi dữ liệu gốc hiện tại: ")
            print(raw_input)
        case 2:
            new_raw_input = raw_input.strip().split(";")
            full_name = new_raw_input[0].strip().title()
            year = new_raw_input[1].strip()
            print("Kết quả chuẩn hóa dữ liệu")
            print("Họ tên: ",full_name)
            print("Tuổi ",2026 - int(year))
        case 3:
            new_raw_input = raw_input.strip().split(";")
            full_name = new_raw_input[0].strip().title()
            year = new_raw_input[1].strip()

            email = (full_name[0] + full_name[7] + full_name[11:13]).lower() + "@company.com"
            id = full_name[11:13].upper() + year[2:4]

            print(f"""==============================
    THẺ THÀNH VIÊN MỚI
==============================
Họ và tên: {full_name}
Email    : {email}
Mã ID    : {id}
==============================""")
        case 4:
            print("Đã thoát chương trình")
            break
        case _:
            print("Vui lòng nhập từ 1-4")