age = 22
height = 144.5
complex = 4+2j
print(complex)
b = int(input("Enter base of triangle"))
h = int(input("Enter height of triangle"))
area = 0.5*b*h
print("Area of triangle - ", area)

a = int(input("Enter side a : "))
b = int(input("Enter side b : "))
c = int(input("Enter side c : "))
perimeter = a+b+c
print(perimeter)

l = int(input("Enter length of rectangle : "))
b = int(input("Enter width of rectangle : "))
area_rect = l*b
peri_rect = 2*(l+b)
print("Ared rectabgle : ", area_rect)
print("Peri rect : ", peri_rect)

r = int(input("Enter circle radius : "))
pi = 3.14
area_circle = pi*r**2
peri_circle = 2*pi*r
print("Area and circumfrance of circle with radius ", r, " is ", area_circle, " and ", peri_circle)

m = 2
y = -2
x = -y/m 
print("Slope, x intercept, y intercept : ", m," , ",  x, " , ", y)

x1 = int(input("Exnter x for point 1 : "))
y1 = int(input("Exnter y for point 1 : "))
x2 = int(input("Exnter x for point 2 : "))
y2 = int(input("Exnter y for point 2 : "))
slope_m = (y2-y1)/(x2-x1)
print("Calculated slope is : ", slope_m)

print(m==slope_m)

eq_x = int(input("Enter x : "))
eq_y = eq_x**2 + 6*eq_x + 9
print("Calculated eq y is : ", eq_y)

print(len('python'), len('dragon'))
print(len('python') != len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon.')

print('on' not in 'python' and 'on' not in 'dragon')

str_len = len('python')
print(type(str_len))
print(str_len)
str_len = (float) (str_len)
print(type(str_len))
print(str_len)
str_len = str(str_len)
print(type(str_len))
print(str_len)

n = int(input("Enter a number to check even or not "))
print(n%2 == 0)

print(7%3 == int(2.7))
print(type('10') == type(10))

#As this is decimal in fload so will give ERROR so first in float and then in 
#print(int('9.8')==10)

print(int(float(('9.8')))==10)

hours = int(input("Enter hours : "))
rate = int(input("Enter rate per hour : "))
print("Your earning is : ", hours*rate)

years = int(input("Enter years you lived : "))
seconds = years*365*24*60*60
print("You have lived these seconds : ", seconds )

print(1, 1**0, 1**1, 1**2, 1**3, 1**4)
print(2, 2**0, 2**1, 2**2, 2**3, 2**4)
print(3, 3**0, 3**1, 3**2, 3**3, 3**4)
print(4, 4**0, 4**1, 4**2, 4**3, 4**4)
print(5, 5**0, 5**1, 5**2, 5**3, 5**4)








