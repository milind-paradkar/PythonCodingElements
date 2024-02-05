class fruits:
    def __init__(self, price):
        self.price = price

obj=fruits(50)
obj.quantity=10
obj.bags=2

print(obj.quantity+len(obj.__dict__))

class Student:
    def __init__(self,roll,marks):
        self.roll = roll
        self.marks = marks
    def display(self):
        print('Roll:', self.roll,'Marks:')

student1 = Student(34,'A')
#student1.age = 17
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