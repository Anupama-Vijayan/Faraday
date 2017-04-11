#finding minimum of 3 numbers
def minimum(a, b, c):
    mini = a
    if b < a:
        mini = b
    if c < mini:
        mini = c
    return mini

'''
******** Testing for the above code *********
'''
print(minimum(-6,6,0))