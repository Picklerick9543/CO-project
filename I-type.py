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
    "lw" :"0000011",
    "addi":"0010011",
    "sltiu":"0010011",
    "jalr":"1100111"
}

dict_func3 = {
    "lw" :"010",
    "addi":"000",
    "sltiu":"011",
    "jalr":"000"
}

i = 0
with open("first.txt",'r+') as f:
    for line in f:
        i += 1
        if line == " ":
            print(f"Error : line {i} has empty line.")
            continue
        if not line.strip():
            continue
        ln = line.split()
        if len(ln)<2:
            print(f"Error: line {i} has syntax error.")
            break
        take = ln[1].split(',')
        m = 1
        if ',' not in line:
            print(f"Error: line {i} has syntax error.")
            break
        for j in take:
            if m == 1:
                ln[1] = j
            else:
                ln.append(j)
            m += 1
        
        
        opcode = ln[0]
        if opcode not in dict_opcode:
            print(f"Error line {i} : Opcode '{opcode}' is not recoginised. ")
            break
        n = ''
        register = ""
        if opcode == 'lw':
            j = 0
            for s in ln[2]:
                if s == "(":
                    register = ln[2][j + 1: len(ln[2])-1]
                    break
                else:
                    n += s
                j += 1
            if(len(take)<2) :
                print(f"Error : line {i} have something syntax issue.")
                break
            if register == '':
                print(f"Error line : {i} has syntax error.")
                break
        else:
            if(len(take)<3) :
                print(f"Error : line {i} have something syntax issue.")
                break
            n = ln[3]
            register = ln[2]
            
        dest_reg = ln[1]
  

        try:
            n = int(n)
        except:
            print(f"Error : line {i} immediate value is not integer or not provided.")
            break
        if dest_reg  not in dict_registers:
            print(f"Error line {i} : destination Register '{dest_reg}' is not recoginised")
            break
        if register not in dict_registers:
            print(f"Error line {i} : Register '{register}' is not recoginised")
            break
        def imm(n):
            binary = ''
            if int(n) == 0:
                return '0' * 11
            elif int(n) < 0:
                return(imm(2**11 + n)[2:])
            else:
                while(n>0):
                    binary=str(n%2) + binary
                    n= n//2
                return binary.zfill(11)
        value = imm(int(n))
        
        immediate = ''
        if(int(n)<0):
            value = value.zfill(11)
            k = 0
            while value[k] != '1':
                immediate += '1'
                k+=1
            immediate  += value[k:len(value)]
        else:
            immediate = value  
                
        x = immediate +" "+ dict_registers[register] +" "+ dict_func3[opcode] +" "+ dict_registers[dest_reg] +" "+ dict_opcode[opcode]
        print(x)
        
    f.close()

        
        



