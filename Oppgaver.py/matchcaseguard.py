alder=int(input())

match alder:
    case n if n<0:
        print("du finnes ikke mann")
    case n if n<18:
        print("du e mindreårig")
    case n if n<67:
        print("du e voksen")
    case _:
        print("unc, pensjonist")
