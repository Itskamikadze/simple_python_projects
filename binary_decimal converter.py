class Converter:
    
    def bin_to_dec(self):   
        while True:     
            try:
                result = ""
                conv_bin = input("Please put a decimal value: ")
                conv_bin = int(conv_bin)
                while conv_bin > 0:
                    if conv_bin % 2 == 0:
                        result = result + "0"
                    elif conv_bin % 2 == 1:
                        result = result + "1"
                    conv_bin //= 2
                return result[::-1]
            except ValueError:
                print('Please put a correct value!')

    def dec_to_bin(self):
        while True:
            try:
                result = 0
                conv_dec = input("Put a binary value: ")
                conv_dec = int(conv_dec)
                l = len(str(conv_dec)) - 1
                for x in str(int(conv_dec)):
                    result += int(x) * pow(2, l)
                    l -= 1
                return result
            except ValueError:
                print("Put a correct value!")
    
    


if __name__ == "__main__":
    
    conv = Converter()
    print("Converted binary value from decimal is: ", conv.bin_to_dec())
    print("Converted decimal value from binary is: ", conv.dec_to_bin())