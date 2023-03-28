def recursion_error1(var, base): # does not decrease argument (var)
    if var == 0:
        return base
    base = base * 2
    return recursion_error1(var, base)

def recursion_error2(var, base): # no terminating case
    base = base * 2
    return recursion_error2(var-1, base)

def __str__(self):
    return str(self)

print(recursion_error1(5, 5))
print(recursion_error2(5, 5))
#print(__str__(111))