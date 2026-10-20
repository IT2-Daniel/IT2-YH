def begrens(verdi):
    return max(0, min(10, verdi))


class Dyr:
    def __init__(self,navn):
        self.navn=navn
        self.sult=5
        self.energi=5
        self.glede=5
        self.alder=0

    def mate(self):
        self.sult = begrens(self.sult - 3)
        self.glede = begrens(self.glede + 1)
        print(f"Du ga {self.navn} mat.")

    def leke(self):
        if self.energi<=2:
            print(f"{self.navn} er for trøtt til å leke")
            return
        self.glede=begrens(self.glede+3)
        self.energi=begrens(self.energi-2)
        self.sult=begrens(self.sult+1)

    def bade(self):
        self.glede=begrens(self.glede-1)
        self.energi=begrens(self.energi-1)

    def sove(self):
        self.energi=begrens(self.energi+4)
        self.sult=begrens(self.sult+1)


    def tiden_gaar(self):
        self.sult = begrens(self.sult + 1)
        self.glede = begrens(self.glede - 1)
        self.alder+=1

    def visstatus(self):
        print(f"{self.navn}: sult {self.sult}   energi {self.energi}    glede {self.glede}  alder {self.alder} ")
        if self.sult>=8:
            print(f"{self.navn} er sulten")
        if self.energi<=2:
            print(f"{self.navn} er trøtt")

class Hund(Dyr):
    def leke(self):
        super().leke()
        print("voff")

class Katt(Dyr):
    def mate(self):
        super().mate()
        print("mjau")
    def leke(self):
        super().leke()
        if self.energi<=3:
            print(f"{self.navn} gidder ikke å leke")
            return



Peder=Dyr("Peder Olsen")
Alejandro=Dyr("Alejandro")


dyrene=[Dyr("Peder Olsen"), Hund("Alejandro"), Katt("Fridtjof")]

for dyr in dyrene:
    dyr.tiden_gaar()

for dyr in dyrene:
    dyr.visstatus()

def velg_dyr(dyrene):
    for i, dyr in enumerate(dyrene):
        print(f"{i + 1}: {dyr.navn}")
    try:
        return dyrene[int(input("Hvilket dyr? ")) - 1]
    except (ValueError, IndexError):
        print("Ugyldig dyr.")
        return None


dyrene=[Dyr("Peder Olsen"), Dyr("Alejandro"), Dyr("Fridtjof")]

while True:
    print()
    for dyr in dyrene:
        dyr.visstatus()
    print("1: Mate  2: Leke  3: Sove   4: bade  5: Adopter nytt dyr  0: Avslutt")
    valg = input("Velg: ")

    if valg == "0":
        break
    elif valg == "5":
        dyrene.append(Dyr(input("Navn på det nye dyret: ")))
    elif valg in ["1", "2", "3", "4"]:
        dyr = velg_dyr(dyrene)
        if dyr is None:
            continue
        if valg == "1":
            dyr.mate()
        elif valg == "2":
            dyr.leke()
        elif valg == "3":
            dyr.sove()
        elif valg==4:
            dyr.bade()
    else:
        print("Ugyldig valg.")
        continue

    for dyr in dyrene:
        dyr.tiden_gaar()