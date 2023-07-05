class Pet:
    def __init__(self):
        name = str(input("Please input the name of your pet: "))
        animal_type = str(input("What type of animal is your per?: "))
        age = int(input("What is the age of your pet?: "))
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age