måned=int(input())

match måned:
    case 12|1|2:
        print("vinter")
    case 3|4|5:
        print("vår")
    case 6|7|8:
        print("sommer")
    case 9|10|11:
        print("høst")
    case _:
        print("ugyldig")