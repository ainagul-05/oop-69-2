
from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name , lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f'Привет,я {self.name},мой уровень{self.lvl}')

    def rest(self):
        print(f'{self.name} отдыхает')
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def __init__(self, name, lvl, health, strength):
        super().__init__(name, lvl, health, strength)
    def attack(self):
        print(f"{self.name} атакует мечом")

class Mage(Hero):
    def __init__(self,name, lvl, health, strength):
        super().__init__(name, lvl, health, strength)
    def attack(self):
        print(f"{self.name} использует магию")

class Assassin(Hero):
     def __init__(self, name, lvl, health, strength):
         super().__init__(name, lvl, health, strength)
     def attack(self):
         print(f'{self.name} атакует из-под тишка')

warrior = Warrior('Warrior', 1000 , 100 , 500)
mage = Mage('Mage', 1000 , 200 , 600)
assassin = Assassin('Assassin', 1000 , 300 , 700)

warrior.greet()
mage.greet()
assassin.greet()

warrior.attack()
mage.attack()
assassin.attack()


warrior.rest()
mage.rest()
assassin.rest()


