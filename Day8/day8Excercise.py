dog = {}
print(dog)
dog['name']='Tuffy'
dog['color']='Brown'
dog['legs']='4'
dog['age ']='2'
print(dog)

student = {
    'first_name':"Aakansha", 'last_name':"Mittal", 'Gender':'Female',
    'Age':22, 'is_married':False, 'skills':['java','python'],
    'country':'India', 'city':'Ghaziabad',
    'address': {
        'vill':'dedha',
        'zip' : '201206'
    }
}

print(student)
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('SQL')
print(student)

print(student.keys())
print(student.values())

print(student.items())

print(student.pop('Age'))

del dog