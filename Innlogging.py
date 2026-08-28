Inlogget: bool=False

Rett_Brukernavn: str="potet1"
Rett_passord: str="MykPlomme26"

while not Inlogget:
    brukernavn= str(input())
    

    if brukernavn!=Rett_Brukernavn:
        print("bruker eksisterer ikke")
        break


    passord=str(input())
    if passord!=Rett_passord:
        print("feil passord")
        break


    if passord==Rett_passord and brukernavn==Rett_Brukernavn:
        inlogget=True
        print("Du er inlogget")

  






