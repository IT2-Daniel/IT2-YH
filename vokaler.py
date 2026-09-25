def fjernVokaler(ord):
    vokaler="aeiouyæøåAEIOUYÆØÅ"
    resultat=""

    for bokstav in ord:
        if bokstav not in vokaler:
            resultat+=bokstav
    return resultat


ord=str(input("skriv et ord:"))
print(fjernVokaler(ord))