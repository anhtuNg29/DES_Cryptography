import os
from binary_operations import hex_to_binary, binary_to_hex, format_binary
from key_generation import generate_subkeys
from encryption import encrypt_des
from decryption import decrypt_des

def create_output_directory():
    """Create output directory if it doesn't exist"""
    if not os.path.exists('output'):
        os.makedirs('output')

def main():
    print("=" * 60)
    print("| " + "CHƯƠNG TRÌNH MÃ HÓA/GIẢI MÃ DES".center(56) + " |")
    print("=" * 60)
    
    create_output_directory()
    
    while True:
        print("\nLựa chọn chức năng:")
        print("1. Mã hóa")
        print("2. Giải mã")
        print("3. Hiển thị chi tiết hơn")
        print("4. Thoát")
        
        choice = input("Nhập lựa chọn của bạn (1-4): ")
        
        verbose_mode = False
        
        if choice == '1':
            plaintext = input("Nhập bản rõ (hexa, 16 ký tự): ").lower()
            key = input("Nhập khóa (hexa, 16 ký tự): ").lower()
            
            if len(plaintext) != 16 or len(key) != 16:
                print("Lỗi: Cả bản rõ và khóa phải có 16 ký tự hexa (64 bits)")
                continue
                
            try:
                # Convert hex to binary
                plaintext_bin = hex_to_binary(plaintext)
                key_bin = hex_to_binary(key)
                
                # Ask for detailed mode
                detail_choice = input("Hiển thị chi tiết quá trình? (y/n): ").lower()
                verbose_mode = detail_choice == 'y'
                
                # Generate subkeys
                subkeys = generate_subkeys(key_bin, verbose_mode)
                
                # Encrypt
                ciphertext_bin = encrypt_des(plaintext_bin, subkeys, verbose_mode)
                ciphertext = binary_to_hex(ciphertext_bin)
                
                print(f"\nKết quả mã hóa:")
                print(f"Bản rõ (hex): {plaintext}")
                print(f"Bản rõ (bin): {format_binary(plaintext_bin)}")
                print(f"Khóa (hex): {key}")
                print(f"Khóa (bin): {format_binary(key_bin)}")
                print(f"Bản mã (hex): {ciphertext}")
                print(f"Bản mã (bin): {format_binary(ciphertext_bin)}")
                print(f"\nCác bước chi tiết đã được lưu vào thư mục 'output'.")
                
            except ValueError as e:
                print(f"Lỗi: {e}")
                
        elif choice == '2':
            ciphertext = input("Nhập bản mã (hexa, 16 ký tự): ").lower()
            key = input("Nhập khóa (hexa, 16 ký tự): ").lower()
            
            if len(ciphertext) != 16 or len(key) != 16:
                print("Lỗi: Cả bản mã và khóa phải có 16 ký tự hexa (64 bits)")
                continue
                
            try:
                # Convert hex to binary
                ciphertext_bin = hex_to_binary(ciphertext)
                key_bin = hex_to_binary(key)
                
                # Ask for detailed mode
                detail_choice = input("Hiển thị chi tiết quá trình? (y/n): ").lower()
                verbose_mode = detail_choice == 'y'
                
                # Generate subkeys
                subkeys = generate_subkeys(key_bin, verbose_mode)
                
                # Decrypt
                plaintext_bin = decrypt_des(ciphertext_bin, subkeys, verbose_mode)
                plaintext = binary_to_hex(plaintext_bin)
                
                print(f"\nKết quả giải mã:")
                print(f"Bản mã (hex): {ciphertext}")
                print(f"Bản mã (bin): {format_binary(ciphertext_bin)}")
                print(f"Khóa (hex): {key}")
                print(f"Khóa (bin): {format_binary(key_bin)}")
                print(f"Bản rõ (hex): {plaintext}")
                print(f"Bản rõ (bin): {format_binary(plaintext_bin)}")
                print(f"\nCác bước chi tiết đã được lưu vào thư mục 'output'.")
                
            except ValueError as e:
                print(f"Lỗi: {e}")
                
        elif choice == '3':
            print("\nChế độ hiển thị chi tiết:")
            print("Khi bật chế độ này, chương trình sẽ hiển thị từng bước của quá trình")
            print("mã hóa/giải mã DES, bao gồm các giá trị trung gian và giải thích.")
            print("\nBạn có thể bật/tắt chế độ này khi thực hiện mã hóa hoặc giải mã.")
                
        elif choice == '4':
            print("\nCảm ơn bạn đã sử dụng chương trình!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1-4.")

if __name__ == "__main__":
    main()
