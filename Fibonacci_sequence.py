#Fibonacci sequence 


def fibonacci(n):

    p = 0
    q = 1
    

    for x in range(n):
        new_seq = p+q        

        p, q = q, new_seq
        print(new_seq)
    

ask = int(input('Put a value for Fibonacci sequence: '))
fibonacci(ask)