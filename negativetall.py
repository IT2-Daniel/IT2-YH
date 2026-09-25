liste=[-3,2,-8,8,9,0,-1]

def talliste(liste):
    
    resultat=[]
    for tall in liste:
        if tall>=0:
            resultat.append(tall)
    return resultat

print(talliste(liste))


