class Car:
    def __init__(self, name, year, owner):
        self.name = name
        self.year = year
        self.owner = owner

    def get_info(self):
        print(f"Автомобиль {self.name}")
        print(f"Год выпуска {self.year}")
        print(f"Владелец {self.owner}")

