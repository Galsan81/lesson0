my_dict={'Vasya': 1974, 'Petya':1955, 'Kolya': 1987, 'Nikita':2000}
print('Dict:',my_dict)
print('Existing value:', my_dict['Nikita'])
print('Not existing value:', my_dict.get('Lena'))
my_dict['Bob']=1989
my_dict['Lee']=1966
f=my_dict.pop('Kolya')
print('удаленный:',f)
print('Modified dictionary:',my_dict)
my_set={1, 3, 2, 're', 3, 2, 'net', (1, 'mat')}
print('Множество:',my_set)
my_set.add('adli')
print('После добавления:', my_set)
my_set.discard('net')
print('C удалением:', my_set)
