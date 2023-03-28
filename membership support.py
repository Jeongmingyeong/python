
def error_func():
    zero_array = [0]
    return '0' in zero_array[0]

def func1():
    zero_array = ["0"]
    return '0' in zero_array[0]

def func2():
    zero_array = [0]
    zero_array[0] = "00"
    return '0' in zero_array[0]

print(func1())
print(func2())
print(error_func())
