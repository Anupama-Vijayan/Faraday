import operator as sign
def apply_operation(left_operand, right_operand, operator):
    #using dictionaries instead of multiple if statements
    x = {'+': sign.add, '-': sign.sub, '*': sign.mul, '/': sign.div }
    return x[operator](left_operand, right_operand)

'''
******** Testing for the above code *********
'''
print(apply_operation(2,3,'+'))
