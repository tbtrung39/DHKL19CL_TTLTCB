# bài 9
def xu_ly_san_bay():
    try:
        # 1. Đọc dữ liệu từ PASSENGERS.IN
        with open('PASSENGERS.IN', 'r') as f:
            lines = f.readlines()
            # Dòng đầu tiên là số khách
            num_passengers = int(lines[0].strip())
            
            # Ghi chuẩn bị cho file đầu ra
            f_weight = open('WEIGHT.OUT', 'w')
            f_canceled = open('CANCELED.OUT', 'w')
            
            # Xử lý từng hành khách (bắt đầu từ dòng thứ 2)
            for i in range(1, num_passengers + 1):
                # Tách trọng lượng từng túi của khách i
                bags = list(map(float, lines[i].split()))
                
                total_weight = sum(bags)
                num_bags = len(bags)
                
                # Ghi tổng trọng lượng vào WEIGHT.OUT
                f_weight.write(f"{total_weight:.2f}\n")
                
                # Kiểm tra điều kiện hủy: > 23kg hoặc > 5 túi
                if total_weight > 23.0 or num_bags > 5:
                    f_canceled.write(f"{i} -> Khách {i} bị hủy chuyến: ")
                    if total_weight > 23.0:
                        f_canceled.write(f"Trọng lượng {total_weight:.2f} > 23kg. ")
                    if num_bags > 5:
                        f_canceled.write(f"Số lượng {num_bags} > 5 túi.")
                    f_canceled.write("\n")
            
            f_weight.close()
            f_canceled.close()
            
        print("Đã xử lý xong! Kiểm tra các file WEIGHT.OUT và CANCELED.OUT.")

    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file PASSENGERS.IN")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Chạy chương trình
xu_ly_san_bay()