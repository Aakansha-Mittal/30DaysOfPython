#Excercise Day2 Level 1

#Day 2: 30 Days of python programming

first_name = 'Aakansha'
last_name = 'Mittal'
full_name = first_name + ' ' + last_name
age = 22
year = 2026
is_married = 'No'
is_true = True
is_light_on = False
country, city, pincode = 'India', 'Ghaziabad', 201206

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(country))
print(type(city))
print(type(pincode))

print(len(first_name))
print(len(last_name))
print(len(full_name))

#object of type 'int' has no len()
#print(len(age))
#print(len(year))

print(len(is_married))

#object of type 'bool' has no len()
#print(len(is_true))
#print(len(is_light_on))

print(len(country))
print(len(city))
#print(len(pincode))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = pow(num_one, num_two)
floor_division = num_one // num_two
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

r=30
pi = 3.14
area_of_circle = pi*r**2
circum_of_circle = 2*pi*r
print(area_of_circle)
print(circum_of_circle)

r_user = float(input("Enter radius of circle : "))
area_user = pi*r_user**2
circum_user = 2*pi*r_user

print("Area with user radius : ", area_user)
print("Cicum with user radius : ", circum_user)

f_name = input("First name : ")
l_nam = input("Enter last name : ")
country = input("Enter country : ")
age = int(input("Enter age : "))

print("FName, LName, Country, Age : ", f_name, l_nam, country, age)

help('keywords')
