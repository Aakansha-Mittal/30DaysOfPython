# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(it_companies)
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Zepto', 'Salesforce', 'Goldman sachs', 'Jp'])
print(it_companies)
it_companies.remove('Goldman sachs')
print(it_companies)
#ERROR
# it_companies.remove('AATU JHATU')

it_companies.discard('AATU JHATU')
print(it_companies)

joinAB = A.union(B)
intersectionAB = A.difference(B)
intersectionBA = B.difference(A)

isASub = A.issubset(B)
areDisjoin = A.isdisjoint(B)
AB = A.union(B)
BA = B.union(A)

symDiff = A.symmetric_difference(B)

print("Union : ", joinAB)
print("Intersection A B: ", intersectionAB)
print("Intersection B A: ", intersectionBA)

print("isSubsets : ", isASub)
print("Disjoints : ", areDisjoin)
print("A union B : ", AB)
print("B union A : ", BA)
print("Symmetric diff : ", symDiff)

del A
del B

age_st = set(age)
print(f"Age list len : {len(age)} and Age set len : {len(age_st)}")

str1 = "I am a teacher and I love to inspire and teach people"
list_str = str1.split(' ')
print(list_str)
str_set_unique = set(list_str)
print(str_set_unique)