tup = tuple()
print(tup)
bros = ('ujjwal', 'nonu', 'rahul', 'aryan')
sis = ('divya', 'jiya', 'nancy', 'arpita', 'anshi')
siblings = bros + sis
print(siblings)
print("No. of siblings : ", len(siblings))
parents = ('Neetu', "Aamod")
family_members = parents + siblings
print(family_members)

mother, father, *sibs = family_members
sibs = tuple(sibs)
pars = (mother, father)
print(pars)
print(sibs)

fruits = ('apple', 'mango', 'banana', 'cherry')
vegetables = ('potato', 'carrot', 'raddish', 'cucumber')
animal_product = ('milk', 'egg')
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_tp)
if (len(food_stuff_lt)%2 == 0):
    print(food_stuff_lt[(len(food_stuff_lt)-1)//2 : (len(food_stuff_lt)//2) + 1])
else : 
    print(food_stuff_lt[(len(food_stuff_lt))//2 ])

print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

del food_stuff_lt
#print(food_stuff_lt)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)