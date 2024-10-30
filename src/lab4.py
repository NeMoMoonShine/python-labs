class ArtificialChristmasTree:

    def __init__(self, manufacturer="None", height=0, price=0, material="None", public_number = 0, public_string = "None"):
        self.__manufacturer = manufacturer
        self.__height = height
        self.__price = price
        self.__material = material
        self.public_number = public_number
        self.public_string = public_string

    def get_manufacturer(self):
        return self.__manufacturer

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def __str__(self):
        return f"Виробник: {self.__manufacturer}, Висота: {self.__height} см, Ціна: {self.__price} грн, Матеріал: {self.__material}"

    def __repr__(self):
        return f"ArtificialChristmasTree (manufacturer='{self.__manufacturer}', height={self.__height}, price={self.__price}, material='{self.__material}')"

    def __del__(self):
        print(f"Об'єкт видалено")


def main():
    tree1 = ArtificialChristmasTree("Виробник 1", 150, 1000, "Пластик")
    tree2 = ArtificialChristmasTree("Виробник 2", 180, 1500, "Метал")
    tree3 = ArtificialChristmasTree("Виробник 3", 200, 2000, "Пластик та метал")
    tree_default = ArtificialChristmasTree()

    print(tree1)
    print(type(tree2))
    print(tree3)
    print(tree_default)
    print(repr(tree1))
    print(repr(tree2))
    print(repr(tree3))
    print(repr(tree_default))

if __name__ == "__main__":
    main()