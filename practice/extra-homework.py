class fruits:
    def __init__(self, price):
        self.price = price


obj = fruits(50)
obj.quantity = 10
obj.bags = 2

print(obj.quantity + len(obj.__dict__))


class Student:
    def __init__(self, roll, marks):
        self.roll = roll
        self.marks = marks

    def display(self):
        print('Roll:', self.roll, 'Marks:')


student1 = Student(34, 'A')
# student1.age = 17
print(student1.display())


class Player:
    # class variables
    club = 'United'
    sport = 'Football'

    def __init__(self, name):
        # Instance variable
        self.name = name

    def show(self):
        print('Name:', self.name, 'Club:', self.club, 'Sports:', self.sport, end=" ")


p1 = Player('Sanjay')
p1.club = 'Real Madrid'
p1.show()

p2 = Player('Ravi')
p2.sport = 'Tennis'
p2.show()


class solution:
    def initial(self, sets):
        return self.final(sets)

    def final(self, sets):
        return list(map(lambda x: ((x ** 3) % 2 == 0, x ** 3), sets))


print(solution().initial([4, 5, 6]))


class Student:

    def __init__(self, marks1, marks2, credits1, credits2):
        # YOUR CODE GOES HERE
        self.marks1 = marks1
        self.marks2 = marks2
        self.credits1 = credits1
        self.credits2 = credits2

    def grade_point_average(self):
        gpa = 0
        g1 = self.points(self.marks1)
        g2 = self.points(self.marks2)
        if g1 == 0 and g2 == 0:
            return -1.0
        else:
            gpa = ((g1 * self.marks1) + (g2 * self.marks2)) / (g1 + g2)
        return gpa

    def points(self, marks):
        if marks >= 90:
            return 10
        elif marks >= 75:
            return 9
        elif marks >= 60:
            return 8
        elif marks >= 45:
            return 7
        else:
            return 0


s1 = Student(12, 12, 12, 12)
s1.grade_point_average()


class fruits:
    def __init__(self, price):
        self.price = price


obj = fruits(50)
obj.quantity = 10
obj.bags = 2

print("jjjjjjjjjjj",obj.__dict__)

ls = [1150, 'sea_level', 909]
ls1 = [8,7,6]
# print(max(tup))
print("+++++ list addition is allowed +++++", ls + ls1)

tup = (1150, 'sea_level', 909)
tup1 = (8,7,6)
# print(max(tup))
print(tup[2])
print("+++++ tuple addition is allowed +++++", tup + tup1)

set1 = {1, 2, 4}
set2 = {4, 5, 6}
# print(set1[0]) # Sets are unordered so indexing is not allowed
# Class 'set' does not define '__getitem__', so the '[]' operator cannot be used on its instances
print(" ++++ set addition is not allowed")
# print((set1 + set2)) ERROR unsupported operand type(s) for +: 'set' and 'set'

print("START")








