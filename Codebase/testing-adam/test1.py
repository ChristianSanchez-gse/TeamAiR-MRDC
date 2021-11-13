def func1():
    print("Function 1")

def power(a, b=1):
    result = 1
    for i in range(b):
        result *= a
        return result

print("Hello world!")
x = 0
print(x)
x = "hello"
print(x)
func1()
print(power(2,4))
