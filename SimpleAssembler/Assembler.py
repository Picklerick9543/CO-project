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
    
dict_opcode_R={
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

dict_func3_R={
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

dict_func7_R={
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

dict_opcode_I = {
    "lw" :"0000011",
    "addi":"0010011",
    "sltiu":"0010011",
    "jalr":"1100111"
}

dict_func3_I = {
    "lw" :"010",
    "addi":"000",
    "sltiu":"011",
    "jalr":"000"
}

dict_opcode_J = {
    "jal":"1101111"
}

dict_opcode_S = {
    "sw":"0100011"
}

dict_func3_S = {
    "sw":"010"
}

dict_opcode_B ={
    # B-type 
    "beq":"1100011",
    "bne":"1100011",
    "blt":"1100011",
    "bge":"1100011",
    "bltu":"1100011",
    "bgeu":"1100011",
}

dict_func3_B ={
    # B-type
    "beq":"000",
    "bne":"001",
    "blt":"100",
    "bge":"101",
    "bltu":"110",
    "bgeu":"111",
}

dict_opcode_U = {
    "lui": "0110111",
    "auipc": "0010111" 
}
with open("first.txt",'r+') as n:
    list_create = n.readlines()
    
    if( list_create == [] or list_create == ['\n']):
        with open("output.txt",'w+') as m:
            m.write(f"Error : Empty file is given.")
        m.close()
        exit(0)
n.close()

i = 0
with open("first.txt",'r+') as k:
    list_make = list()
    for lines in k:
        take = lines.split()
        
        list_make.append(take)
        
    e = len(list_make)
    
    if(list_make[e-1][0] != 'beq'):
        with open("output.txt",'w') as m:
            m.write(f"Error : Halt instruction is not provided at end of code.")
        m.close()
        exit(0)
    
    s = 0
    while(s<e):
        if list_make[s] == []:
            s += 1
        elif s != e-1 and list_make[s][0] == 'beq' and list_make[s][1] == 'zero':
            
            with open("output.txt",'w') as m:
                m.write(f"Error :Halt instruction is provided at middle of code.")
            m.close()
            exit(0)
        else:
            s += 1

u = open("output.txt",'w+')
f = open("first.txt","r+")

def code_R(line):
    try:
        instruction = line[0]
        registers = line[1]
        dest_reg = registers.split(",")[0].strip()
        src_reg1 = registers.split(",")[1].strip()
        src_reg2 = registers.split(",")[2].strip()
    except:
       
        u.close()
        with open("output.txt",'w') as m:
            m.write(f"Error : line {i} has syntax error.")
        m.close()
        exit(0)

    if dest_reg == " " or src_reg1 == " " or src_reg2 == " ":
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error: line {i} has syntax error.")
        m.close()
        exit(0)
    if instruction not in dict_func7_R :
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error: Instruction {instruction} is not recognized.")
        m.close()
        exit(0)
    if dest_reg not in dict_registers or src_reg1 not in dict_registers or src_reg2 not in  dict_registers:
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error: Register(s) {dest_reg}, {src_reg1}, {src_reg2} is/are not recognized.")
        m.close()
        exit(0)
    x = dict_func7_R[instruction] + " " + dict_registers[src_reg2] + " " + dict_registers[src_reg1] + " " + dict_func3_R[instruction] + " " + dict_registers[dest_reg] + " " + dict_opcode_R[instruction]

    u.write(str(x)+'\n')   
        
        
    
    
        


def code_I(line):
    take = line[1].split(',')
  
    if ',' not in line[1]:        
        u.close()
        with open("output.txt",'w+') as m:
            m.write(f"Error : line {i} has syntax error.")
        m.close()
        exit(0)
    m = 1
    for j in take:
        if m == 1:
            line[1] = j
        else:
            line.append(j)
        m += 1
    
    
    opcode = line[0]
  
    n = ''
    register = ""
    if opcode == 'lw':
        j = 0
        for s in take[1]:
            if s == "(":
                register = take[1][j + 1 : len(take[1])-1]
                break
            else:
                n += s
            j += 1
    else:
        if(len(take)<3) :
            u.close()
            with open("output.txt",'w+') as m:
                m.write(f"Error : line {i} has syntax error.")
            m.close()
            exit(0)
        n = take[2]
        register = take[1]
    if register == '':
        u.close()
        with open("output.txt",'w+') as m:
            m.write(f"Error : line {i} has syntax error.")
        m.close()
    
        exit(0)
    dest_reg = take[0]
  
    try:
        n = int(n)
    except:
        
        u.close()
        with open("output.txt",'w+') as m:
            m.write(f"Error : line {i} immediate value is not integer or not provided.")
        m.close()
        exit(0)
    if dest_reg  not in dict_registers:
       
        u.close()
        with open("output.txt",'w+') as m:
            m.write(f"Error line {i} : destination Register '{dest_reg}' is not recoginised")
        m.close()
        exit(0)
    if register not in dict_registers:
        
        u.close()
        with open("output.txt",'w+') as m:
            m.write(f"Error line {i} : Register '{register}' is not recoginised")
        m.close()
        exit(0)
    def imm(n):
        binary = ''
        if int(n) == 0:
            return '0' * 12
        elif int(n) < 0:
            return(imm(2**12 + n)[:])
        else:
            while(n>0):
                binary=str(n%2) + binary
                n= n//2
            return binary.zfill(12)
    value = 0
    if int(n) >= (-525288) and int(n) <= 524287:
        value = (imm(n))
        
    else:
        
        u.close()
        with open("output.txt",'w+') as m:
            m.write(f"Erro: line {i} immediate value is out of range.")
        m.close()
        exit(0)
    
    immediate = value

    x = immediate +" "+ dict_registers[register] +" "+ dict_func3_I[opcode] +" "+ dict_registers[dest_reg] +" "+ dict_opcode_I[opcode]
    u.write(str(x)+'\n')
    

def code_S(line):
    if ',' not in line[1]:
        u.close()
        with open("output.txt",'w') as m:
            m.write(f"Error: line {i} contains syntax error.")
        m.close()
        exit(0)
    if len(line)<2:
        u.close()
        with open("output.txt",'w') as m:
            m.write(f"Error : line {i} has syntax error.")
        m.close()
        exit(0)
    take = line[1].split(',')
    register = ''
    j = 0
    n = ''
    line.insert(1,take[0])
    
    for s in take[1]:
        if s == "(":
            register = take[1][j + 1: len(take[1])-1]
            break
        else:
            n += s
        j += 1
    take[0],take[1] = register,n
    
    if register == '':
        u.close()
        with open("output.txt",'w') as m:
            m.write(f"Error line {i} has syntax error.")
        m.close()
        exit(0)
    try:
        n = int(n)
    except:
        u.close()
        with open("output.txt",'w') as m:
            m.write(f"Error line {i}: immediate value is not integer.")
        m.close()
        exit(0)
    if len(take)<2:
        u.close()
        with open("output.txt",'w') as m:
            m.write(f"Error line {i} has syntax error.")
        m.close()
        exit(0)
    if register not in dict_registers:
        u.close()
        with open("output.txt",'w') as m:
            m.write(f"Error line {i} has {register} unathourised register.")
        m.close()
        exit(0)
    m = 1
    for j in take:
        if m == 1:
            line[2] = j
        else:
            line.append(j)
        m += 1
    
    dest_reg = line[1]
    if dest_reg not in dict_registers:
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error : line {i} has {dest_reg} unathourised destinationregister.")
        m.close()
        exit(0)
    opcode = line[0]
    if opcode not in dict_opcode_S:
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error : line {i} has syntax error.")
        m.close()
        exit(0)
    def imm(n):
        binary = ''
        if int(n) == 0:
            return '0' * 12
        elif int(n) < 0:
            return(imm(2**12 + n)[:])
        else:
            while(n>0):
                binary=str(n%2) + binary
                n= n//2
            return binary.zfill(12)
    value = imm(n)
    
    x = str(value)[0:7] +" "+ dict_registers[dest_reg] +" "+dict_registers[register]+" "+dict_func3_S[opcode]+" "+str(value)[7:]+" "+dict_opcode_S[opcode]
    u.write(str(x)+'\n')

def code_J(line):


    take = line[1].split(',')  
    if ',' not in line[1]:
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error: line {i} contains syntax error.")
        m.close()
        exit(0)
    
    if len(line)<2:
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error: line {i} has syntax error.")
        m.close()
        exit(0)
    
    m = 1
    for j in take:
        if m == 1:
            line[1] = j
        else:
            line.append(j)
        m += 1
    
    register = line[1]
    if register not in dict_registers:
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error line {i} has unathuorised register.")
        m.close()
        exit(0)
    
    opcode = line[0]
    if line[2] == '':
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error: line {i} has no label or immediate value.")
        m.close()
        exit(0)
        
    n = ''
    try:
        n = int(line[2])
    except:
        for s in line[2]:
            if s == '(':
                break
            else:
                n += s
    n = int(n)
    if opcode not in dict_opcode_J:
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error line {i} : Opcode '{opcode}' is not recognised.")
        m.close()
        exit(0)
    
    def imm(n):
        
        if i > 980:
            return '0'
        binary = ''
        if n == 0:
            return '0' * 20
        elif n < 0:
            return imm(2**20 + n)[:]
        else:
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            return binary.zfill(20)
    value = 0
    if int(n) >= (-525288) and int(n) <= 524287:
        value = str(imm(n))
    else:
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Erro: line {i} immediate value is out of range.")
        m.close()
        exit(0)
    
    new_value = value[0]+value[9:19]+ value[9] + value[1:9]
    x = new_value +" "+ dict_registers[register] +" "+ dict_opcode_J[opcode]
    u.write(str(x) + '\n')

def code_U(line):
    if ',' not in line[1]:
        u.close()
        with open("output.txt","r+") as m:
            m.write(f"Error :line {i} has syntax error. ")
        m.close()
        exit(0)
    a = line[1].split(',')
    instruction = line[0]
    register = a[0]
    immediate = a[1]

    
    if register == '':
     
        u.close()
        with open("output.txt","r+") as m:
            m.write(f"Error line {i} has syntax error. ")
        m.close()
        exit(0)
    if instruction not in dict_opcode_U:
        
        u.close()
        with open("output.txt","r+") as m:
            m.write(f"Error : line {i} instruction not recognised.")
        m.close()
        exit(0)
    if register not in dict_registers:
        print(f"Error: Register '{register}' is not recognised")
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error  : line {i} Register is not recognised.")
        m.close()
        exit(0)
    
    n= immediate
    
    try:
        n = int(immediate)
    except:
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error : line {i} immediate value is not integer or not provided. ")
        m.close()
        exit(0)

    
    value = 0
    
    def imm(n):
        binary = ''
        if int(n) == 0:
            return '0' * 32
        elif int(n) < 0:
            return(imm(2**32 + n)[:])
        else:
            while(n>0):
                binary=str(n%2) + binary
                n= n//2
            return binary.zfill(32)

    if int(n) >= (-1048576) and int(n) <= 1048575:
        value = (imm(n))
        
    else:
        u.close()
        with open("output.txt","r+") as m:
            m.write(f"Error: line {i} immediate value is out of range.")
        m.close()
        exit(0)
    x = str(value)[0:20] +" "+ dict_registers[register] + " "+dict_opcode_U[instruction] 
    
    u.write(str(x)+'\n')

def code_B(line):
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

    instruction = line[0]
    registers = line[1]

    dest_reg = registers.split(",")[0].strip()
    src_reg1 = registers.split(",")[1].strip()
    label = registers.split(",")[2].strip()

    label=int(label)

    if instruction not in dict_func3_B :
       
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error: Instruction {instruction} is not recognized.")
        m.close()
        exit(0)

    if dest_reg not in dict_registers or src_reg1 not in dict_registers :
        u.close()
        with open("output.txt",'r+') as m:
            m.write(f"Error: Register(s) {dest_reg}, {src_reg1} is/are not recognized.")
        m.close()
        exit(0)
    x=immediate1(label)[:7] + ' ' + dict_registers[src_reg1] + ' ' + dict_registers[dest_reg] + ' ' + dict_func3_B[instruction]+' ' + immediate1(label)[7:] + ' ' + dict_opcode_B[instruction]

    u.write(str(x)+'\n')

    







for lines in f:

    i +=1

    if not lines.strip():  
        continue
    list_create = lines.split( )
    if len(list_create)<2:
        u.close()
        with open("output.txt",'w') as m:
            m.write(f"Error: line '{i}' has syntax error.")
        m.close()
        break
    take_create = list_create[1].split(',')
    if list_create[0] == 'beq' and take_create[1] == 'zero':
        break
    if list_create[0] in dict_opcode_R:
        code_R(list_create)
    elif list_create[0] in dict_opcode_I:
        code_I(list_create)
    elif list_create[0] in dict_opcode_B:
        code_B(list_create)
    elif list_create[0] in dict_opcode_J:
        code_J(list_create)
    elif list_create[0] in dict_opcode_S:
        code_S(list_create)
    elif list_create[0] in dict_opcode_U:
        code_U(list_create)
    else:
        u.close()
        with open("output.txt",'w') as m:
            m.write(f"Error: line '{i}' Instruction {list_create[0]} is not recognized.")
        m.close()
        break
f.close()
u.close()
