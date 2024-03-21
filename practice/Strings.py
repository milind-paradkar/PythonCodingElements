s = "This is big string and can have anything in it"
print(f'String length:{len(s)}, \nparts of string: s[0-10] char(0 to 9):{s[:10]} \nlast char:{s[-1]}\nlast 10 chars:{s[-10:]} \nreverse:{s[::-1]}\n')

multi_line = '''It really starts here.
and goes " multi " ' line ' .          so
no need to encode \\n or escape it
'''
print("multi-line String:", multi_line)
s += multi_line
print(f"Concatenated s:{s}")
print(f'String.split(): splits by all separator. If sep is not specified or is None, '
      f'any whitespace string is a separator and empty strings are removed from the result.\n {s.split()}')

s1 = "This string is funny thing in Python."
print("\nString:",s1, "-->Split with some chars ('is'):", s1.split('is'))
# Split: Input: str, Output: list(str)
# Opposite of this:
# Join: Input: list(str), Output: single str
sList = ["Sam", "Mona", 'Lala', 'Gordon']
print("\nJoin:", "_".join(sList))
print("Split and join together.", "_".join(s1.split()))

print("find:", s1.find("is"), s1.find('T'), s1.find('t'),  s1.find('z'))
print("count", s1.count("is")) # This, is
print("count", s1.count(" "))
print("count", s1.count(","))
sList.sort()
print("sList.sort() : Sorts the string list and list is mutable, so inline sort happens. If you print sList.sort(), it gives None because it sorts but does not return anything.", sList)
print("Opposite to it, if we use sorted(List), it gives you back sorted list as a return and also keeps actual list sorted. Double work.")
sList = ["Sam", "Mona", 'Lala', 'Gordon']
print("list(str).sort():", sList, sorted(sList), sorted(sList, reverse=True), sList)

print("\nReplace:", s1.replace("is", "was")) #  Thwas ?? 'is' replaced with 'was'

print("\nisdigit():", "".isdigit(), " ".isdigit(), "9".isdigit(), "9 ".isdigit(), "-9".isdigit())
print("\nisdigit():", "".isdecimal(), " ".isdecimal(), "9".isdecimal(), "9 ".isdecimal(), "9.0".isdecimal(), "-9.0".isdecimal())
print("isspace():", "".isspace(), " ".isspace(),"     ".isspace(), " d ".isspace())
print("", "".isalpha(), " ".isalpha(), "asa".isalpha(), "as2".isalpha())
print("isalnum():", "".isalnum(), "a".isalnum(), "1".isalnum(), "12dd2".isalnum())
s.islower()
m='''
####This is GM message.###
'''
m.startswith("\n")

m.strip("#")
s.upper()
s.capitalize()
s.casefold()
s.center(3,'*')
s.count('is')
s.find('is')
s.casefold()
s.isascii()
s.isdigit()
s.isdecimal()
s.istitle()
s.isupper()
s.maketrans()
s.partition()
s.swapcase()

'''
print(f'length: {s.strip()}')

print("To get ascii for any char: ord():", ord('A'), ord('Z'), ord('a'), ord('z'), "So 'A'< 'a':", 'A' < 'a',
      "'bad'< 'bat':", 'bad'< 'bat')
print("To get char out of ascii provided: chr():", chr(65), chr(90))

print(f"String maths: \nstr + str=","Milind"+"Paradkar", "\n'Milind'+3==> not allowed, so we can use fString here like : f'this is {num} KGs'", "\n\nstr * num:","Milind"*5, " or num * str:", 3*"Paradkar")

'''