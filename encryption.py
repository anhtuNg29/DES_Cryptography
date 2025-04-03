import os
from binary_operations import permute, xor_bits, substitute, split_bits, swap_halves, format_binary
from constants import IP, E, SBOX, P, FP

def f_function(right_half, subkey):
    """
    Feistel (F) function in DES
    
    Args:
        right_half: 32-bit right half of the block
        subkey: 48-bit subkey for this round
        
    Returns:
        32-bit output from the F function and intermediate results
    """
    # Step 1: Expand 32-bit right half to 48 bits using E table
    expanded = permute(right_half, E)
    
    # Step 2: XOR with the subkey
    xored = xor_bits(expanded, subkey)
    
    # Step 3: Apply S-box substitution (48 bits -> 32 bits)
    substituted = substitute(xored, SBOX)
    
    # Step 4: Apply permutation P
    permuted = permute(substituted, P)
    
    return expanded, xored, substituted, permuted

def encrypt_des(plaintext_bin, subkeys, verbose=False):
    """
    Encrypt plaintext using DES algorithm
    
    Args:
        plaintext_bin: 64-bit plaintext in binary string format
        subkeys: List of 16 subkeys, each 48 bits
        verbose: If True, prints detailed steps to console
        
    Returns:
        64-bit ciphertext in binary string format
    """
    # Create output file
    with open('output/encryption_process.txt', 'w') as f:
        f.write("DES ENCRYPTION PROCESS\n")
        f.write("======================\n\n")
        f.write(f"Original plaintext (64 bits): {plaintext_bin}\n\n")
    
    if verbose:
        print("\n" + "=" * 60)
        print("| " + "QUÁ TRÌNH MÃ HÓA DES".center(56) + " |")
        print("=" * 60)
        print(f"Bản rõ gốc (64 bits): {format_binary(plaintext_bin)}")
        print("-" * 60)
    
    # Step 1: Apply initial permutation (IP)
    ip_result = permute(plaintext_bin, IP)
    with open('output/encryption_process.txt', 'a') as f:
        f.write(f"Step 1: Apply Initial Permutation (IP)\n")
        f.write(f"After IP: {ip_result}\n\n")
    
    if verbose:
        print("\nBước 1: Áp dụng hoán vị ban đầu (IP)")
        print(f"Sau IP: {format_binary(ip_result)}")
        print("Giải thích: IP hoán vị các bit theo bảng IP đã định nghĩa")
    
    # Split into left and right halves (32 bits each)
    left = ip_result[:32]
    right = ip_result[32:]
    with open('output/encryption_process.txt', 'a') as f:
        f.write(f"Split into left and right halves (32 bits each):\n")
        f.write(f"L0: {left}\n")
        f.write(f"R0: {right}\n\n")
    
    if verbose:
        print("\nCắt thành nửa trái và nửa phải (mỗi nửa 32 bits):")
        print(f"L0: {format_binary(left)}")
        print(f"R0: {format_binary(right)}")
    
    # Store all L and R values for display at the end
    l_values = [left]
    r_values = [right]
    
    # 16 rounds of processing
    for i in range(16):
        with open('output/encryption_process.txt', 'a') as f:
            f.write(f"Round {i+1}:\n")
            f.write(f"==========\n")
            f.write(f"L{i}: {left}\n")
            f.write(f"R{i}: {right}\n")
            f.write(f"Subkey {i+1}: {subkeys[i]}\n\n")
        
        if verbose:
            print(f"\n{'-' * 60}")
            print(f"Vòng {i+1}:")
            print(f"L{i}: {format_binary(left)}")
            print(f"R{i}: {format_binary(right)}")
            print(f"Khóa con {i+1}: {format_binary(subkeys[i], 6)}")
        
        # Save the current right half (it will become the new left half)
        new_left = right
        
        # Apply Feistel (F) function
        expanded, xored, substituted, permuted = f_function(right, subkeys[i])
        
        with open('output/encryption_process.txt', 'a') as f:
            f.write(f"F function processing:\n")
            f.write(f"1. Expansion E(R{i}): {expanded}\n")
            f.write(f"2. XOR with subkey: {xored}\n")
            f.write(f"3. S-box substitution: {substituted}\n")
            f.write(f"4. Permutation P: {permuted}\n\n")
        
        if verbose:
            print("\nXử lý hàm F:")
            print(f"1. Mở rộng E(R{i}): {format_binary(expanded, 6)}")
            print(f"   Giải thích: Mở rộng 32 bit thành 48 bit theo bảng E")
            print(f"2. XOR với khóa con: {format_binary(xored, 6)}")
            print(f"   Giải thích: XOR 48 bit đã mở rộng với khóa con 48 bit")
            print(f"3. Thay thế S-box: {format_binary(substituted)}")
            print(f"   Giải thích: Chia 48 bit thành 8 khối 6 bit, mỗi khối qua bảng S tương ứng ra 4 bit")
            print(f"4. Hoán vị P: {format_binary(permuted)}")
            print(f"   Giải thích: Hoán vị 32 bit sau S-box theo bảng P")
        
        # XOR the result with the left half to get the new right half
        new_right = xor_bits(left, permuted)
        with open('output/encryption_process.txt', 'a') as f:
            f.write(f"5. XOR with L{i}: {new_right}\n\n")
        
        if verbose:
            print(f"5. XOR với L{i}: {format_binary(new_right)}")
            print(f"   Giải thích: XOR kết quả với nửa trái L{i} để tạo nửa phải mới")
        
        # Update left and right for the next round
        left = new_left
        right = new_right
        
        # Store for final display
        l_values.append(left)
        r_values.append(right)
        
        with open('output/encryption_process.txt', 'a') as f:
            f.write(f"After Round {i+1}:\n")
            f.write(f"L{i+1}: {left}\n")
            f.write(f"R{i+1}: {right}\n\n")
        
        if verbose:
            print(f"\nSau Vòng {i+1}:")
            print(f"L{i+1}: {format_binary(left)}")
            print(f"R{i+1}: {format_binary(right)}")
    
    # Step 17: Swap the final left and right halves
    final_swap = right + left
    with open('output/encryption_process.txt', 'a') as f:
        f.write(f"Step 17: Final swap (R16 + L16)\n")
        f.write(f"After swap: {final_swap}\n\n")
    
    if verbose:
        print("\nBước 17: Hoán đổi cuối cùng (R16 + L16)")
        print(f"Sau hoán đổi: {format_binary(final_swap)}")
        print("Giải thích: Đổi vị trí nửa trái và nửa phải cuối cùng")
    
    # Step 18: Apply final permutation (FP)
    ciphertext = permute(final_swap, FP)
    with open('output/encryption_process.txt', 'a') as f:
        f.write(f"Step 18: Apply Final Permutation (FP)\n")
        f.write(f"Ciphertext (64 bits): {ciphertext}\n")
    
    if verbose:
        print("\nBước 18: Áp dụng hoán vị cuối cùng (FP)")
        print(f"Bản mã (64 bits): {format_binary(ciphertext)}")
        print("Giải thích: FP là hoán vị ngược của IP, hoàn tất quá trình mã hóa")
        print("\n" + "=" * 60)
        print("| " + "BẢNG TỔNG HỢP CÁC VÒNG MÃ HÓA".center(56) + " |")
        print("=" * 60)
        print("| {:^4} | {:^20} | {:^20} |".format("Vòng", "L", "R"))
        print("-" * 60)
        
        for i in range(17):
            print("| {:^4} | {:^20} | {:^20} |".format(
                i, 
                l_values[i][:4] + "..." + l_values[i][-4:], 
                r_values[i][:4] + "..." + r_values[i][-4:]
            ))
        
        print("=" * 60)
    
    return ciphertext