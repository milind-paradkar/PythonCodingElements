# Single line comment

'''
Multi-line comment
looks
like
        this
'''

'''  Getting input from user and showing message
print('What is your name:', end='')
usr = input()
print("Hello,", usr, "!", "-from", "Milind", sep=' ')
'''
# print('d')
# print(type('a'))
# print(type("a"))

xy = ["1", 2]
print(type(xy))

i = 5
i += 7
print("i:", i)
print('Looks like Python does not support --i and i--')
# List-ordered collection of even different  datatype
a = [1, 'Milind', 2.5, True, None]
print(type(a), type(a[0]), type(a[1]), type(a[2]), type(a[3]), type(a[4]))
print(3 * 4)
print(13 / 5, "(division may results in float)")
print(13 // 5, "# // represents int division")
print(-13 // 5, "# // causes in flooring in case of negative number")
print("% operator:", 13 % 5)
print(-13 % 5, "Why? why not", 13 % 5)  # to be noted
print(3 % 20)
print(3 ** 2, "** represents exponential")
print(3 ^ 2, "# ^ represents bitwise XOR")
print(2 + 3 * 4)
print(True)
print(False)
print("@ : Matrix multiplication"" is "
      " shown "
      " like this."
      " \nI am not using + operator here."
      " Strange ! double quotes or single quotes does not require + to concatenate in Python.")

# Slicing
print('\n\nslicing')
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)
print(lst[0])
print(lst[-1])
print(lst[2:])
print("lst[1:]=", lst[1:])
print("lst[:3]=", lst[:3])
print(lst[:-3])
print(lst[1:-1])

usr = input("Please enter your name:")
print("Hello", usr)



