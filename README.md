1. binary_operations.py
File này chứa các hàm xử lý nhị phân cơ bản được sử dụng trong thuật toán DES:

hex_to_binary(): Chuyển đổi chuỗi hexa thành chuỗi nhị phân
binary_to_hex(): Chuyển đổi chuỗi nhị phân thành chuỗi hexa
permute(): Thực hiện hoán vị các bit theo bảng hoán vị
xor_bits(): Thực hiện phép XOR giữa hai chuỗi bit
substitute(): Thực hiện thay thế bit theo các S-box
split_bits(): Chia chuỗi bit thành hai nửa
swap_halves(): Hoán đổi hai nửa của chuỗi bit
format_binary(): Định dạng chuỗi nhị phân để hiển thị đẹp hơn
--------------------------------------------------------------
2. constants.py
File này chứa các bảng hằng số được sử dụng trong thuật toán DES:

IP: Bảng hoán vị ban đầu (Initial Permutation)
FP: Bảng hoán vị cuối cùng (Final Permutation)
E: Bảng mở rộng (Expansion) - mở rộng 32 bit thành 48 bit
P: Bảng hoán vị P dùng trong hàm Feistel
SBOX: Các bảng thay thế S-box (S1-S8)
PC1: Bảng hoán vị lựa chọn 1 dùng trong sinh khóa
PC2: Bảng hoán vị lựa chọn 2 dùng trong sinh khóa
SHIFT_SCHEDULE: Lịch dịch bit cho mỗi vòng sinh khóa
--------------------------------------------------------------
3. key_generation.py
File này xử lý quá trình sinh các khóa con từ khóa chính:

generate_subkeys(): Tạo 16 khóa con (mỗi khóa 48 bit) từ khóa gốc 64 bit
Áp dụng PC1 để chuyển 64 bit thành 56 bit
Chia thành hai nửa 28 bit
Thực hiện dịch trái theo lịch dịch
Áp dụng PC2 để tạo khóa con 48 bit cho mỗi vòng
--------------------------------------------------------------
4. encryption.py
File này xử lý quá trình mã hóa DES:

f_function(): Thực hiện hàm Feistel, bao gồm:
Mở rộng nửa phải từ 32 bit thành 48 bit
XOR với khóa con
Thay thế qua S-box (48 bit → 32 bit)
Hoán vị P
encrypt_des(): Thực hiện mã hóa DES hoàn chỉnh:
Áp dụng hoán vị ban đầu IP
Thực hiện 16 vòng lặp Feistel
Hoán đổi nửa trái và phải sau vòng thứ 16
Áp dụng hoán vị cuối FP
--------------------------------------------------------------
5. decryption.py
File này xử lý quá trình giải mã DES:

f_function(): Giống như trong encryption.py
decrypt_des(): Thực hiện giải mã DES hoàn chỉnh:
Tương tự như mã hóa nhưng sử dụng các khóa con theo thứ tự ngược lại (từ K16 đến K1)
--------------------------------------------------------------
6. main.py
File chính điều khiển luồng chương trình:

create_output_directory(): Tạo thư mục output để lưu kết quả
main(): Hàm chính với menu tương tác cho người dùng:
Mã hóa: Nhận bản rõ và khóa dạng hexa, thực hiện mã hóa
Giải mã: Nhận bản mã và khóa dạng hexa, thực hiện giải mã
Hiển thị chi tiết: Bật/tắt chế độ hiển thị chi tiết các bước
Thoát: Kết thúc chương trình
