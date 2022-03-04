class Person:
    """
        Representation of a person, which includes name, gender, date of birth
    """

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Gender: {self.gender}, Age: {self.age}'


harry = Person('Harry', 'Male', 47)

print(harry)
