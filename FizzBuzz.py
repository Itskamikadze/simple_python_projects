def FizzBuzz(n):
    result = []
    z = ["FizzBuzz"*(not x%15) or "Fizz"*(not x%3) or "Buzz"*(not x%5) or x for x in range(1, n+1)]
    print(z)
result = int(input("Put a value: "))
FizzBuzz(result)