
gyldig=False
try:
    while not gyldig:
        Tall=input("skriv et tall")
        try:
            Tall=int(Tall)
            gyldig=True
        except ValueError:
            print("Skriv inn et heltall tulling")
        except KeyboardInterrupt:
            print("Program avsluttet av bruker")
        
        if 101> Tall>0:
            gyldig=True
        else:
            print("Tallet må være mellom 1 og 100")
            gyldig=False
except KeyboardInterrupt:
    print("Program avsluttet av brukeren")

else:
    print(f"Du skrev inn {Tall}")
