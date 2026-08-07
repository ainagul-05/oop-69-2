class Hero:
    def __init__(self , name , lvl , health , strength):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength

    def greet(self):
        print (f"Привет, я {self.name},  мой уровень{self.lvl}")
    def attack(self):
        print(f"{self.name} наносит удар! " )
        self.strength -= 1
    def rest(self):
        print(f"{self.name} отдыхает")
        self.health += 1

manas = Hero("Manas", 100, 500, 1000)
semetei = Hero("Semetei",100,400,800 )

print(manas.name)
manas.greet()
semetei.rest()
print(semetei.health)