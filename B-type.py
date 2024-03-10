dict_registers = {
    "zero": "00000",
    "ra": "00001",
    "sp": "00010",
    "gp": "00011",
    "tp": "00100",
    "t0": "00101",
    "t1": "00110",
    "t2": "00111",
    "s0": "01000",
    "fp": "01000",
    "s1": "01001",
    "a0": "01010",
    "a1": "01011",
    "a2": "01100",
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",
    "s2": "10010",
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",
    "t3": "11100",
    "t4": "11101",
    "t5": "11110",
    "t6": "11111"
}
    
dict_opcode={
    # B-type 
    "beq":"1100011",
    "bne":"1100011",
    "blt":"1100011",
    "bge":"1100011",
    "bltu":"1100011",
    "bgeu":"1100011",
}

dict_func3={
    # B-type
    "beq":"000",
    "bne":"001",
    "blt":"100",
    "bge":"101",
    "bltu":"110",
    "bgeu":"111",
}

def immediate1(immediate, num_bits=12):
    if immediate >= 0:
        binary_result = ""
        while immediate > 0:
            remainder = immediate % 2
            binary_result = str(remainder) + binary_result
            immediate //= 2

        while len(binary_result) < num_bits:
            binary_result = '0' + binary_result

        return binary_result
    else:
        abs_immediate = abs(immediate)
        binary_result = ""

        while abs_immediate > 0:
            remainder = abs_immediate % 2
            binary_result = str(remainder) + binary_result
            abs_immediate //= 2

        while len(binary_result) < num_bits:
            binary_result = '0' + binary_result

        flipped_binary = ""
        for bit in binary_result:
            flipped_binary += '1' if bit == '0' else '0'

        result = ""
        carry = 1
        for bit in flipped_binary[::-1]:
            temp_sum = int(bit) + carry
            result = str(temp_sum % 2) + result
            carry = temp_sum // 2

        result = result.lstrip('0') or '0'

        result = '1' + result[1:]

        while len(result) < num_bits:
            result = '0' + result

        result=str(result)
        return result


i = 0
with open("hello.txt", 'r') as f:
    for line in f: 
        i += 1
        if not line.strip():  
            continue
        a = line.split()
        if len(a) < 2:  
            print(f"Error: Line {i} does not contain an instruction and registers.")
            continue
        instruction = a[0]
        registers = a[1]

        dest_reg = registers.split(",")[0].strip()
        src_reg1 = registers.split(",")[1].strip()
        label = registers.split(",")[2].strip()

        label=int(label)

        if instruction not in dict_func3 :
            print(f"Error: Instruction {instruction} is not recognized.")
            continue

        if dest_reg not in dict_registers or src_reg1 not in dict_registers :
            print(f"Error: Register(s) {dest_reg}, {src_reg1} is/are not recognized.")
            continue

        # for B-type instruction
        x=immediate1(label)[:7] + ' ' + dict_registers[src_reg1] + ' ' + dict_registers[dest_reg] + ' ' + dict_func3[instruction] + ' ' + immediate1(label)[7:] + ' ' + dict_opcode[instruction]

        print(x)
