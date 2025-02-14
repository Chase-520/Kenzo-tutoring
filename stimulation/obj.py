class student:
    def __init__(self, n :str, i :int , g:str, h :float):
        self.name :str = n
        self.intelligence :int = i
        self.gender :str = g
        self.height :float = h

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender



x = student(n="Cindy",i=100,g="Bread",h=200)
y = student(n="Timothy", i=32, g="Female",h=304)

print(x.getName())
print(y.getName())





