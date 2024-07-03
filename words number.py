#words number

words_number = {
    1: "One", 2: "Two", 3: "Three",
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


def number_under_20(num):

    #if number don't exceed 20
    if num <= 20:
        num_lst = [words_number[num] for x in words_number.keys() if x == num and x <= 20]
        return num_lst[0]
    
    
def number_above_20(num):

    wrote = ""
    
    num1 = num - (num % 10)
    num2 = num % 10
    if num1 in words_number.keys() and num2 in words_number.keys():
        wrote += words_number[num1] + "-" + words_number[num2]
        return wrote
    


    
def three_digits(num):
     
    num1 = 0
    wrote = ""
    h = words_number[100]
    

    # read a first digit of 3-digit value
    if num % 100 == 0:
        wrote += words_number[num // 100] + " " + h
    # read all value from dict if digit have less than 20
    elif num % 100 <= 20:
        num1 = num %100
        wrote += words_number[num // 100] + " " + h + " " + number_under_20(num1)
    else:
        num1 = num %100
        wrote += words_number[num // 100] + " " + h + " " + number_above_20(num1)
    return wrote

def four_digits(num):

    num1 = num %1000
    wrote = ""
    t = words_number[1000]
    # read one thousand
    if num % 1000 == 0:
        wrote += words_number[num // 1000] + " " + t
    # read thousand with value less than 20
    elif num % 1000 <= 20:
        wrote += words_number[num // 1000] + " " + t + " " + number_under_20(num1)
    elif num % 1000 > 20 and num % 1000 <= 99 :
        wrote += words_number[num // 1000] + " " + t + " " + number_above_20(num1)
    else:
        #make double += (before and after thousand)
        wrote += words_number[num // 1000]
        num %= 1000
        wrote += " " + t + " " + three_digits(num1)
    return wrote

def five_digits(num):
    num1 = num %1000
    num2 = num %10000
    t = words_number[1000]
    
    wrote = ""

    # if value have exactly 10 000
    if num2 == 0:
        wrote += words_number[num // 1000] + " " + t
    elif num2 <= 20:
        if words_number[num // 1000] <= 20:
            wrote += number_under_20(num1) + " "
            num //= 10
            wrote += four_digits(num1)
        elif words_number[num // 1000] > 20 and words_number[num // 1000] <= 99:
            wrote += number_above_20(num1) + " "
            num //= 10
            wrote += four_digits(num1)
    elif num2 > 20 and num2 <= 99:
        if words_number[num // 1000] <= 20:
            wrote += number_under_20(num1) + " "
            num //= 10
            wrote += four_digits(num1)
        elif words_number[num // 1000] > 20 and words_number[num // 1000] <= 99:
            wrote += number_above_20(num1) + " "
            num //= 10
            wrote += four_digits(num1)
    return wrote
    

    
    

def show_number():

    numbers = input("please enter the number from 1 to 1 000 000 000: ")
    if numbers.isdigit():
        numbers = int(numbers)
        if numbers <= 20:
            print(number_under_20(numbers))
        elif numbers > 20 and len(str(numbers)) == 2:
            print(number_above_20(numbers))
        elif len(str(numbers)) == 3:
            print(three_digits(numbers))
        elif len(str(numbers)) == 4:
            print(four_digits(numbers))
        elif len(str(numbers)) == 5:
            print(four_digits(numbers))
    else:
        print("Put a correct value!")
    
show_number()

