

gyldig=False
while not gyldig:
    tall1=input("Skriv inn tall")
    tall2=input("skriv inn tall")
    try:
        tall1=float(tall1)
        tall2=float(tall2)
        resultat=tall1/tall2
        gyldig=True
    except ValueError:
        print("Skriv inn tall dust")
    except ZeroDivisionError:
        print("du kan ikke dele på null")
    finally:
        print("forsøk på divisjon avsluttet")
    break
        
print(f"{tall1}/{tall2}={resultat}")