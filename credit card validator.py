#check sum
check_sum = [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
card_num = []
c = []
print(type(check_sum))


class ValidCard:

    def number(self):
        # make a value input to create for loop
        while True:
            try:
                value = int(input("Please put a value: "))
                value = str(value)
                # if exceeded, put an information
                if len(value) > 16:
                    print("Your value is out of range! Max numbers are 16!")
                # if is lower than 16, add 0's to the very beggining to make 16
                elif len(value) < 16:
                    while len(value) < 16:
                        value = "0" + value
                # if is equal to 16, add values to the lists
                    else:
                        for x in value:
                            card_num.append(int(x))
                        return 'Your card number is:', card_num
                else:
                    for x in value:
                            card_num.append(int(x))
                    return 'Your card number is:', card_num
                
            except ValueError:
                print("Put a correct value!")

    def check(self):
        # create third lists to multiply value by value
        res_list = [check_sum[x] * card_num[x] for x in range(len(check_sum))]
        print(res_list)
        # catch the values which are higher than 10 and change the on the string 
        for x in range(len(res_list)):
            if res_list[x] > 9:
                res_list[x] = res_list[x] % 10
                res_list.append(1)
        if sum(res_list) % 10 == 0:
            return 'Your card number is valid!', sum(res_list)
        return ' Your card number is invalid!', sum(res_list)
        

        
if __name__ == "__main__":
    valid = ValidCard()
    print(valid.number())
    print(valid.check())


