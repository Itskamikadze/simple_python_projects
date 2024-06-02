#make a Caesar Cipher

def encrypt(text, shift):
    global result
    result = ""
    
    for x in range(len(text)):
        z = chr(ord(text[x])+shift)
        result += z
    return result
                  

def decrypt():

    result_2 = ""
    for x in range(len(result)):
        z = chr(ord(result[x])-shift)

        result_2 += z
    return result_2


if __name__ == "__main__":
    text = input("Please put a text to Caesar Cipher: ")
    shift = int(input("Please enter the number of shifts in the text: "))
    print("The number of shifts: ", shift) 
    print("Encrpyted password is: ", encrypt(text, shift))
    print("Decrypted password is: ", decrypt())