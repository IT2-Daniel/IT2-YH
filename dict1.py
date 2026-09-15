karakterer={"IT2":"6",
        "Fysikk":"6",
        "kjemi":"6",
        "matte":"6",
        "engelsk":"6"}

if "engelsk" in karakterer:
    print ("Du har {karakterer[engelsk]} i engelsk")

else:
    print("Du har ikke engelsk")


for key, verdi in karakterer.items():
    print(f"du fikk {verdi} i {key}")