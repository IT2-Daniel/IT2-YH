navn="Peder Olsen"
sult=5
energi=5
glede=5

navn2="Alejandro"
sult2=5
energi2=5
glede2=5


def begrens(verdi):
    return max(0, min(10,verdi))

sult=begrens(sult-3)
sult2=begrens(sult2-3)

def visstatus():
    print(f"\033[34m{navn}: sult: {sult}, energi: {energi}, glede:{glede}\033[0m ")
    print(f"\033[33m{navn2}:sult: {sult2}  energi: {energi2}   glede:{glede2}\033[0m")
    print("\033[35m**---------------------**\033[0m")
    if sult>=8:
        print(f"\033[31m{navn} er sulten ):\033[0m")
    if energi<=2:
        print(f"\033[94m{navn} er trøtt\033[0m")
    if sult2>=8:
        print(f"\033[31m{navn2} er sulten ):\033[0m")
    if energi2<=2:
        print(f"\033[94m{navn2} er trøtt\033[0m")

def mating():
    global sult,glede
    sult=begrens(sult-3)
    glede=begrens(glede+1)
    print(f"du matet {navn}")

def mating2():
    global sult2,glede2
    sult2=begrens(sult2-3)
    glede2=begrens(glede2+1)
    print(f"du matet {navn2}")

def leking():
    global sult,energi,glede
    if energi<=2:
        print(f"{navn} har ikke energi til å leke")
        return
    if sult>=8:
        print(f"{navn} er for sulten til å leke")
        return
    glede=begrens(glede+3)
    energi=begrens(energi-2)
    sult=begrens(sult+1)
    print(f"du lekte med {navn}")

def leking2():
    global sult2,energi2,glede2
    if energi2<=2:
        print(f"{navn2} har ikke energi til å leke")
        return
    if sult2>=8:
        print(f"{navn2} er for sulten til å leke")
        return
    glede2=begrens(glede2+3)
    energi2=begrens(energi2-2)
    sult2=begrens(sult2+1)
    print(f"du lekte med {navn2}")


def sove():
    global sult,energi
    energi=begrens(energi+4)
    sult=begrens(sult+1)
    print(f"{navn} sov")

def sove2():
    global sult2,energi2
    energi2=begrens(energi2+4)
    sult2=begrens(sult2+1)
    print(f"{navn2} sov")

def tid():
    global sult,glede
    sult=begrens(sult+1)
    glede=begrens(glede-1)

def tid2():
    global sult2,glede2
    sult2=begrens(sult2+1)
    glede2=begrens(glede2-1)

while True:
    visstatus()
    print("1: Mate  2: Leke 3: Sove 4:Avslutt")
    valg=input("velg:")
    print(f"velg dyr 1: {navn}  2: {navn2}")
    dyr=int(input())

    if valg=="1" and dyr==1:
        mating()
    elif valg=="1" and dyr==2:
        mating2()
    elif valg=="2" and dyr==1:
        leking()
    elif valg=="2" and dyr==2:
        leking2()
    elif valg=="3" and dyr==1:
        sove()
    elif valg=="3" and dyr==2:
        sove2()
    elif valg=="4":
        break
    else:
        print("ugyldig valg")
        continue
    print("\033[35m**---------------------**\033[0m")
   

    tid()
    tid2()
