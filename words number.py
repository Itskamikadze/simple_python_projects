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
    


    
def count_numbers(num):
     
    num1 = 0
    wrote = ""

    # read a first digit of 3-digit value
    if len(str(num)) == 3:
        h = words_number[100]
        if num % 100 == 0:
            wrote += words_number[num // 100] + " " + h
        elif num % 100 <= 20:
            num1 = num %100
            wrote += words_number[num // 100] + " " + h + " " + number_under_20(num1)
        else:
            num1 = num %100
            wrote += words_number[num // 100] + " " + h + " " + number_above_20(num1)
    elif len(str(num)) == 4:
        t = words_number[1000]
        if num % 1000 == 0:
            wrote += words_number[num // 1000] + " " + t
        #from this line need to be fix
        elif num % 1000 <= 20:
            num1 = num %1000
            wrote += words_number[num // 1000] + " " + h + " " + number_under_20(num1)
        else:
            num1 = num %1000
            wrote += words_number[num // 1000] + " " + h + " " + number_above_20(num1)
    return wrote
        
    

    

    #if number exceed 20
    # if num > 20:
    #     if len(str(num)) == 2:

    #     return num_lst[0]
    # elif num_lst > 20:
    #     num_lst = str(num_lst)
    #     return num_lst


    # for x in words_number.keys():
    #     if x == num:
    #         return words_number[num]
    # else:
    #     num = str(num)

    # cor = [words_number.values() for x in words_number.keys if x == num ]
    # return cor
    

def show_number():

    numbers = input("please enter the number from 1 to 1 000 000 000: ")
    if numbers.isdigit():
        numbers = int(numbers)
        if numbers <= 20:
            print(number_under_20(numbers))
        elif numbers > 20 and len(str(numbers)) == 2:
            print(number_above_20(numbers))
        elif len(str(numbers)) >= 3:
            print(count_numbers(numbers))
    else:
        print("Put a correct value!")
    
show_number()

