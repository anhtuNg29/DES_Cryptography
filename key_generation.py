import os
from binary_operations import permute, left_shift, format_binary
from constants import PC1, PC2, SHIFT_SCHEDULE

def generate_subkeys(key_64bits, verbose=False):
    """
    Generate 16 subkeys for DES encryption/decryption
    
    Args:
        key_64bits: 64-bit key in binary string format
        verbose: If True, prints detailed steps to console
        
    Returns:
        List of 16 subkeys, each 48 bits
    """
    # Create output file
    with open('output/key_generation.txt', 'w') as f:
        f.write("DES KEY GENERATION PROCESS\n")
        f.write("==========================\n\n")
        f.write(f"Original 64-bit Key: {key_64bits}\n\n")
    
    if verbose:
        print("\n" + "=" * 60)
        print("| " + "DES KEY GENERATION PROCESS".center(56) + " |")
        print("=" * 60)
        print(f"Original 64-bit Key: {format_binary(key_64bits)}")
        print("-" * 60)
    
    # Step 1: Apply PC-1 permutation (64 bits -> 56 bits)
    key_56bits = permute(key_64bits, PC1)
    with open('output/key_generation.txt', 'a') as f:
        f.write(f"Step 1: Apply PC-1 (64 bits -> 56 bits)\n")
        f.write(f"Key after PC-1: {key_56bits}\n\n")
    
    if verbose:
        print("\nBước 1: Áp dụng PC-1 (64 bits -> 56 bits)")
        print(f"Khóa sau PC-1: {format_binary(key_56bits, 7)}")
        print("Giải thích: PC-1 loại bỏ bit chẵn lẻ và hoán vị các bit còn lại")
    
    # Split into left and right halves (28 bits each)
    c0 = key_56bits[:28]
    d0 = key_56bits[28:]
    with open('output/key_generation.txt', 'a') as f:
        f.write(f"Split into C0 and D0 (28 bits each):\n")
        f.write(f"C0: {c0}\n")
        f.write(f"D0: {d0}\n\n")
    
    if verbose:
        print("\nCắt thành C0 và D0 (mỗi phần 28 bits):")
        print(f"C0: {format_binary(c0, 7)}")
        print(f"D0: {format_binary(d0, 7)}")
    
    # Store C and D values for each round
    c_values = [c0]
    d_values = [d0]
    
    # Generate 16 rounds of C and D by applying left shifts
    for i in range(16):
        # Apply left shifts according to the shift schedule
        shift = SHIFT_SCHEDULE[i]
        c_next = left_shift(c_values[i], shift)
        d_next = left_shift(d_values[i], shift)
        
        c_values.append(c_next)
        d_values.append(d_next)
        
        with open('output/key_generation.txt', 'a') as f:
            f.write(f"Round {i+1}:\n")
            f.write(f"Left shift by {shift} bit(s)\n")
            f.write(f"C{i+1}: {c_next}\n")
            f.write(f"D{i+1}: {d_next}\n\n")
        
        if verbose:
            print(f"\nVòng {i+1}:")
            print(f"Dịch trái {shift} bit:")
            print(f"C{i+1}: {format_binary(c_next, 7)}")
            print(f"D{i+1}: {format_binary(d_next, 7)}")
    
    # Generate subkeys by applying PC-2 to the concatenated C and D values
    subkeys = []
    
    with open('output/key_generation.txt', 'a') as f:
        f.write("Subkey Generation:\n")
        f.write("=================\n\n")
    
    if verbose:
        print("\n" + "=" * 60)
        print("| " + "SINH KHÓA CON".center(56) + " |")
        print("=" * 60)
    
    for i in range(16):
        # Concatenate C and D
        cd = c_values[i+1] + d_values[i+1]
        
        # Apply PC-2 permutation (56 bits -> 48 bits)
        subkey = permute(cd, PC2)
        subkeys.append(subkey)
        
        # Convert to hex for display
        subkey_hex = hex(int(subkey, 2))[2:].upper().zfill(12)
        
        with open('output/key_generation.txt', 'a') as f:
            f.write(f"Subkey {i+1} (K{i+1}):\n")
            f.write(f"CD{i+1}: {cd}\n")
            f.write(f"After PC-2: {subkey}\n")
            f.write(f"Subkey {i+1} (hex): {subkey_hex}\n\n")
        
        if verbose:
            print(f"\nKhóa con {i+1} (K{i+1}):")
            print(f"CD{i+1}: {format_binary(cd, 7)}")
            print(f"Sau PC-2: {format_binary(subkey, 6)}")
            print(f"Khóa con {i+1} (hex): {subkey_hex}")
            print("Giải thích: PC-2 bỏ 8 bit từ 56 bit và hoán vị còn lại thành 48 bit cho khóa con")
    
    return subkeys