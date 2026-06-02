#DICTIONARY
'''
Dictionary - Ordered (3.7+ version), key value pair, keys should be immuatble.

Access - dictionary[<key>] - If key doesn't exists then, give error. 
         dictionary.get(<key>) - Returns None, if key doesn't exist. 

If we have duplicate key then it updates that key with later value. 

dictionary.items() - Change dictionary into a list of key-value pair tuple.

Remove - pop(<key>) - removes specified key item and error if key doesn't exists, and returns value.
         popitem() - removes last item, no argument, returns last item.
         del dictionary[<key>] - removes specified key item, error if key doesn't exists.

COPY = dictionary.copy() - creates a copy and prevents mutation.

clear() - empties the dict.
del dictionary - delete it.

.keys() - returns a list of keys
.values() - returns a list of values. 

'''
#I put it above as we have a var name dict
d = dict.fromkeys(['1','2','3','4'])
print(d)


dict = {}
print(type(dict))

#'key3' will point to 'val4'
dict = {'key1':'value1', 'key2':'value2','key3':'value3','key3':'value4','key5':'value5'}
print(dict)

print(dict.get('key4'))
#KeyError : key not exists
# print(dict['key4'])

#List as key not allowed
#dict[['a','b']]='list'

#Adding a new element in dict
dict[('a','b')]='tuple'
print(dict)

#Update existing key's value.
dict['key1']='value-one'
print(dict)

#Checking key
print('key4' in dict)
print('key3' in dict)

#Convert dict to a list
dict_list = dict.items()
print(dict_list)

print(dict)
print(dict.pop('key3'))
print(dict)
print(dict.popitem())
print(dict)
del dict['key2']
print(dict)

#copy() prevents from mutation.
dict2 = dict.copy()
dict2['key2']='value2'
print(dict2)
print(dict)

dict.clear()
print(dict)

keys = dict2.keys()
print(keys)
vals = dict2.values()
print(vals)
print(dict2.fromkeys('1'))
print(dict2)

