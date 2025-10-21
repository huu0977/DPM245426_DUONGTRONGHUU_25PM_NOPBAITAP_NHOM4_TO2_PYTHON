def tinh_tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong


def kiem_tra_hoan_thien(n):
    tong_uoc = tinh_tong_uoc_so(n)

    if n > 1 and tong_uoc == n:
        return True
    else:
        return False


def kiem_tra_thinh_vuong(n):
    tong_uoc = tinh_tong_uoc_so(n)

    if tong_uoc > n:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        n = int(input("Nhập một số nguyên dương n: "))

        if n <= 0:
            print("Vui lòng nhập số nguyên dương lớn hơn 0.")
        else:
            print(f"--- Kiểm tra số {n} ---")

            tong_cac_uoc = tinh_tong_uoc_so(n)
            print(f"Tổng các ước số của {n} (không kể {n}) là: {tong_cac_uoc}")

            if kiem_tra_hoan_thien(n):
                print(f"a) {n} LÀ số hoàn thiện.")
            else:
                print(f"a) {n} KHÔNG PHẢI là số hoàn thiện.")

            if kiem_tra_thinh_vuong(n):
                print(f"b) {n} LÀ số thịnh vượng.")
            else:
                print(f"b) {n} KHÔNG PHẢI là số thịnh vượng.")

    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")