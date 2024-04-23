class Employee:
    def __init__(self, name, age, position):
        self.__name = name
        self.__age = age
        self.__position = position

    def __str__(self):
        return f"{self.name} is {self.age} and works as a {self.position}"

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def position(self):
        return self.__position

    @name.setter
    def name(self, new_name):
        if not new_name.isalpha():
            raise ValueError('Name should only consist of letters')
        self.__name = new_name

    @position.setter
    def position(self, new_position):
        self.__position = new_position


if __name__ == '__main__':
    mark = Employee('Mark', 32, 'manager')
    print(mark.name)
    print(mark.age)
    print(mark.position)
    print(mark)