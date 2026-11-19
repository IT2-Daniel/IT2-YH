
from random import randint


class Character:
    def __init__(self, hp=100, baseDamage=10):
        self.hp = hp #helse
        self.baseDamage = baseDamage #baseskade
        self.advantage = False #bestemmer om en har advantage

    #Hovedklassen som alle andre arver fra, oppretter og setter standardverdier for attributene som deles av alle klassene

    def roll(self):
        #Ruller en terning fra en til 20
        print("Advantage status:", self.advantage)

        if self.advantage:
            #hvis man har advatage ruller man 2 ganger og bruker det høyeste
            roll1 = randint(1, 20)
            roll2 = randint(1, 20)

            print("Terning 1:", roll1)
            print("Terning 2:", roll2)

            #vanlig kast uten advantage
            roll = max(roll1, roll2)
            #advantage forsvinner etter en tur
            self.advantage = False

        else:
            roll = randint(1, 20)

        return roll #sender resultatet tilbake til metoder som kaller denne 


'''Character
legger grunnlaget for de andre klassene og stter standarverdier for og definerer hp og basedamage
og håndterer rng i spillet ved metoden roll som brukes av alle klasser

'''


class Player(Character):
    #arver fra Character og legger til andre attributter som mp, speed(irrelevant ettersom at å gjøre noe med det ble nedprioritisert)
    # samt abilityBaseDamage, ability1 og ability2 og items
    def __init__(self, hp, mp, speed, baseDamage, abilityDamageBase):
        super().__init__(hp, baseDamage)

        self.mp = mp
        self.speed = speed
        self.abilityDamageBase = abilityDamageBase

        self.ability1 = None
        self.ability2 = None


        self.items = ["Mana potion","Mana potion", "Health potion","Health potion"]

    
    

    def take_turn(self, enemy):
        #fikser ka som skjer når det er din tur
        print("\nDin tur!")
        print("1: Base attack | 2: Abilities | 3: Run | 4: Items")

        #her velger du hva du vil bruke turen din på
        try:
            valg = int(input("> "))
        except ValueError:
            print("Ugyldig valg \n Du mister turen din som straff for denne enorme tabben")
            return True

        if valg == 1:
            rollDamage = self.roll()

            if rollDamage > 1:
                damage = int(self.baseDamage * rollDamage / 10)
                enemy.hp -= damage
                print("Du gjorde", damage, "skade!")
            else:
                self.hp -= 1
                print("Du bommet og fikk skulderen ut av ledd!")

        elif valg == 2:
            print("1:", self.ability1[0])
            print("2:", self.ability2[0])

            try:
                valgAbility = int(input("> "))
            except ValueError:
                print("Ugyldig valg \n du mister turen din for denne enorme tabben")
                return True

            if valgAbility == 1:
                name, cost, ability = self.ability1
            elif valgAbility == 2:
                name, cost, ability = self.ability2
            else:
                print("Ugyldig valg \n du mister turen din")
                return True

            if self.mp >= cost:
                damage = ability()
                self.mp -= cost

                if damage is not None:
                    enemy.hp -= damage
                    print(name, "gjorde", damage, "skade!")
            else:
                print("Du har ikke nok MP!")

        elif valg == 3:
            print("Du stikker av.")
            print("D e svakt ass.")
            print("Du kommer ikke til Valhall hvis du fortsetter sånn.")
            print("Arr på ryggen er en krigers skam.")
            print("-100 aura")
            return False

        elif valg == 4:
            #skjekker hvor mange items du har
            if len(self.items) == 0:
                print("Du har ingen items!")
                return True

            print("Dine items:")

            #lager tall for items i inventory
            for i in range(len(self.items)):
                print(i + 1, self.items[i])

            try:
                valgItem = int(input("> "))
            except ValueError:
                print("Ugyldig valg \n du mister turen din")
                return True

            if valgItem < 1 or valgItem > len(self.items):
                print("Ugyldig valg \n du mister turen din")
                return True

            item = self.items[valgItem - 1]

            if item == "Mana potion":
                #skjekker om du er Wizard
                if isinstance(self,Wizard):
                    self.mp=20
                else:
                    self.mp = 10
                print("Du drikker en mana potion! Mana gjenopprettet.")

            elif item == "Health potion":
                self.hp += 50
                print("Du drikker en health potion! +50 HP.")

            self.items.pop(valgItem - 1)

        else:
            print("Ugyldig valg \n du mister turen din")

        return True

'''
her er da attributter og metoder som deles av alle spillerklasser for eksempel tursystemet til combaten og alt som skjer der 
og items og andre stats som nevnt lenger oppe
'''


class Brawler(Player):
    def __init__(self, hp, mp, speed, baseDamage, abilityDamageBase):
        super().__init__(hp, mp, speed, baseDamage, abilityDamageBase)

        #Definierer ability 1 og 2 og hvor mye mana de koster
        self.ability1 = ("Enrage", 2, self.enrage)
        self.ability2 = ("Leaping Strike", 3, self.leapingStrike)

    #bestemmer hva som skjer når du bruker enrage(ability1)
    def enrage(self):
        self.advantage = True
        print("Du går berserk! Neste terningkast får Advantage.")
        return None

    #bestemmer hva som skjer når du bruker Brawlers ability 2 og bestemme rskade ut i fra abilityBaseDamage og terningen
    def leapingStrike(self):
        roll = self.roll()
        damage = int(self.abilityDamageBase * roll / 10)
        return damage

'''spesialisert spillerklasse brawler, arver fra Player som igjen arver fra Character
Legger til attributtene enrage og leapingStrike og metoder for dem 

'''


class Wizard(Player):
    def __init__(self, hp, mp, speed, baseDamage, abilityDamageBase):
        super().__init__(hp, mp, speed, baseDamage, abilityDamageBase)

        #definerer ability 1 og 2 og hvor mye mana de koster
        self.ability1 = ("Fireball", 3, self.fireball)
        self.ability2 = ("Lightning Strike", 10, self.lightningStrike)
        #begrenser bruk av lightningStrike fordi den e lowk  alt for op når mana potion finnes
        self.lightningUses=2

    #bestemmer skaden til fireball med terning og abilityBaseDamage
    def fireball(self):
        roll = self.roll()
        damage = int(self.abilityDamageBase * roll / 10)
        return damage

#bestemmer skade til lightningStrike med roll og abilityBaseDamage pluss en liten ekstra multiplier
    def lightningStrike(self):
        #skjekker om du har flere bruk av lightning
        if self.lightningUses<=0:
            print("du e tom for lightning")
        else:
            #vanlig bruk av lightning
            roll = self.roll()
            damage = int(self.abilityDamageBase * 2.5 * roll / 10)
            #mister en bruk av lightning når du bruker det
            self.lightningUses-=1
            return damage

        
'''spesialisert spillerklasse som fokuserer mer på abilities og har en slags ult 
ellers samme konsept som brawler

'''

class Enemy(Character):
    def __init__(self, hp, baseDamage):
        super().__init__(hp, baseDamage)

    def attack(self, player):
        roll = self.roll()

        if roll > 1:
            damage = int(self.baseDamage * roll / 10)
            player.hp -= damage
            print("Fienden gjorde", damage, "skade!")
        else:
            print("Fienden bommet!")

        '''Enemy arver direkte fra Characterog bruker bare attributtene hp og baseDamage
        samt metoden roll
        
        '''


#Funksjonen bak selve kampen
def start_combat(player, enemy):
    print("KAMPEN STARTER!")

    #viser relevante stats underveis
    while player.hp > 0 and enemy.hp > 0:
        print("\nDine HP:", player.hp, "| MP:", player.mp)
        print("Fiendens HP:", enemy.hp)

        if not player.take_turn(enemy):
            break

        if enemy.hp <= 0:
            break

        enemy.attack(player)

    print("\n--- KAMPEN ER OVER ---")
    print("Dine HP:", player.hp)
    print("Fiendens HP:", enemy.hp)

    if player.hp <= 0:
        print("Du tapte!")
    elif enemy.hp <= 0:
        print("Du vant!")


#bare en test som ble gjort underveis
if __name__=="__main__":
    player = Brawler(100, 10, 5, 10, 20)
    enemy = Enemy(60, 8)

    start_combat(player, enemy)