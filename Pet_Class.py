class Pet:
    def __init__(self):
        name = str(input("Please input the name of your pet: "))
        animal_type = str(input("What type of animal is your per?: "))
        age = int(input("What is the age of your pet?: "))
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    def get_name(self):
        print("The name of the pet is", self.__name)
    def set_name(self):
        self.__name = str(input("What name do you want to set for your pet?: "))
        print("The name is now set to", self.__name)
    def get_animal_type(self):
        print("The type of animal of your pet is:",self.__animal_type)
    def set_animal_type(self):
        self.__animal_type = str(input("What type of animal do you want to set for your pet?: "))
        print("The type of animal is now set to", self.__animal_type)
    def get_age(self):
        print("The age of your pet is", self.__age, "years old")
    def set_age(self):
        self.__age = int(input("What age do you want to set for your pet?: "))
        print("The age is now set to", self.__age)