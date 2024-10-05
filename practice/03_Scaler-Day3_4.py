print("day 3")
print(type(None))
print(bool(None))

#Day 3
    #missed
    # while loop


#day 4
print()
print(range(5))
print(list(range(5)))
print(list(range(1)))
print(list(range(2)))
print(list(range(10)))
print("list(range(0, 0)):", list(range(0, 0)))
print("list(range(0, 1)):", list(range(0, 1)))
print("list(range(1, 2)):", list(range(1, 2)))
print("list(range(1, 10)):", list(range(1, 10)))
print("\nlist(range(1, 10, 2)):", list(range(1, 10, 2)))
print(list(range(1, 10, 3)))
print(list(range(1, 10, 4)))
print(list(range(10, -2)))
print("list(range(10, 0, -2)):", list(range(10, 0, -2)))
print(list(range(10, 2, -2)))
print(list(range(10, 1, -2)))
print(list(range(-5, 2, 2)))
print(list(range(-5, 2, 1)))
print(list(range(-1, -10, 1)))
print(list(range(-1, -10)))
print(list(range(-10, -1)))
print(list(range(-1, -10, -1)))

print()
n = 10
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
for i in range(1, n+1):
    if i % 2 == 1:
        print(i)

'''
print(" ")
# smarter code
for i in range(2, n+1, 2):
    print(i)

for i in range(1, n+1, 2):
    print(i)


print(" Print 2- n separated by space ")
n=20
for i in range(2, n+1):
    print(i, end=' ')
print("\nsomething")
b=10
for j in range(b, 0, -1):
    print(j, end=" ")
print("\nsomething")
n = 10
for j in range(0, n):
    print(n - j, end=" ")
#sum of 1-n
n = int(input("Enter number for sum of 1 - n:"))
summ = 0
for i in range(n + 1):
    summ += i

print(summ)
'''
print(88888)
for i in range(1, 17, 3):
    print(i, sep=",", end=",")

'''
HW: Write a while loop to print the following numbers:
Exact output:
1, 3, 7, 13, 21, 31, 43
'''
print("\nPrint this: 1, 3, 7, 13, 21, 31, 43")
for i in range(1, 7):
    init = 1;
    addition = 2;
    addition += init;
    init = addition
    print(addition, end=", ")

#Day 7
a= [1,2,3,4,5,6,7,8,9,10]
a[6:3:-2] #it shows index 6,4, and stops at 3+1 (go in negative still stop --1=+1 step back
a[::-1] #still prints all list in negative direction

#Memorise lambda
#Memorise map function

b = 1, 'a', "b", 6.8
print(b)

m = [(1, "Milind"), (2, "shruti")]

for elem in m:
    print(elem[0])
