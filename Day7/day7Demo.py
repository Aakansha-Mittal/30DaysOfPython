#SET
'''
Un-indexed, un-ordered, unique. 
Empty set - set () 

ADDING - 
add() - adds one item, update() - take list or set as arg and can add multiple items.

DELETE - 
remove(<item>) - item not found then, error
discard(<item>) - removes item and if item not present no error. 
pop() - No args, returns the removed item.

clear() - empties the set.

del <set_name> - delete the set

#UNION - union(), | -> returns a new union set
update() - updates in 1st set

difference() -> returns the diff set

issuperset() 
issubset()

'''

#Empty set 
set1 = set()
print(set1)

#ADD
set1.add(1)
print(set1)
set1.update([1,2,3,4,5,6,7,7,8])
print(set1)

#REMOVE / DELETE
print(set1.discard(8))
print(set1.discard(10))
print(set1)

print(set1.remove(3))
print(set1)
#print(set1.remove(11))
#print(set1.pop(2))
print(set1)
print(set1.pop())
print(set1)

set1.clear()
print(set1)

#del set1
print(set1)

set2 = {1,2,4,5,8,9}
print(set2)

print(set1 | set2)
print(set1.update(set2))
print(set1)
print(set1.union(set2))