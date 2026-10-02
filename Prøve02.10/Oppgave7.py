poeng = {"Ada": 42, "Linus": 17, "Grace": 58, "Alan": 17, "Guido": 33}

total=0

for nokkel in poeng:
    print(f"{nokkel} har {poeng[nokkel]} poeng")


for key in poeng:
    total+=poeng[key]

print(f"De har {total} poeng til sammen")


navn=input("Skriv navn til en deltaker")

poengsum={poeng.get(navn)}


if poengsum!={None}:
    print(f"{navn} har {poeng.get(navn)}")

else:
    print("Fant ingen deltaker med navnet")
