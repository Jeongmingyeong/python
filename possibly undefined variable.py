def print_content(iterable):
    """
        print the content of the given iterable
    """
    for value in iterable:
        print(value)
    last_value = value
    print('The last_value is ', last_value)


print_content('abcd') # No error
print_content([]) # error