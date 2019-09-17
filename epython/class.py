class student:
    def __init__(self, name):
        self.name=name

    def display(self):
        print(self.name,end="")
    
x=student("rsm")
x.display()    
print(x.name)

class amulya(student):
    pass

y =amulya("hero")
y.display()