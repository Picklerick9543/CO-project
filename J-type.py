dict_reg={
    "zero":"00000",
    "ra":"00001",
    "sp":"00010",
    "gp":"00011",
    "tp":"00100",
    "t0":"00101",
    "t1":"00110",
    "t2":"00111",
    "s0":"01000",
    "fp":"01000",
    "s1":"01001",
    "a0":"01010",
    "a1":"01011",
    "a2":"01100",
    "a3":"01101",
    "a4":"01110",
    "a5":"01111",
    "a6":"10000",
    "a7":"10001",
    "s2":"10010",
    "s3":"10011",
    "s4":"10100",
    "s5":"10101",
    "s6":"10110",
    "s7":"10111",
    "s8":"11000",
    "s9":"11001",
    "s10":"11010",
    "s11":"11011",
    "t3":"11100",
    "t4":"11101",
    "t5":"11110",
    "t6":"11111"
}

dict_opcode = {
    "jal":"1101111"
}

with open("first.txt",'r+') as f:
    i = 0
    for line in f:
        i += 1
        if not line.strip():
            continue
        if ',' not in line:
            print(f"Error: line {i} contains syntax error.")
            break
        ln = line.split()
        if len(ln)<2:
            print(f"Error: line {i} has syntax error.")
            break
        take = ln[1].split(',')
        m = 1
        for j in take:
            if m == 1:
                ln[1] = j
            else:
                ln.append(j)
            m += 1
        
        register = ln[1]
        if register not in dict_reg:
            print(f"Error line {i} has unathuorised register.")
            break
        
        opcode = ln[0]
        if ln[2] == '':
            print(f"Error: line {i} has no label or immediate value.")
            break
        
        try:
            n = int(ln[2])
        except:
            print(f"Error line {i} : immediate value is not integer.")
            break
        if opcode not in dict_opcode:
            print(f"Error line {i} : Opcode '{opcode}' is not recognised.")
        def imm(n):
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

        
        value = str(imm(n))
        new_value = value[0]+value[9:19]+ value[9] + value[1:9]
        x = new_value +" "+ dict_reg[register] +" "+ dict_opcode[opcode]
        print(x)

    
    f.close()

