# D  I C T I O N A R I E S
d = {}  # By default, {} represents empty dict, to create empty set we need to say se = set()
print(d, type(d))
d = {"name": "Me", "age": 3, "subject_count": 3, "subjects": ['Maths', "Physics"]}
print(d, type(d))

print("\nAgain, dicts are non-indexed, so cannot be called by di[3]")
print(f'\nDict:{d}\nKeys (unique):{d.keys()} type:{type(d.keys())}\nValues (non-unique):{d.values()}')
print(f'Accessing dict: age:{d["age"]}')
d["age"] = 4
d["new_key"] = 'New Value'
print(d)

s = "Milind"
d[s] = "Paradkar"
print(d)
print(d[s], d['Milind'], d.get(s), d.get('Milind'), d.get('milind', 'default value'))
# print(d['random'])  KeyError: 'random'

print('\n', 'random' in d.keys(), 'age' in d.keys())
print('\nloops:')
for i in d:
    print("i:", i)
    print('d:', d[i])
for i in d.keys():
    print("keys:", i)
for i in d.values():
    print('values:', i)
    print(
        'You can access values, but there is no way to access element back based on value.. because values can contain duplicates.. no way back.')
for i in d.items():
    print('items:', i)
    print(i[0], i[1])
for key, value in d.items():
    print('key:', key, 'value:', value)

print("removing key 'Milind':", d.pop("Milind"), "remaining dict:", d)
# d.pop("new_key1")
d.popitem()  # Pops last item. Return value is tuple (key, value) being popped out. You can use it iteratively until all items are popped out.
print(d.popitem(), d.popitem(), d)

print('\n HETEROGENITY OF DICTIONARIES:')
print('Keys -> any type other than Lists, set and dictionaries. Tuples are allowed as a key.\nValues: No restriction')

d1 = {
    'string': 12,
    12: 123,
    None: 'Never',
    True: 'always',
    4.3: 'PI',
    (6, 7, 8): True
}
print(d1)

print("\nMUTABLES: LISTS, SETS, DICTIONARIES")
print('MUTABLE: INTEGER, FLOAT, STRING, BOOLEAN, TUPLES -- ARE ALLOWED AS A KEY IN DICTIONARIES\n')

st = "This is a simple string"
# st= 'ababbbba    f  h   '
value_count = {}
unique_set = set(st)
ctr = 0
for s in unique_set:
    value_count[s] = st.count(s)
    '''ctr += 1
    print(ctr)'''
print("Value_counts:", value_count)

dict1 = {1: 1, 2:3}
dict2 = {4: 1, 2:5}
# dict1 + dict2 # Class 'dict' does not define '__add__', so the '+' operator cannot be used on its instances