u = open("output.txt",'w+')
dict_registers = {
    "00000": "zero",
    "00001": "ra",
    "00010": "sp",
    "00011": "gp",
    "00100": "tp",
    "00101": "t0",
    "00110": "t1",
    "00111": "t2",
    "01000": "s0",
    "01001": "s1",
    "01010": "a0",
    "01011": "a1",
    "01100": "a2",
    "01101": "a3",
    "01110": "a4",
    "01111": "a5",
    "10000": "a6",
    "10001": "a7",
    "10010": "s2",
    "10011": "s3",
    "10100": "s4",
    "10101": "s5",
    "10110": "s6",
    "10111": "s7",
    "11000": "s8",
    "11001": "s9",
    "11010": "s10",
    "11011": "s11",
    "11100": "t3",
    "11101": "t4",
    "11110": "t5",
    "11111": "t6"
}

dict_opcode_R = {
    "0110011": "add",
    "0110011": "sub",
    "0110011": "sll",
    "0110011": "slt",
    "0110011": "sltu",
    "0110011": "xor",
    "0110011": "srl",
    "0110011": "or",
    "0110011": "and"
}

dict_func3_R = {
    "000": "add",
    "000": "sub",
    "001": "sll",
    "010": "slt",
    "011": "sltu",
    "100": "xor",
    "101": "srl",
    "110": "or",
    "111": "and"
}

dict_func7_R = {
    "0000000": "add",
    "0100000": "sub",
    "0000000": "sll",
    "0000000": "slt",
    "0000000": "sltu",
    "0000000": "xor",
    "0000000": "srl",
    "0000000": "or",
    "0000000": "and"
}
dict_registers_content_decimal = {
    "zero":0,
    "ra": 0,
    "sp": 0,
    "gp": 0,
    "tp": 0,
    "t0": 0,
    "t1": 0,
    "t2": 0,
    "s0": 0,
    "fp": 0,
    "s1": 0,
    "a0": 0,
    "a1": 0,
    "a2": 0,
    "a3": 0,
    "a4": 0,
    "a5": 0,
    "a6": 0,
    "a7": 0,
    "s2": 0,
    "s3": 0,
    "s4": 0,
    "s5": 0,
    "s6": 0,
    "s7": 0,
    "s8": 0,
    "s9": 0,
    "s10":0,
    "s11":0,
    "t3": 0,
    "t4": 0,
    "t5": 0,
    "t6": 0
}

str = ""
opcode = ""
def decimal_to_binary(decimal, num_bits):
    # Convert absolute value of decimal to binary string
    if decimal < 0:
        positive_decimal = abs(decimal)
        # Invert bits
        inverted_binary_string = ''.join('1' if bit == '0' else '0' for bit in bin(positive_decimal)[2:].zfill(32))
        # Add 1 to the inverted bits to get two's complement
        twos_complement = bin(int(inverted_binary_string, 2) + 1)[2:].zfill(32)
        return twos_complement
    else:
        # Convert the positive decimal to binary string with 32 bits
        binary_string = bin(decimal)[2:].zfill(32)
        return binary_string


def binary_to_decimal(binary_string):
    # Check if the binary string represents a negative number
    if binary_string[0] == '1':
        # If the number is negative, convert it using two's complement
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary_string)
        decimal = -(int(inverted_binary, 2) + 1)
    else:
        # If the number is positive, convert it directly
        decimal = int(binary_string, 2)
    return decimal

temp_list = ["zero",
"ra",
"sp",
"gp",
"tp",
"t0",
"t1",
"t2",
"s0",
"s1",
"a0",
"a1",
"a2",
"a3",
"a4",
"a5",
"a6",
"a7",
"s2",
"s3",
"s4",
"s5",
"s6",
"s7",
"s8",
"s9",
"s10",
"s11",
"t3",
"t4",
"t5",
"t6"]


memory_map = {
    "0x00010000": 0,
    "0x00010004": 0,
    "0x00010008": 0,
    "0x0001000c": 0,
    "0x00010010": 0,
    "0x00010014": 0,
    "0x00010018": 0,
    "0x0001001c": 0,
    "0x00010020": 0,
    "0x00010024": 0,
    "0x00010028": 0,
    "0x0001002c": 0,
    "0x00010030": 0,
    "0x00010034": 0,
    "0x00010038": 0,
    "0x0001003c": 0,
    "0x00010040": 0,
    "0x00010044": 0,
    "0x00010048": 0,
    "0x0001004c": 0,
    "0x00010050": 0,
    "0x00010054": 0,
    "0x00010058": 0,
    "0x0001005c": 0,
    "0x00010060": 0,
    "0x00010064": 0,
    "0x00010068": 0,
    "0x0001006c": 0,
    "0x00010070": 0,
    "0x00010074": 0,
    "0x00010078": 0,
    "0x0001007c": 0
}

def decimal_to_hexadecimal(decimal_number):
    hexadecimal_string = hex(decimal_number)
    return hexadecimal_string

def S_type(instruction,pc):
    pc += 4
    keep_track[line] = False
    imme_1 = instruction[0:7]
    imme_2 = instruction[20:25]
    imme = imme_1 + imme_2
    ans = binary_to_decimal(imme)
    src_register = instruction[12:17]
    
    string_src_reg = dict_registers[src_register]
    value_src_reg = dict_registers_content_decimal[string_src_reg]
    final = ans+value_src_reg
    mem_address = decimal_to_hexadecimal(final)
    dest_registers = instruction[7:12]

    string_dest_register = dict_registers[dest_registers]
    value_dest_reg = dict_registers_content_decimal[string_dest_register]
    memory_map[mem_address] = value_dest_reg
    temp = (decimal_to_binary(pc,32))
    u.write("0b"+temp)
    for i in temp_list:
        u.write(" ")
        take = (decimal_to_binary(dict_registers_content_decimal[i],32))
        u.write("0b"+take)
    u.write("\n")
    return pc
    
def U_type(line,pc):
    pc += 4
    keep_track[line] = False
    opcode = line[25:32]
    imme = line[0:21]
    src_register = line[20:25]
    string_src_register = dict_registers[src_register]
    imme = imme + "0" * 12
    if(opcode == "0110111"):
        dict_registers_content_decimal[string_src_register] = binary_to_decimal(imme)
    else:
        dict_registers_content_decimal[string_src_register] = pc + binary_to_decimal(imme)
    temp = (decimal_to_binary(pc,32))
    u.write("0b"+temp)
    for i in temp_list:
        u.write(" ")
        take = (decimal_to_binary(dict_registers_content_decimal[i],32))
        u.write("0b"+take)
    u.write("\n")
    return pc

def bitwise_xor(decimal1, decimal2):
    # Perform bitwise XOR operation on decimal numbers
    result = decimal1 ^ decimal2
    return result

def do_worK(opcode,pick,pc):
    pc += 4
    keep_track[line] = False
    funtval = pick[17:20]
    instruction = dict_func3_R[funtval]
    instruction_1 = pick[0:7]
    if(instruction_1 == "0100000"):
        instruction = "sub"
    address_Register_1 = pick[12:17]
    address_Register_2 = pick[7:12]
    address_dest_regist = pick[20:25]
    string_register1 = dict_registers[address_Register_1]
    string_register2 = dict_registers[address_Register_2]
    string_dest_reg = dict_registers[address_dest_regist]
    value_reg1 = dict_registers_content_decimal[string_register1]
    value_reg2 = dict_registers_content_decimal[string_register2]
    value_dest_reg = dict_registers_content_decimal[string_dest_reg]
    if instruction == "add":
        value_dest_reg = value_reg1 + value_reg2
        dict_registers_content_decimal[string_dest_reg] = value_dest_reg

    elif instruction == "sub":
        value_dest_reg = value_reg1 - value_reg2
        dict_registers_content_decimal[string_dest_reg] = value_dest_reg

    elif instruction == "sll":
        temp_reg_2 = decimal_to_binary(value_reg2,32)
       
        ans = binary_to_decimal(temp_reg_2[28:32])
        value_dest_reg = value_reg1<<abs(ans)
        dict_registers_content_decimal[string_dest_reg] = value_dest_reg

    elif instruction == "slt":
        if(value_reg1 < value_reg2):
            value_dest_reg = 1
        dict_registers_content_decimal[string_dest_reg] = value_dest_reg

    elif instruction == "sltu":
        if(abs(value_reg1)< abs(value_reg2)):
            value_dest_reg = 1
        dict_registers_content_decimal[string_dest_reg] = value_dest_reg

    elif instruction == "xor":
        value_dest_reg = bitwise_xor(value_reg1,value_reg2)
        dict_registers_content_decimal[string_dest_reg] = value_dest_reg
       

    elif instruction == "srl":
        temp_reg_2 = decimal_to_binary(value_reg2,32)
        ans = binary_to_decimal(temp_reg_2[28:32])
        value_dest_reg = value_reg1>>abs(ans)
        dict_registers_content_decimal[string_dest_reg] = value_dest_reg
        

    elif instruction == "or":
        value_dest_reg = value_reg1 | value_reg2
        dict_registers_content_decimal[string_dest_reg] = value_dest_reg
       

    elif instruction == "and":
        value_dest_reg = value_reg1 & value_reg2
        dict_registers_content_decimal[string_dest_reg] = value_dest_reg
        
    
    temp = (decimal_to_binary(pc,32))
    u.write("0b"+temp)
    for i in temp_list:
        u.write(" ")
        take = (decimal_to_binary(dict_registers_content_decimal[i],32))
        u.write("0b"+take)
    u.write("\n")
    return pc

def J_type(line,pc):
    keep_track[line] = False
    imme = ""
    opcode = line[25:32]
    dest_reg = line[20:25]
    string_dest_reg = dict_registers[dest_reg]
    imme = imme + line[0]
    imme = imme + line[12:20]
    imme = imme + line[11]
    imme  = imme + line[1:11]
    imme = imme + "0"
    dict_registers_content_decimal[string_dest_reg] = pc + 4
    imme_bin = decimal_to_binary(pc,32)
    imme_bin = imme_bin[0:31]
    imme_bin += "0"
    pc = binary_to_decimal(imme_bin)
    pc += binary_to_decimal(sign_extend(imme))
    
    temp = (decimal_to_binary(pc,32))
    
    u.write("0b"+temp)
    for i in temp_list:
        u.write(" ")
        take = (decimal_to_binary(dict_registers_content_decimal[i],32))
        u.write("0b"+take)
    u.write("\n")
    return pc

                   
dict_func3_I = {
    "000": "addi",
    "000": "jalr",
    "010": "lw",
    "011": "sltiu",
}

dict_opcode_I = {
    "0000011": "lw",
    "0010011": "addi",
    "0010011": "sltiu",
    "1100111": "jalr",
}

def sign_extend(binary_num):
    # Check if the number is negative (if the first bit is 1)
    if binary_num[0] == '1':
        # If negative, sign-extend with 1s
        extended_num = '1' * (32 - len(binary_num)) + binary_num
    else:
        # If positive, sign-extend with 0s
        extended_num = '0' * (32 - len(binary_num)) + binary_num
    return extended_num

def I_type(line,pc,opcode):
    keep_track[line] = False
    pc += 4
    imme = line[0:12]
    funct3 = line[17:20]
    dest_reg = line[20:25]
    src_reg = line[12:17]
    string_dest_reg = dict_registers[dest_reg]
    string_src_reg = dict_registers[src_reg]
    sin_imme = sign_extend(imme)
    string_opcode = dict_opcode_I[opcode]
    if(funct3 == "010"):
        dict_registers_content_decimal[string_dest_reg] = memory_map[decimal_to_hexadecimal((dict_registers_content_decimal[string_src_reg] + binary_to_decimal(sin_imme)))]
        
    elif(funct3 == "000" and opcode == "0010011"):
        
        dict_registers_content_decimal[string_dest_reg] = dict_registers_content_decimal[string_src_reg] + binary_to_decimal(sin_imme)
        
    elif(funct3 == "011"):
        if(abs((dict_registers_content_decimal[string_src_reg])) < abs(binary_to_decimal(sin_imme))):
            dict_registers_content_decimal[string_dest_reg] = 1
    elif(funct3 == "000" and opcode == "1100111"):
        dict_registers_content_decimal[string_dest_reg] = pc + 4
        imme_bin = decimal_to_binary(pc,32)
        imme_bin = imme_bin[0:31]
        imme_bin += "0"
        pc = binary_to_decimal(imme_bin)
        pc = dict_registers_content_decimal[string_src_reg] + binary_to_decimal(sign_extend(imme))
    temp = (decimal_to_binary(pc,32))
    u.write("0b"+temp)
    for i in temp_list:
        u.write(" ")
        take = (decimal_to_binary(dict_registers_content_decimal[i],32))
        u.write("0b"+take)
    u.write("\n")
    return pc



def B_type(line,pc,opcode):
    temp = pc
    keep_track[line] = False
    imm_binary = ""
    imm_binary = imm_binary + line[0]
    imm_binary = imm_binary + line[24]
    imm_binary = imm_binary + line[1:7]
    imm_binary = imm_binary + line[20:24]
    imm_binary = imm_binary + "0"
    funt3 = line[17:20]
    src_reg_1 = line[12:17]
    src_reg_2 = line[7:12]
    string_src_1 = dict_registers[src_reg_1]
    string_src_2 = dict_registers[src_reg_2]
    if(dict_registers_content_decimal[string_src_1] == dict_registers_content_decimal[string_src_2]):
        temp += (binary_to_decimal(sign_extend(imm_binary)))
        
    elif(dict_registers_content_decimal[string_src_1] != dict_registers_content_decimal[string_src_2]):
        temp += (binary_to_decimal(sign_extend(imm_binary)))
    elif(dict_registers_content_decimal[string_src_1] >= dict_registers_content_decimal[string_src_2]):
        temp += (binary_to_decimal(sign_extend(imm_binary)))
    elif(abs(dict_registers_content_decimal[string_src_1]) >= abs(dict_registers_content_decimal[string_src_2])):
        temp += (binary_to_decimal(sign_extend(imm_binary)))
    elif(dict_registers_content_decimal[string_src_1] < dict_registers_content_decimal[string_src_2]):
        temp += (binary_to_decimal(sign_extend(imm_binary)))
    elif(abs(dict_registers_content_decimal[string_src_1] ) < abs(dict_registers_content_decimal[string_src_2])):
        temp += (binary_to_decimal(sign_extend(imm_binary)))
    if(temp == pc):
        temp += 4
    pc = temp
    
    temp = (decimal_to_binary(pc,32))
    u.write("0b"+temp)
    for i in temp_list:
        u.write(" ")
        take = (decimal_to_binary(dict_registers_content_decimal[i],32))
        u.write("0b"+take)
    u.write("\n")
    return pc


def special_case(opcode,line,pc):
    keep_track[line] = False
    pc += 4
    funct3 = line[17:20]
    src_reg_1 = line[12:17]
    src_reg_2 = line[7:12]
    dest_reg = line[20:25]
    string_src_reg_1 = dict_registers[src_reg_1]
    string_src_reg_2 = dict_registers[src_reg_2]
    string_dest_reg = dict_registers[dest_reg]
    if(funct3 == "000"):
        get_val = dict_registers_content_decimal[string_src_reg_1] * dict_registers_content_decimal[string_src_reg_2]
        string_val = decimal_to_binary(get_val,32)
        real_val = binary_to_decimal(get_val)
        dict_registers_content_decimal[string_dest_reg] = real_val
    elif(funct3 == "001"):
        for i in temp_list:
            dict_registers_content_decimal[i] = 0
    elif(funct3 == "010"):
        exit(0)
    elif(funct3 == "011"):
        src_con = dict_registers_content_decimal[string_src_reg_1]
        dest_con = dict_registers_content_decimal[string_dest_reg]
        dict_registers_content_decimal[string_dest_reg] = src_con
        dict_registers_content_decimal[string_src_reg_1] = dest_con
    temp = (decimal_to_binary(pc*4,32))
    u.write("0b"+temp)
    for i in temp_list:
        u.write(" ")
        take = (decimal_to_binary(dict_registers_content_decimal[i],32))
        u.write("0b"+take)
    u.write("\n")
    return pc
keep_track = {}

line_list = []
with open("take.txt", "r") as file:
    
    for line in file:
        if(line != '\n'):
            line_list.append(line)
            keep_track[line] = True
pc = 0
for i in range(len(line_list)):
    line = line_list[pc//4]
    
    opcode = line[25:32]
    if(opcode == "0100011" and keep_track[line]):
        pc = S_type(line,pc)
    elif(opcode == "0110011" and keep_track[line]):
        pc = do_worK(opcode,line,pc)
    elif (opcode == "0010111" or opcode == "0110111"and keep_track[line]):
        pc = U_type(line,pc)
    elif(opcode == "1101111"):
        pc = J_type(line,pc)
    elif(opcode == "0000011" or opcode == "0010011" or opcode == "1100111" and keep_track[line]):
        pc = I_type(line,pc,opcode)
    elif(opcode == "1100011" and keep_track[line]):
        pc = B_type(line,pc,opcode)
    elif(opcode == "1101111" ):
        pc = special_case(opcode,line,pc)

for i in memory_map:
    address = i 
    address_val  = decimal_to_binary(memory_map[i],32)
    u.write(address + " " + address_val)
    u.write("\n")
u.close()
