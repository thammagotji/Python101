# create a function that converts decimal to binary base-2, octal base-8,
# and hexadecimal base-16, and vice versa.

def converter(number,typ):
    if typ==1:                          # input decimal
        deci = int(number)
        bi = bin(deci)[2:]
        octal = oct(deci)[2:]
        hexad = hex(deci)[2:]
        print("-----converting decimal-----")
        print("decimal: ",deci)
        print("binary: ",bi)
        print("octal: ",octal)
        print("hexadecimal: ",hexad)
    elif typ==2:                        # input binary
        deci = int(str(number),2)
        bi = int(number)
        octal = oct(deci)[2:]
        hexad = hex(deci)[2:]
        print("-----converting binary-----")
        print("decimal: ",deci)
        print("binary: ",bi)
        print("octal: ",octal)
        print("hexadecimal: ",hexad)
    elif typ==3:                        # input octal
        deci = int(str(number),8)
        bi = bin(deci)[2:]
        octal = int(number)
        hexad = hex(deci)[2:]
        print("-----converting octal-----")
        print("decimal: ",deci)
        print("binary: ",bi)
        print("octal: ",octal)
        print("hexadecimal: ",hexad)
    elif typ==4:                        # input hexadecimal
        deci = int(str(number),16)
        bi = bin(deci)[2:]
        octal = oct(deci)[2:]
        hexad = int(deci)
        print("-----converting hexadecimal-----")
        print("decimal: ",deci)
        print("binary: ",bi)
        print("octal: ",octal)
        print("hexadecimal: ",hexad)
    else:
        print("-----ERROR!-----")

converter("2566",1)
converter("1011001010",2)
converter("4567",3)
converter("1a4f",4)
converter("1a4f",5)         # test converter function
