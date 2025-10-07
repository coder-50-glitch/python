class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age, color):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        self.color = color

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3, "red")

print(dog1.name) 
print(dog1.species)
print(dog1.color)

dog2 = Dog("Lusi",4, "grey")
print(dog2.name) 
print(dog2.species)
print(dog2.color)
print(dog2.age)

class labrador(Dog):
    master_name="Rajashree"
    
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
        self.bark="heavily"  # class labrador attribute
       
lab1=labrador("elon",12,"black")
print("{} is a {} colored dog. it is {} years age".format(lab1.name,lab1.color,lab1.age))
print("{} barks {}".format(lab1.name, lab1.bark))
print("master name",labrador.master_name)