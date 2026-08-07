class Hero :
    # Конcтруктор класса
    def __init__(self, name , lvl , hp):
        #Атрибуты обьекта класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self): #метод обьекта к5
        print(f'{self.name} this is my base action')

#Обьект / экземпляр на основе класса
kirito = Hero("Kirito", 100 , 1000) #
asuna = Hero("Asuna", 111 , 1111)  #


print(kirito.name)
print(kirito.lvl)
print(kirito.hp)

my_int = 123
my_str = "Text"
my_float = 1.23
my_bool = True
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)

print(type(kirito))

kirito.action()
asuna.action()


# SELF считается обьязательным параметром в конструкторе класса , магаческих методах , публичных и проперти методах

# HeroMage  camel case верблюжая  нотация только для классов !
# mage_hero  snack case  змеийная нотация




