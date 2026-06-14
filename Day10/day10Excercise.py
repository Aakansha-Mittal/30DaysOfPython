#LEVEL 3

from countries import countries
from countries_name import countries_data



country_land = []

for iter in countries:
    if 'land' in iter:
        country_land.append(iter)

print(country_land)

fruits = ['banana', 'orange', 'mango', 'lemon']
s = 0
e= len(fruits)-1
while s<=e:
    temp = fruits[e]
    fruits[e] = fruits[s]
    fruits[s] = temp
    s = s+1
    e = e-1
print(f"Fruits after reverse : {fruits}")

lang_set = set()

for my_dict in countries_data:
    lang_set.update(my_dict.get('languages'))

print(lang_set)
print(f"Total no of languages : {len(lang_set)}")


language = dict()

for my_dict in countries_data:
    for i in my_dict.get('languages'):
        if language.get(i):
            language[i] = language[i] + 1
        else :
            language[i] = 1
print(language)
for i in language.items():
    print(i)

sorted_language = (sorted(language.items(), key= lambda item : item[1], reverse=True))
print(f"Sorted Language : {sorted_language}")
print(f"Top 10 spoken languages are : {sorted_language[:10]}")

population = dict()

for iter in countries_data:
    population[iter.get('name')] = iter.get('population')

population = sorted(population.items(), key= lambda item:item[1], reverse=True)
print(f"Top 10 populated countries are : {population[:10]}")


#LEVEL - 2 
sum = 0
for i in range (1, 101):
    sum = sum+i
print(f"Sum of integers from 1 to 100 is : {sum}")

even_sum, odd_sum = 0, 0

for i in range(1, 101) :
    if (i%2==0):
        even_sum = even_sum+i
    else:
        odd_sum = odd_sum + i

print(f"Even sum : {even_sum} and odd sum is : {odd_sum}")


#LEVEL 1 - 1
''' 
for i in range(10):
    print(i, " for loop")

count =0
while count <11:
    print(count, " while loop")
    count = count+1

count = 10
while(count>=0):
    print(count, " while loop")
    count = count-1
    '''

skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in skills:
    print(i)

print("Even numbers fro, 1 to 100 are : ")
for i in range(1, 101):
    if i%2==0:
        print(i, end= ' ')
print()

print("Odd numbers fro, 1 to 100 are : ")
for i in range(1, 101):
    if i%2!=0:
        print(i, end= ' ')
print()

n = 8
for i in range(n):
    for j in range(n):
        print('# ', end='')
    print()

for i in range(n):
    j = 0
    while j<=i:
        print('* ', end='')
        j = j+1
    print()

for i in range(11):
    print(f"{i} * {i} = {i*i}")