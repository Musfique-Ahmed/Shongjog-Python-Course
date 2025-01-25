class Alien:
    def __init__(self, color, heart=0): #constructor
        self.color = color #red, green, blue
        self.heart = heart #attriutes
        self.damage = 5

    def can_fire(self): #method
        if self.color == "red":
            return True
        else: return False

    def fire(self, hero):
        hero.health -= self.damage

class Hero:
    def __init__(self, health=100):
        self.health = health
        self.damage = 10

    def fire(self, alien):
        alien.heart -= self.damage

alien_1 = Alien("red", 15)
print(f"Alien-1 heart: {alien_1.heart}")
alien_2=  Alien("blue", 20)
print(f"Alien-2 heart: {alien_2.heart}")
hero = Hero()
print(f"Hero health: {hero.health}")

alien_1.fire(hero)
print(hero.health)
alien_2.fire(hero)
print(hero.health)

hero.fire(alien_1)
print(alien_1.heart)
hero.fire(alien_2)
print(alien_2.heart)
hero.fire(alien_2)
print(alien_2.heart)