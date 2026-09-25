def er_palindrom(tekst):
    tekst=tekst.lower().replace("","")
    return tekst==tekst[::-1]

print(er_palindrom("racecar"))
print(er_palindrom("ost"))