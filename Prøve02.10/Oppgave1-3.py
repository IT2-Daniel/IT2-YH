
#a)

#minutter = 135
#print(f"{minutter // 60} t og {minutter % 60} min")

#skriver ut tiden 135 minutt i formatet timer og minutter først med // som gir antall ganger det går opp i 60 og så med % som gir resternede minutter


#b)

#fag = "Programmering"
#print(fag[0:4].upper() + fag[-3:])

#Velger et ord "Programmering" og printer indeks 0-3 altså de fire første bokstavene i caps og de siste 3 uendret altså i små bokstaver


#c)

#tall = [3, 8, 1, 6]
#tall.sort(reverse=True)
#print(tall[1], len(tall))

#Lager en liste med tall inni og sorterer den i motsatt stigende rekkefølge og printer så ut element 1 som da blir det andre tallet altså 6


#d)

#total = 0
#for i in range(1, 10, 3):
#    total += i
#print(total)

#setter et tall lik 0 og deretter mens i er mellom 1 og 10 legges i til i total og hopper 3 om gangen så da får vi til slutt 12 ¨


#Oppg 2

#alder = input("Hvor gammel er du? ") #Her må du bruke f.eks int så det blir lest som et tall så det skal funke med resten av koden

#if alder >= 18 #mangler :
#    print("Du er myndig.")
#elif alder = 17: #Her må du ha ==
#    print("Du blir myndig neste år!")
#else:
#    print(f"Du blir myndig om {18 - alder} år.")


#Rettet versjon

#alder = int(input("Hvor gammel er du? "))

#if alder >= 18:
#    print("Du er myndig.")
#elif alder == 17:
#    print("Du blir myndig neste år!")
#else:
#    print(f"Du blir myndig om {18 - alder} år.")




#oppg 3


def dobbel_partall(liste):
    resultat = []
    for tall in liste:
        if tall % 2 == 0:
            resultat.append(tall * 2)
        else:
            resultat.append(tall)
    return resultat

tallene = [1, 2, 3, 4]
nye = dobbel_partall(tallene)
print(nye)
print(tallene)
print(sum(nye) > 10)


#Programmet vil skrive ut 
# [1,4,3,8]
# [1,2,3,4]
# True  

#Dette er fordi Funksjonen skjekker om tallene er delelig med to altså partall og hvis de er dobles de, hvis ikke forblir de som de er
#Da får vi i den første listen som skrives ut altså nye der vi kaller funksjonen: Doble partall, vanlige oddetall
#I andre printer vi bare listen som den er 
#Og i den tredje skjekker vi om summen av "nye" er over 10 som den er 