
abc = ['dog', 'Fido', 10]

#using a tuple
(animal, name, age) = abc
output = ('{name} the {animal} is {age} years old'.format(animal=animal, name=name, age=age))

'''
******** Testing for the above code *********
'''
print(output)