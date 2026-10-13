lager = {
    "A100": {"navn": "Mekanisk tastatur", "pris": 899.0, "antall": 12, "kategori": "tastatur"},
    "A101": {"navn": "Trådløst tastatur", "pris": 499.0, "antall": 3, "kategori": "tastatur"},
    "B200": {"navn": "Gamingmus", "pris": 649.5, "antall": 0, "kategori": "mus"},
    "B201": {"navn": "Kontormus", "pris": 199.0, "antall": 25, "kategori": "mus"},
    "C300": {"navn": "27\" skjerm", "pris": 2999.0, "antall": 4, "kategori": "skjerm"},
}


def vis_lager(lager: dict) -> None:
    print(f"{'Varenr':<8}{'Navn':<20}{'Kategori':<10}{'Pris':>10}{'Antall':>8}")
    print("-" * 56)
    for varenummer, vare in lager.items():
        print(f"{varenummer:<8}{vare['navn']:<20}{vare['kategori']:<10}"
              f"{vare['pris']:>10.2f}{vare['antall']:>8}")


def selg_vare(lager: dict, varenummer: str, antall: int) -> bool:
    if varenummer not in lager:
        print(f"Fant ingen vare med varenummer {varenummer}.")
        return False

    vare = lager[varenummer]

    if vare["antall"] < antall:
        print(f"Bare {vare['antall']} igjen av {vare['navn']}, kan ikke selge {antall}.")
        return False

    vare["antall"] -= antall
    å_betale = antall * vare["pris"]
    print(f"Solgt {antall} stk. {vare['navn']}. Å betale: {å_betale:.2f} kr")
    return True


def lav_beholdning(lager: dict, grense: int = 5) -> list[str]:
    lave = []
    for vare in lager.values():
        if vare["antall"] < grense:
            lave.append(vare)

    lave.sort(key=lambda vare: vare["antall"])

    navn = []
    for vare in lave:
        navn.append(vare["navn"])
    return navn


vis_lager(lager)
print()
print(selg_vare(lager, "A100", 2))    # True
print(selg_vare(lager, "X999", 1))    # False, ukjent varenummer
print(selg_vare(lager, "C300", 10))   # False, for få på lager
print(selg_vare(lager, "C300", 4))    # True, akkurat så mange som er på lager
print()
print(lav_beholdning(lager))