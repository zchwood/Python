def get_num():
    n = int(input("Enter how many Fibbonacci numbers to generate : "))
    return n

def get_fib(n):
    x = 1
    y = 1
    fib = [x,y]
    while len(fib) < n:
        z = x + y
        fib.append(z)
        x = y
        y = z
    return fib
number = get_num()
print(get_fib(number))
