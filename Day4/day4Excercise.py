str1 = 'Thirty'
str2 = 'Days'
str3 = 'of'
str4 = 'python'
space = ' '
str = str1+space+str2+space+str3+space+str4
print(str)

str = 'Coding' + ' ' + 'for' + ' ' +'all'
print(str)

company = "Coding for all"
print(company)
print(len(company))
companyUpper = company.upper()
print(companyUpper)
companyLower = company.lower()
print(companyLower)

print(company.capitalize(), company.title(), company.swapcase() )

print(company.split(' ')[0])

print(company.index('Coding'))
print(company.find('Coding'))

company_new = company.replace('Coding', 'Python')
print(company_new)

company_new = company_new.replace('all', 'everyone')
print(company_new)

list_str = company.split(' ')
print(list_str)

str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
li2 = str.split(", ")
print(li2)
print(company[0])
print(company.rfind('l'))
print(company[10])

list3 = company_new.split(' ')
str = ""
for word in list3:
    str += word[0]

print(str)

str_acry = ''.join(company.split()[0][0])
str_acry = str_acry+company.split()[1][0]+company.split()[2][0]
print(str_acry)

print(company.index('C'))
print(company.find('C'))

print(company.find('f'))

print(company.rfind('l'))

phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase.find('because'))
print(phrase.rfind('because'))
print(phrase[phrase.find('because'):phrase.rfind('because')+7])

print(company.startswith('Coding'))
print(company.endswith('coding'))

print('   Coding For All      '.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

list_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
str_join = '# '.join(list_lib)
print(type(str_join))
print(str_join)

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
print('The area of a circle with radius %d is %d meters square.' % (radius, (int)(area)))
print('The area of a circle with radius {} is {} meters square'.format(radius, (int)(area)))
print(f'The area of a circle with radius {radius} is {(int)(area)} meters square')

a=8
b=6

print('%d + %d = %d' %(a, b, a+b))
print('%d - %d = %d' % (a, b, a-b))
print('%d * %d = %d' % (a, b, a*b))
print('%d / %d = %.2f' % (a, b, a/b))
print('%d %% %d = %d' % (a, b, a%b))
print('%d // %d = %d' % (a, b, a//b))
print('%d ** %d = %d' % (a, b, a**b))

print(f'{a} % {b} = {a%b}')


print('{} % {} = {}'.format(a, b, a%b))