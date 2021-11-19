# debug
## create a new file, solution5.py
## don't copy paste the code, but type it to get more experience with intellisense
# To take input from the user
num = int(input("Enter a number: "))

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

## run the code, it should verify whether something is a prime nr
## if you run the code and enter a prime number, it results in that it's not a prime number
## debug the code using the debug option to step through and find the problem (and fix it)