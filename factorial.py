i=int(input("Please enter any value"))
def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i-1)

result = factorial(i)
print(result)
