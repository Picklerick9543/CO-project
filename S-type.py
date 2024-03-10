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

dict_opcode = {
    "sw":"0100011"
}

dict_func3 = {
    "sw":"010"
}

with open("first.txt",'r+') as f:
    i = 0
    for line in f:
        if line == '':
            print(f"Error: line {i} is empty.")
            continue
        i += 1
        if not line.strip():
            continue
        if ',' not in line:
            print(f"Error: line {i} contains syntax error.")
            break
        ln = line.split()
        if len(ln)<2:
            print(f"Error : line {i} has syntax error.")
            break
        take = ln[1].split(',')
        register = ''
        j = 0
        n = ''
        ln.insert(1,take[0])
        
        for s in take[1]:
            if s == "(":
                register = take[1][j + 1: len(take[1])-1]
                break
            else:
                n += s
            j += 1
        take[0],take[1] = register,n
        
        if register == '':
            print(f"Error line {i} has syntax error.")
            break
        try:
            n = int(n)
        except:
            print(f"Error line {i}: immediate value is not integer.")
            break
        if len(take)<2:
            print(f"Error line {i} has syntax error.")
            break
        if register not in dict_registers:
            print(f"Error line {i} has {register} unathourised register.")
            break
        m = 1
        for j in take:
            if m == 1:
                ln[2] = j
            else:
                ln.append(j)
            m += 1
        
        dest_reg = ln[1]
        if dest_reg not in dict_registers:
            print(f"Error : line {i} has {dest_reg} unathourised destination register.")
            break
        opcode = ln[0]
        if opcode not in dict_opcode:
            print(f"Error : line {i} has syntax error.")
            break
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
        
        x = str(value)[0:7] +" "+ dict_registers[dest_reg] +" "+dict_registers[register]+" "+dict_func3[opcode]+" "+str(value)[7:]+" "+dict_opcode[opcode]
        print(x)
    f.close()