from pygame import *
from random import randint

minTur=True
Advantage=False

class Character:
    def __init__(self):
        self.filler=1

    def roll(self):
        if Advantage==True:
            roll1=randint[1,20]
            roll2=randint[1,20]
            if roll1>roll2:
                roll=roll1
            else:
                roll=roll2
        else:roll=randint[1,20]


class Player(Character):
    def __init__(self,hp,mp,speed,baseDamage,abilityDamageBase,ability1,ability2):
        self.hp=hp
        self.mp=mp
        self.speed=speed
        self.baseDamage=baseDamage
        self.abilityDamageBase=abilityDamageBase
        self.ability1=ability1
        self.ability2=ability2

    def minTur(self):
        if minTur==True:
            print("1:Base attack | 2: Abilities | 3: move")
            valg=int(input())

            if valg==1:
                    rollDamage=randint[1,20]
                    if rollDamage>1:
                        damage=self.baseDamage*rollDamage/10
                    else:
                        self.hp-=1
                        print("Du bommet og fikk skulderen ut av ledd")
                    

            elif valg==2:
                print("1: ability1 | 2: ability2")
                valgAbility=int(input())
                if valgAbility==1 and self.mp>=3:
                    #kalle ability1 for klassen
                    minTur=False
                elif valgAbility==2:
                    rollAbility=randint[1,20]
                    if rollAbility>1:
                      a=a # kalle ability2
                    else:
                        self.hp-=3
                        print("du snublet over våpenet ditt")



class Brawler(Player):
    def __init__(self,hp,mp,speed,baseDamage,abilityDamageBase,ability1,ability2):
        super().__init__(hp,mp,speed,baseDamage,abilityDamageBase,ability1,ability2)

    super().minTur()


    def enrage():
        mp-=2
        Advantage=True
        abilityDamageBase=0


    def leapingStrike():
        mp-=3
        abilityDamageBase=5

    
            

class Wizard(Player):
    def __init__(self,hp,mp,speed,baseDamage,abilityDamageBase,ability1,ability2):
        super().__init__(hp,mp,speed,baseDamage,abilityDamageBase,ability1,ability2)

    super().minTur()

    def fireball():
        mp-=3
        abilityDamageBase=5

    def lightningStrike():
        mp-=7
        abilityDamageBase=10


class Enemy(Character):
    def __init__(self,hp,baseDamage):
        self.hp=hp
        self.baseDamage=baseDamage 
