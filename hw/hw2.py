
class Hero :

    def __init__(self, name , lvl , health , strength):

        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength

    def greet (self):
        print(f"Привет , я {self.name} ")
    def attack(self):
        print(f"{self.name}  наносит удар ")
    def rest(self):
        print(f"{self.name}   отдыхает и восстаннавливает здоровье  ")

class WarriorHero(Hero):
    def __init__(self , name , lvl , health , strength , stamina):
        super().__init__( name , lvl , health , strength)
        self.stamina = stamina
    def attack(self):
        print(f" {self.name} : Воин атакует мечом ! ")


class MageHero(Hero):
    def __init__(self , name , lvl , health , strength , mana):
        super().__init__( name , lvl , health , strength)
        self.mana = mana
    def attack(self):
        print(f"{self.name} : Маг кастует заклинание !")


class AssassinHero(Hero):
    def __init__(self , name , lvl , health , strength , stealth):
        super().__init__( name , lvl , health , strength)
        self.stealth = stealth
    def attack(self):
        print(f" {self.name} :Ассасин атакует из под тишка !")

warrior = WarriorHero ("Воин" , 100 , 1000, 200 , 800 )
mage = MageHero ("Маг" , 100 , 800 , 250 , 1000 )
assassin = AssassinHero("Ассасин" , 100 , 900, 220 , 950)

hero1 = input("Выберите героя : Warrior/ Mage / Assassin :" )


import random

hero2 =  {
          1:"Warrior",
          2:"Mage" ,
          3:"Assassin"
}

bot_hero = random.randint(1,3)

if hero1 == "Warrior":
    player = warrior
elif hero1 == "Mage" :
    player = mage
else :
    player = assassin

enemy = hero2[bot_hero]


    if player == warrior and enemy == assassin:

        print("Вы победили!")

    elif player == assassin and enemy == mage:

        print("Вы победили!")

    elif player == mage and enemy == warrior:

        print("Вы победили!")

    else:

        print(f"{enemy.name} победил!")









