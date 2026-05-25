#String - Single, double or triple quotes
#String - text data type

str = 'Demo string'
print(str)
print(len(str))

#Multi line string - Triple quotes (''' ''' or """ """)
multi_line = '''Hi, 
This is me
Aakansha !!!
'''
print(multi_line)

#String concatenation : To concatenate two strings
first = 'Aakansha'
space = ' '
last = 'Mittal'
full = first + space + last
print(first, space, last, full)

#ESCAPE SEQ : Aletter followed by \.
'''\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")'''
print('\\', '\'', '"', '\"')

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"')

#STRING FORMATTING
'''
Putting values/variables inside a string in a proper and readable way.

Method -1 
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision

Method - 2
str.format
print("My name is {}. And age is {}".format(name , age))

METHOD - 3
f - strings (3.6+)

starts with f and use {}

print(f'{a} + {b} = {a+b}')

'''
r = 6
area_circle = 3.14*r**2
print('Area of circle with radius %d is %f' % (6, area_circle)) #Forced print till 6th decimal place
print('Area of circle with radius %d is %.2f' % (6, area_circle))

print('Area of circle with radius {} is {}'.format(r, area_circle)) #Exact value only
print(f'Area of circle with radius {6} is {area_circle}')

print('Area of circle with radius {} is {:.2f}'.format(6, area_circle)) #Exact value only
print(f'Area of circle with radius {6} is {area_circle:.2f}')

#String slicing
'''
[s:e:step] - s to e-1

'''

str = 'python'
print(str[7:0:-1])
print(str[7:-1:-1])

#STRING METHODS
'''
capitalize(): Converts the first character of the string to capital letter
count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
endswith(): Checks if a string ends with a specified ending
expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
find(): Returns the index of the first occurrence of a substring, if not found returns -1
rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
format(): formats string into a nicer output
index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
isalnum(): Checks alphanumeric character
isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
isdecimal(): Checks if all characters in a string are decimal (0-9)
isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
islower(): Checks if all alphabet characters in the string are lowercase
isupper(): Checks if all alphabet characters in the string are uppercase
join(): Returns a concatenated string
strip(): Removes all given characters starting from the beginning and end of the string
replace(): Replaces substring with a given string
split(): Splits the string, using given string or space as a separator
title(): Returns a title cased string
swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
startswith(): Checks if String Starts with the Specified String

'''
"""
str.upper() - returns a string all upper case so, need to store the result in a variable.

str.strip() - removes starting and ending spaces.
"""
