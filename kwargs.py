def skriv_profil(**info):
    for nokkel, verdi in info.items():
        print(f"{nokkel}: {verdi}")

skriv_profil(navn="daniel", alder="16", klasse="2STD")
    