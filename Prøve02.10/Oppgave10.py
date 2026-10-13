# Øktene lagres som en liste av dictionaries. Da tas rekkefølgen vare på,
# og hver økt har navngitte felter ("aktivitet" og "minutter").


def les_aktivitet() -> str:
    """Spør til brukeren skriver en aktivitet som ikke er tom."""
    while True:
        aktivitet = input("Aktivitet: ").strip().lower()
        if aktivitet != "":
            return aktivitet
        print("Aktiviteten kan ikke være tom.")


def les_minutter() -> int:
    """Spør til brukeren skriver et heltall større enn 0."""
    while True:
        try:
            minutter = int(input("Antall minutter: "))
        except ValueError:
            print("Du må skrive inn et heltall.")
            continue

        if minutter > 0:
            return minutter
        print("Antall minutter må være større enn 0.")


def registrer_okt(okter: list[dict]) -> None:
    aktivitet = les_aktivitet()
    minutter = les_minutter()
    okter.append({"aktivitet": aktivitet, "minutter": minutter})
    print("Økta er registrert.")


def vis_okter(okter: list[dict]) -> None:
    if len(okter) == 0:
        print("Ingen økter registrert ennå.")
        return

    for nummer, okt in enumerate(okter, start=1):
        print(f"{nummer}. {okt['aktivitet']}: {okt['minutter']} min")


def vis_statistikk(okter: list[dict]) -> None:
    if len(okter) == 0:
        print("Ingen økter registrert ennå.")
        return

    # Summer minutter per aktivitet i en dictionary: {"løping": 50, "sykling": 45}
    per_aktivitet = {}
    for okt in okter:
        aktivitet = okt["aktivitet"]
        if aktivitet in per_aktivitet:
            per_aktivitet[aktivitet] += okt["minutter"]
        else:
            per_aktivitet[aktivitet] = okt["minutter"]

    print(f"Antall økter: {len(okter)}")
    print(f"Totalt: {sum(per_aktivitet.values())} min")
    print("Per aktivitet:")
    for aktivitet, minutter in per_aktivitet.items():
        print(f"  {aktivitet}: {minutter} min")

    mest_trent = max(per_aktivitet, key=per_aktivitet.get)
    print(f"Du har trent mest {mest_trent} ({per_aktivitet[mest_trent]} min).")


def main() -> None:
    okter = []

    while True:
        print("\n--- Treningslogg ---")
        print("1: Registrer økt")
        print("2: Vis alle økter")
        print("3: Statistikk")
        print("4: Avslutt")
        valg = input("Velg: ")

        if valg == "1":
            registrer_okt(okter)
        elif valg == "2":
            vis_okter(okter)
        elif valg == "3":
            vis_statistikk(okter)
        elif valg == "4":
            print("Ha det!")
            break
        else:
            print("Ugyldig valg. Skriv 1, 2, 3 eller 4.")


main()