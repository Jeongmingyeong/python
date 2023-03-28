def A(): # return false regardless of a and b
    arg1 = False
    arg2 = True

    sub1 = not arg1
    sub2 = not sub1 or arg2
    sub3 = not sub2 and arg2
    sub4 = not arg1 and sub3

    return sub4

print(A())