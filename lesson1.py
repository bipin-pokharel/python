# 1  # greeting = "hello world" 
# print(greeting)

#  2 # line01 = '**********************' #header / footer
# line02 = '*                     *' #re-use
# line03 = '*   WELCOME  !        *'
# print('')
# print(line01)
# print(line02)
# print(line03)
# print(line02)
# print(line01)

#  3 meaning = 69
# print('')
# if meaning > 10:
#   print('right on')
# else:
#   print('not today')
   
  #  4 ternary operator
# meaning = 20
# print('right on') if meaning > 10 else print('not today')

# 5 data types
# string data type
first = 'Dave'
last = 'gray'
# print(type(first))
# print(type(first)==str)
# print(isinstance(first,str))

# constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))

# concatenation
# fullName = first + "" + last
# print(fullName)
# fullName +="!"
# print(fullName)

#casting a number to a string
# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = " i like rock music from the " + decade + "s."
# print(statement)

# Multiple lines
multiline = '''
Hey how are you ?

i was just checking in .
                         All good?             

'''
# print( multiline)


# escaping special characters
# sentence = 'I\'m  back at work! \t Hey! \n\n Where\'s this at\\located?'
# print(sentence)


# string methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good","ok"))
# print(len(multiline))

#build a menu
# title = "menu".upper()
# print(title.center(20,"="))
# print("Coffee".ljust(16,".") +"$1".rjust(4))
# print("Moffin".ljust(16,".") +"$2".rjust(4))
# print("Cheesecake".ljust(16,".") +"$4".rjust(4))
# print('')

#string index values
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

#Some methods include boolean data
# print(first.startswith("D"))
# print(first.endswith("Z"))

# boolean data type
# myvalue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue,bool))

# numeric data type
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price,int))

# float type
gpa = 3.28
# y = float(1.4)
# print(type(gpa))

# built-in functions
# print(abs(gpa))
# print(round(gpa))

print(round(gpa,1))
import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting an string to an number
zipcode = "1001"
zip_value = int(zipcode)
print(type(zip_value))
