import random as r

pts_spiller: int=0
pts_bot: int=0
uavgjort: int=0

while pts_spiller <3 and pts_bot<3:
    valg_spiller=str(input("stein,saks,papir"))
    valg_bot=r.choice(["stein","saks","papir"])

    if valg_spiller not in ["stein","saks","papir"]:
        print("ugyldig")
        

    if valg_spiller==valg_bot:
        uavgjort+=1
        print(f"Du valgte {valg_spiller}, boten valgte {valg_bot}. {resultat}")
        print(f"stilling: Spiller:{pts_spiller}-bot:{pts_bot}-uavgjort:{uavgjort}")
    elif (valg_spiller=="stein" and valg_bot=="saks")or\
        (valg_spiller=="papir" and valg_bot=="stein")or\
    (   valg_spiller=="saks" and valg_bot=="papir"):
            pts_spiller+=1
            resultat: str="du vant"
            print(f"Du valgte {valg_spiller}, boten valgte {valg_bot}. {resultat}")
            print(f"stilling: Spiller:{pts_spiller}-bot:{pts_bot}-uavgjort:{uavgjort}")
    else:
            pts_bot+=1
            resultat: str="bot vant"
            print(f"Du valgte {valg_spiller}, boten valgte {valg_bot}. {resultat}")
            print(f"stilling: Spiller:{pts_spiller}-bot:{pts_bot}-uavgjort:{uavgjort}")

            
            

print(f"spillet er over {resultat}")
print(f"Endelig stilling: Spiller:{pts_spiller} - bot:{pts_bot} - Uavgjort:{uavgjort}")

