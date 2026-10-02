
gyldig=False

while not gyldig:
    billetter=input("Hvor mange biletter vil du ha?")
    try:
        billetter=int(billetter)
        if 0<billetter<=10:
            gyldig=True
            print(f"Det koster {billetter*150}kr")
        else:
            gyldig=False
            print("Du kan maks kjøpe 10 biletter")
    except ValueError:
        print("skriv inn et heltall")
        gyldig=False
