def get_number():
    n = int(input("Enter a number : "))
    return n

def get_divisors(n):
    divisors = []
    for i in range(2,n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

n = get_number()
divisors = get_divisors(n)
if divisors == []: 
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number, it's divisors are {}".format(n,divisors))
