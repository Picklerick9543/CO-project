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

dict_opcode= {
    "lui": "0110111",
    "auipc": "0010111" 
}
def imm(n):
    binary = ''
    if n == 0:
        return '0' * 20
    elif n < 0:
        return(imm(2**20 + n)[2:])
    else:
        while(n>0):
            binary=str(n%2) + binary
            n= n//2
        return binary.zfill(20)

i = 0
fhand = open("hello.txt",'r')
for line in fhand:
    i+=1
    if not line.strip():
        continue
    a = line.split()
    if (len(a)<2):
        print(f"Error: line {i} doesn't contain the instruction and register.")
        break
    instruction = a[0]
    register = a[1]
    dest_reg = register.split(',')[0].strip()
    immediate = int(register.split(',')[1].strip())
    # src_reg1 = register.split(',')[1].strip()
    # src_reg2 = register.split(',')[2].strip()

    if instruction not in dict_opcode:
        print(f"instruction '{instruction}' not recognised.")
        break
    if dest_reg not in dict_reg:
        print(f"Error: Register '{dest_reg}' is not recognised")
        break
    x = imm(immediate) + dict_reg[dest_reg] + dict_opcode[instruction] 
    print(x)
fhand.close()










