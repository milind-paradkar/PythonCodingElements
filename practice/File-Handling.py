# File Handling

print("open modes:")
print("r: default, read file. File should exist. Otherwise error")
print("w: writes from start of file. Creates if does not exist.")
print("r+: read and write. Error if file does not exists.")
print("w+: read and write. Creates file if not exists")
print("a: append. writes at end of file. Keeps existing contents. Creates file if not exists.")
print("a+: append and read.")
print("")

'''
file = open("Scaler.txt","w")
file.write("This file is created through Python's builtin open(file,'w'). And it overwrites.")
file.close()
'''
file = open("Scaler.txt", "a")
file.write("This statement should get appended.")
file.write("and one more time.")
file.close()

f1 = open("Scaler-append.txt", "a")
f1.write(" This Content is added at the end of file.")
f1.close()

f1 = open("Scaler-append.txt", "w")
f2 = open("Scaler-append.txt", "w")  # Writing same file by another variable.
f1.write(" This Content is added at the end of file by f1.")
f2.write(" This Content is added at the end of file by f2.")

lines = ["This is line1", "this is line2", "this is line 3"]
f2.writelines(lines)

f3 = open("Scaler-append.txt", "r+")
# f3.writelines(lines)
data = f3.read(5)
print("data:", data, data is None)

print('1' == 1)


def testLeap(x):
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    x = int(x)
    print("aa:", x % 400 == 0)
    if x % 400 == 0:
        return 1
    if x % 4 == 0 and x % 100 != 0:
        return 1
    return 0


print(testLeap(1600))
str1 = "quick brown fox word!"
print(str1[12:15], str1[:5], str1[-5:-1], str1[8:110], str1[-4:])
s = "My PO Box number is 310"
print(s.isalnum(), s.islower(), s.startswith('My P'), s.isspace())

s = "hello"
print(s[0:9])
# print( s[9] )
print(s[:: -1])
