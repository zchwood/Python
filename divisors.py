print("**********DIVISORS************\n \n ")
num = int(input("Enter a number to see its divisors : "))
x = []
for i in range(2,num+1):
    if num % i == 0:
        x.append(i)

print(x)