binding=3
print("tast 1 for metall og 2 for ikkemetall")
stoff1=int(input("stoff 1:"))
stoff2=int(input("Stoff 2:"))
match binding:
    case n if stoff1==1 and stoff2==2:
        print("ionebinding")
    case n if stoff1==2 and stoff2==2:
        print("kovalent binding")
    case n if stoff1==2 and stoff2==1:
        print("ionebinding")
    case _:
        print("Metallbinding")