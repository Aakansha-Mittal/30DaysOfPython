#Que 1 Level 1
age = int(input("Enter your age : "))
if age>=18 :
    print("You are old enough to learn to drive!")
elif age>0 :
    print(f"You need {18-age} more years to learn to drive.")
else :
    print("Please enter valid age!!!")


#Que 2
if age>22 :
    if (age-22 == 1):
        print("You are 1 year older than me")
    else :
        print(f"You are {age-22} years older than me. ")
    
elif age==22 : 
    print("We both are of same age. ")

else : 
    print("I'm the elder one")

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
if (a>b):
    print(f"{a} is greater than {b}")
elif (b>a):
    print(f"{b} is greater than {a}")
else : 
    print(f"{a} and {b} are equal.")


score = int(input("Enter the score : "))
if score>=90 and score<=100 : 
    print("A")
elif score>=80 and score<=89 : 
    print("B")
elif score>=70 and score<=79 : 
    print("C")
elif score>=60 and score<=69 : 
    print("D")
elif score>=0 and score<=59 : 
    print("F")
else : 
    print("Enter the valid score!!!")


Autumn = ['september', 'october', 'november']
Winter = ['december', 'january', 'february']
Spring = ['march', 'april', 'may']
Summer = ['june', 'july', 'august']
month = input("Please enter the valid and correct month : ")
month = month.lower()

if month in Autumn : 
    print("Autumn")

elif month in Winter : 
    print("Winter")

elif month in Spring : 
    print("Spring")

elif month in Summer : 
    print("Summer")

else :
    print("Pleae correct month")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit : ")
fruit = fruit.lower()
if fruit in fruits: 
    print("That fruit already exist in the list")
else : 
    fruits.append(fruit)
    print(fruits)


#LEVEL 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

print(person.get('name'))

if person.get('skills'):
    print(f"Middle skill in skills set : {person.get('skills')[2]}")
    if 'Python' in person.get('skills'):
        print("Python is in skills")
else :
    print('No skills key')

frontend = ["JavaScript", "React"]
if person.get('skills'):
    if frontend == person.get('skills'):
        print("Frontend dev!!")
    elif 'React' in person.get('skills') and 'Node' in person.get('skills') and 'MongoDB' in person.get('skills'):
        print("Fullstack Dev !!")
    elif 'Python' in person.get('skills') and 'Node' in person.get('skills') and 'MongoDB' in person.get('skills'):
        print("Backend Dev !!")
    else :
        print("Dont know!")

if person.get('is_married') and person.get('country')=='Finland' :
    print(f"{person.get('first_name')} {person.get('last_name')} is married. He lives in {person.get('country')}")