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
    "add":"0110011",
    "sub":"0110011",
    "sll":"0110011",
    "slt":"0110011",
    "sltu":"0110011",
    "xor":"0110011",
    "srl":"0110011",
    "or":"0110011",
    "and":"0110011",
}

dict_func3={
    "add":"000",
    "sub":"000",
    "sll":"001",
    "slt":"010",
    "sltu":"011",
    "xor":"100",
    "srl":"101",
    "or":"110",
    "and":"111",
}

dict_func7={
    "add":"0000000",
    "sub":"0100000",
    "sll":"0000000",
    "slt":"0000000",
    "sltu":"0000000",
    "xor":"0000000",
    "srl":"0000000",
    "or":"0000000",
    "and":"0000000",
}

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
        src_reg2 = registers.split(",")[2].strip()

        if instruction not in dict_func7 :
            print(f"Error: Instruction {instruction} is not recognized.")
            continue

        if dest_reg not in dict_registers or src_reg1 not in dict_registers or src_reg2 not in dict_registers:
            print(f"Error: Register(s) {dest_reg}, {src_reg1}, {src_reg2} is/are not recognized.")
            continue

        x = dict_func7[instruction] + " " + dict_registers[src_reg2] + " " + dict_registers[src_reg1] + " " + dict_func3[instruction] + " " + dict_registers[dest_reg] + " " + dict_opcode[instruction]

        print(x)