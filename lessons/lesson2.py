"""Наследование"""
# Родительский класс / Супер класс
class Hero :
    #Конмтруктор класса
    def __init__(self, name , lvl , hp):
        #Атрибуты обьекта класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
     #методы класса
    def action(self): #метод обьекта
        print(f'{self.name} this is my base action')

# Дочерний класс
class MageHero(Hero) :

    def __init__(self, name , lvl , hp, mp ):
        #Атрибуты обьекта класса
      super().__init__(name, lvl,hp)
      self.mp = mp #так нужно добавлять новые атрбуды для дочернего класса

    def cast_spell(self):
        print(f"{self.name} Cast fire boll !!!")  #дочерний класс не передает ничего к родительскому классу


kirito = MageHero("Kirito", 100 , 1000 ,709)
asuna = Hero("Asuna", 111, 1111)

# kirito.action()
# asuna.action()
# kirito.cast_spell()

class Fly:
    def action(self):
        print("Fly")


class Swim:
    def action(self):
        print("Swim")


class Animal(Swim , Fly):
    def action(self):
        print("Base action")

donald_duck = Animal()
donald_duck.action()
print(Animal.mro()) #механизм который отвечает за порядок классов

class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        print("B")
class C(A):
    def action(self):
        print("C")
class D(B,C):
    def action (self):
        super().action()
        print("D")

test = D()
test.action()







