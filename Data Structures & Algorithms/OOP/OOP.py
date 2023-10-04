class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hell my name is {self.name} and i am {self.age} years old")

person1 = person("zack", 21)
person1.introduce()

person2 = person("Bob", 25)
person2.introduce()