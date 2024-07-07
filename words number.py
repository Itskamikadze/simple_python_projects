#words number

numbers = {
    0:"Zero", 1: "One", 2: "Two", 3: "Three",
    4: "Four", 5: "Five", 6: 'Six',
    7: "Seven", 8: "Eight", 9: "Nine",
    10: "Ten", 11: "Eleven", 12: "Twelve",
    13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
    16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
    19: "Nineteen", 20: "Twenty", 30: "Thirty",
    40: "Fourty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
    80: "Eighty", 90: "Ninety", 100: "Hundred", 1000: "Thousand",
    1000000: "Million",
}

def one_num(num):
    num = int(num)
    # check if number is exact with the num in dictionary
    if num in numbers.keys():
        return numbers[num]

def two_nums(num):
    
    wrote = ""
    # the exact num will display
    num = int(num)
    # if num < 9
    if num <= 20 or num % 10 == 0:
        return numbers[num]
    # if we have more than 20
    if num % 10 > 0:
        wrote += numbers[(num//10)*10] + "-" + numbers[num%10]
    return wrote

        
def three_nums(num):
    
    
    wrote = ""
    num = int(num)
    if num % 100 == 0:
        wrote += numbers[num//100] + " " + numbers[100]
    elif num % 100 > 0:
        wrote += numbers[num//100] + " " + numbers[100] + " "
        num %= 100
        wrote += two_nums(num)
    return wrote

def four_nums(num):
    
    num = int(num)
    num1 = num
    wrote = " "
    if num % 1000 == 0:
        wrote += numbers[num//1000] + " " + numbers[1000]
    elif num % 1000 > 0:
        wrote += numbers[num//1000] + " " + numbers[1000] + " "
        num1 %= 1000
        if len(str(num1)) == 1:
            wrote += one_num(num1)
        elif len(str(num1)) == 2:
            wrote += two_nums(num1)
        else:
            wrote += three_nums(num)
    return wrote

def five_nums(num):

    num = int(num)
    wrote = " "
    #save original value before divided
    num1 = num
    #if value equal to 0
    if num % 10000 == 0:
        wrote += numbers[num] + " " + numbers[1000] + " "
    #if value more than 0
    elif num %10000 > 0:
        num //= 1000
        wrote += two_nums(num) + " " + numbers[1000] + " "
        num1 %= 1000
        if len(str(num1)) == 1:
            wrote += one_num(num1)
        elif len(str(num1)) == 2:
            wrote += two_nums(num1)
        else:
            wrote += three_nums(num1)
    return wrote

def six_nums(num):

    num = int(num)
    wrote = " "

    #save original value before divided
    num1 = num
    #if value equal to 0
    if num % 100000 == 0:
        num //= 1000
        wrote += three_nums(num) + " " + numbers[1000]
    else:
        num //= 1000
        wrote += three_nums(num) + " " + numbers[1000] + " "
        num1 %= 1000
        if len(str(num1)) == 1:
            wrote += one_num(num1)
        elif len(str(num1)) == 2:
            wrote += two_nums(num1)
        else:
            wrote += three_nums(num1)
    return wrote

def seven_nums(num):
    
    num = int(num)
    num1 = num
    wrote = " "

    if num % 1000000 == 0:
        num //= 1000000
        wrote += one_num(num) + " Million"
    else:
        num //= 1000000
        wrote += one_num(num) + " Million "
        num1 %= 1000000
        if len(str(num1)) == 1:
            wrote += one_num(num1)
        elif len(str(num1)) == 2:
            wrote += two_nums(num1)
        elif len(str(num1)) == 3:
            wrote += three_nums(num1)
        elif len(str(num1)) == 4:
            print(len(str(num1)))
            wrote += four_nums(num1)
        elif len(str(num1)) == 5:
            wrote += five_nums(num1)
        else:    
            wrote += six_nums(num1)
    return wrote
    
    

    
    

if __name__ == "__main__":
    number = input("Please provide a value: ")
    if len(number) == 1:
        print(one_num(number))
    if len(number) == 2:
        print(two_nums(number))
    elif len(number) == 3:
        print(three_nums(number))
    elif len(number) == 4:
        print(four_nums(number))
    elif len(number) == 5:
        print(five_nums(number))
    elif len(number) == 6:
        print(six_nums(number))
    elif len(number) == 7:
        print(seven_nums(number))

