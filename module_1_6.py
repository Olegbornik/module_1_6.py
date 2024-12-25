my_dikt = {'Oleg': 1971, 'Vlad': 1993, 'Lusi': 1946}
print(my_dikt)
print(my_dikt['Lusi'])
print(my_dikt.get('Ivan'))
my_dikt['Anton'] = 1973
print(my_dikt)
my_dikt.update({'Platon': 2021,'Sergei': 1970})
print(my_dikt)
a = my_dikt.pop('Anton')
print(my_dikt)
print(a)
print(my_dikt)
my_set = {1,2,3,12,23,41,'Banana',3.14,1,2,3}
print(my_set)
print(type(my_set))
list_ = [1,1,22,3,3,12,23,41,3.14]
list_ = set(list_)
print(list_)
print(list_.add(19))
print(list_)
print(list_.discard(41))
print(list_)

