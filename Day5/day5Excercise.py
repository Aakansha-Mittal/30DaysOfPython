lst = []
print(lst)
lst = list()
print(lst)

lst = [1,2,3,4,5,6]
print(lst)
print(len(lst))
print(f"First {lst[0]}, middle {lst[(len(lst)-1)//2]}, last {lst[len(lst)-1]}")

mixed_list = ['Aakansha', 22, 155, 'Unmarried', 'Ghaziabad, UP, India']
print(mixed_list)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print("No of companies : ", len(it_companies))
print(f"First {it_companies[0]}, middle {it_companies[(len(it_companies))//2]}, last {it_companies[-1]}")
it_companies.insert(5, 'Myntra')
it_companies.insert((len(lst))//2, 'Hp')
it_companies[0] = it_companies[0].upper()
print(it_companies)

str = '#; '.join(it_companies)
print(str)

print('Myntra' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
if len(it_companies)%2 ==0:
    print(it_companies[(len(it_companies)-1)//2 : (len(it_companies)//2 ) +1])
else:
    print(it_companies[(len(it_companies))//2])
print(it_companies[-3:])

it_companies.pop(0)
if len(it_companies)%2 ==0:
    del it_companies[(len(it_companies)-1)//2 : (len(it_companies)//2 ) +1]
else:
    del it_companies[(len(it_companies))//2]
print(it_companies[-3:])

it_companies.pop(-1)
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
#print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end
print(full_stack)
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'Sql')
print(full_stack)


#EXCERCISE 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f"Min is : {ages[0]} and Max is : {ages[-1]}")
ages.append(ages[0])
ages.append(ages[-1])
ages.sort()
if len(ages)%2 ==0:
    print(
        ages[(len(ages)-1)//2 : (len(ages)//2 ) +1])
else:
    print(ages[(len(ages))//2])

for n in ages:
    n+=n
avg = n/len(ages)
print(f"{avg:.2f}")

rng = ages[-1]-ages[0]
print(rng)
print(abs(ages[0]- avg))
print(abs(ages[-1]- avg))
print(abs(ages[0]- avg)> abs(ages[-1]- avg))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

if len(countries)%2 ==0:
    print(countries[(len(countries)-1)//2 : (len(countries)//2 ) +1])
else:
    print(countries[(len(countries))//2])
first_half = countries[: (len(countries)//2 ) +1]
second_half = countries[ (len(countries)//2 ) +1 : ]
print(first_half)
print(second_half)

first, second, third, *scandous = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(f'{first}, {second}, {third}, {scandous}')
