def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

n = int(input("Enter number: "))
print("Factorial:", factorial(n))
