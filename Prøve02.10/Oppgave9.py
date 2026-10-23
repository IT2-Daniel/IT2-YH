lager= [

    tastatur1:={"varenummer":"001","antall":5, "pris":500, "kategori":"tastatur"},
    mus1:={"varenummer":"002","antall":100, "pris":600, "kategori":"mus"},
    headset1:={"varenummer":"003","antall":0, "pris":899, "kategori":"headset"},
    skjerm1:={"varenummer":"004","antall":3, "pris":2999, "kategori":"skjerm"},
    mus2:={"varenummer":"005","antall":140, "pris":650, "kategori":"mus"} 
] #valgte dette oppsettet fordi jeg har vært litt borti det før og tenkte først at det kunne funke bra her å ha en liste med flere dictionaries i, en for hvert produkt 


def vis_lager(lager):
    for nokkel in tastatur1:
        print(nokkel, tastatur1[nokkel])



print(f"tastatur1:{vis_lager(tastatur1)}")
print(f"mus1:{vis_lager(mus1)}")
print(f"headset1:{vis_lager(headset1)}")
print(f"skjerm1:{vis_lager(skjerm1)}")
print(f"mus2:{vis_lager(mus2)}")


def selg_vare(lager:dict,varenummer:str,antall:int) -> bool:
    if varenummer not in lager:
        print(f"fant ingen vare med varenummer {varenummer}")
        return False

vare=lager[varenummer]

if vare["antall"]<antall:
    