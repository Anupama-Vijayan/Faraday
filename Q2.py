def convert(a):

    #check if string can be converted to int, else pass
    try:
        b = int(a)
        return b
    except ValueError:
        pass

    #check if string can be converted to float, else it is a string
    try:
        c = float(a)
        return c
    except ValueError:
        return a

'''
******** Testing for the above code *********
'''
print(type(convert("1")))
print(type(convert("1.00")))
print(type(convert("1abc")))