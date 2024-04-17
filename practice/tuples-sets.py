# Tuple : Immutable list of items. Obviously ORDERED.

i = 0
j = 0
while i <= 2:
    if j % 2:
        j += 1
    print(i, ":", j, end=" ")
    i += 1
    j += 1

t = (1, 's', 3.4, None, False, "sodjdj")
print(t)
t1 = (1, 2, 3, 4)
t2 = (1, 2, 3, 4)
t3 = (4, 3, 2, 1)
print("Tuples are ordered: t1 == t2:", t1 == t2, " t1 == t3:", t1 == t3)
# t.append(3)  Cannot append/add new element
print("t[2]:", t[2], "t[-2]:", t[-2])  # Can access tuple members by numeric index
print("tuple slicing:", t[1:-1])  # from index 1 until -2
# t[2] = ""    TypeError: 'tuple' object does not support item assignment

# How to initialize an empty tuple
tu = ()  # Initialize empty tuple
print(type(tu))
singleMemberTuple = (1)
print(type(singleMemberTuple))  # Cannot create single member tuple with this syntax: (1stItem)
singleMemberTuple = (1,)
print(type(singleMemberTuple))

l = [1, 4, 2, 5, 2, 1]
tfl = tuple(l)
print("\n", tuple(l))
print(list(tfl))

# PACKING and UNPACKING
tpl = 1, 2, 3  # Assigning 3 variables
tpl1 = t, singleMemberTuple, t1, l, t3  # Assigned more complex values
print(
    f"Assigning multiple variable (use case: returning multiple items from return statement) are packed into tuple:\nsimple tuple: {tpl} \ncomplex tuple:{tpl1}")


def captureThisAsTuple():
    return 1, 2, 3  # returning multiple variables is not possible in other programming languages


print("Return values automatically converted to tuple:", captureThisAsTuple())
m = captureThisAsTuple()
print("Multiple variables are automatically captured as tuple:", m)
x, y, z = captureThisAsTuple()  # Power of Python, returning and capturing multiple variables
print("Tuples get automatically unpacked into multiple variables:", x, y, z)

# x, y = captureThisAsTuple() -- Not possible. Too many values to unpack
# x, y, z,c = captureThisAsTuple()  -- Not possible. Need more values to unpack

x, y = (10, 20)
xx, yy = [10, 20]  # Unpacking also works for list. But returning multiple values defaults into tuple.
c = 1, 2, 3, 4, 5  # Packs into tuple only
print(type(c), c)

print(x, y)
y, x = x, y
print("Use of tuple to swap values: y, x = x, y -->", x, y)

# Use of tuple
student_data, second_low_score, second_names = None, None, None

students = [("Milind", 100), ("Neel", 87), ("Latika", 98), ("Hrishikesh", 56),
            (67, "Vivek")]  # Don't change sequence while creating tuple. It will give you trouble afterwards
students = [("Milind", 100), ("Neel", 87), ("Latika", 98), ("Hrishikesh", 56), ("Vivek", 67)]
print("\nStd for loop with tuple")
for st in students:
    print(f"Student name:{st[0].center(10, ' ')} got {st[1]} marks")
print("\nEasy and good way by tuple unpacking:")
for name, marks in students:
    print(f"Student name:{name.center(10, ' ')} got {marks} marks")

# Tuple maths
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(
    f"\nTuple maths: a:{a}, b:{b} then a + b : length:{len(c)}, data:{c}\nREASON: TUPLES ARE IMMUTABLE.. so values do not add themselves but new members are added.")

# Maths
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(f"\nList maths: a:{a}, b:{b} then a + b : length:{len(c)}, data:{c}\nREASON: New members are added.")

f = [1, 2, 3]
j = (6, f)
print(j)
f.append(5)
print(j, "tuples are immutable.. but list inside tuple is always mutable.")
(lambda n: print(f'Hello World {n}'))(7)

people = [
    ("Alice", 30, "Female"),
    ("Bob", 25, "Male"),
    ("Charlie", 35, "Male"),
    ("Diana", 28, "Female"),
    ("Ethan", 40, "Male"),
    ("Fiona", 22, "Female"),
    ("George", 33, "Male"),
    ("Hannah", 29, "Female"),
    ("Ian", 27, "Male"),
    ("Julia", 31, "Female")
]

aged_people = sorted(people, key=lambda n: n[1])
print(aged_people)

# S  E  T  S
# Sets are UNORDERED
# No index can be used set[2] -- NO

l = [4, 5, 3, 5, 7, 3, 6, 7, 8, 3, 3, 3, 5, 6, 6, 5, 5]
t = (4, 5, 3, 5, 7, 3, 6, 7, 8, 3, 3, 3, 5, 6, 6, 5, 5)
s = {4, 5, 3, 5, 7, 3, 6, 7, 8, 3, 3, 3, 5, 6, 6, 5, 5}  # Set automatically avoids same elements
print(f'\n\nl={l}\nt={t}\ns={s}')

# s[3] ERROR: Class 'set' does not define '__getitem__', so the '[]' operator cannot be used on its instances
# Cannot use indexing s[3] becuase sets are unordered.

se = {}
print(type(se))
print("\nType of empty {} resolves to", type(se), "because dictionaries and set, both use curley braces. So empty sets "
                                                  "are created using se = set()")
se = set()
print(se, type(se))

print(5 in s, 10 in s)
print("Sets are heretogenious, it can store any* data structures. But restrictions are:")
print("Sets cannot store other sets, lists and dictionaries because they are MUTABLE")
se.add(1)
se.add(2.3)
se.add("String")
# se.add((4,8,[9,0],{2,8}, {"abc": 1})) # TypeError: unhashable type: 'list'
se.add((4, 8, True, None))  # Adding a tuple
print(se, " --( looks unordered)")
print('So Immutable - INT,FLOAT,STRING,TUPLE,BOOL'
      '\nmutable - LIST,SET,DICT')

# se.add([5,3,7,8]) # Not allowed to add single element which is list-- lists are mutable
# but, following is allowed
se.update(
    [5, 3, 7, 8, 3])  # update is adding all elements present in iterable.. it is not for adding it as a single complex.
print(se)
se.remove(2.3)
print(se)
# SET INTERSECTION, UNION, DIFFERENCE-> A-B, B-A ,  SYMMETRIC DIFFERENCE-> (A-B) UNION (B-A)
s1 = {2, 3, 4, 5}
s2 = {1, 3, 4, 6, 7, 8}
print(f's1:{s1} AND s2:{s2}')
print("INTERSECTION:", s1.intersection(s2), 'OR', s1 & s2, " --& is short hand operator for intersection for set")
print("UNION:", s1.union(s2), 'OR', s1 | s2, " -- | is short hand operator for union")
print("DIFFERENCE:", s1.difference(s2), 'OR', s1 - s2, "  -- dash - is shorthand for difference")
print('SYMMETRIC DIFFERENCE', s1.symmetric_difference(s2), 'OR', s1 ^ s2,
      "  -- ^ is shorthand for symmetric difference")

print("\n Given a string, show all unique characters.")
str = "This is unique string"
uniq = set()
uniq.update(str)
print(uniq)

tup1 = (1,2,3)
tup2 = (1,2,3)
print(tup1+tup2)

set1 = {1,2,3}
set2 = {2, 3, 7}
# print(set1+set2) #Error because Class 'set' does not define '__add__', so the '+' operator cannot be used on its instances
set1.add(4) # single element
# set1.add(set2) # set cannot be added as it unhashable.
set1.update(set2) # iterable
print(set1)
