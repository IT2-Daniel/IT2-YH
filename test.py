def skriv_profil(**info):
    for nokkel, verdi in info.items():
        print(f"{nokkel}: {verdi}")

skriv_profil(navn="Ola", alder=17, klasse="3IM1")