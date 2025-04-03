def hex_to_binary(hex_string):
    """Convert hexadecimal string to binary string"""
    try:
        # Convert to integer then to binary, remove '0b' prefix and pad to 64 bits
        binary = bin(int(hex_string, 16))[2:].zfill(64)
        return binary
    except ValueError:
        raise ValueError("Invalid hexadecimal string")

def binary_to_hex(binary_string):
    """Convert binary string to hexadecimal string"""
    try:
        # Convert to integer then to hex, remove '0x' prefix and pad
        hex_value = hex(int(binary_string, 2))[2:].zfill(16)
        return hex_value
    except ValueError:
        raise ValueError("Invalid binary string")

def left_shift(bits, shift_amount):
    """Perform left circular shift on a bit string"""
    return bits[shift_amount:] + bits[:shift_amount]

def xor_bits(bits1, bits2):
    """Perform XOR operation on two bit strings of the same length"""
    if len(bits1) != len(bits2):
        raise ValueError("Bit strings must be of the same length for XOR operation")
    
    result = ""
    for b1, b2 in zip(bits1, bits2):
        result += "1" if b1 != b2 else "0"
    
    return result

def split_bits(bits, n):
    """Split a bit string into chunks of size n"""
    return [bits[i:i+n] for i in range(0, len(bits), n)]

def permute(bits, permutation_table):
    """Permute the bits according to the given permutation table"""
    return ''.join(bits[i-1] for i in permutation_table)

def substitute(bits, sbox):
    """Apply S-box substitution to 6-bit chunks, producing 4-bit outputs"""
    # Split the 48-bit input into 8 chunks of 6 bits each
    chunks = split_bits(bits, 6)
    result = ""
    
    # Process each 6-bit chunk with its corresponding S-box
    for i, chunk in enumerate(chunks):
        # The first and last bits determine the row (0-3)
        row = int(chunk[0] + chunk[5], 2)
        # The middle 4 bits determine the column (0-15)
        col = int(chunk[1:5], 2)
        
        # Get the value from the S-box and convert to 4-bit binary
        value = bin(sbox[i][row][col])[2:].zfill(4)
        result += value
        
    return result

def swap_halves(left, right):
    """Swap the left and right halves"""
    return right, left

def format_binary(binary_str, group_size=8):
    """Format binary string with spaces for readability"""
    return ' '.join(binary_str[i:i+group_size] for i in range(0, len(binary_str), group_size))