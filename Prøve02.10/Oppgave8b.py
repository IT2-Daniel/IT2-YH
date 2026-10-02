
passord=str(input())

def sterktpassord (passord):
    if len.passord<=8:
        krav1=True
    if passord.isdigit()==True:
        krav2=True
    if passord.isupper()==True:
        krav3=True

    if krav1==True and krav2==True and krav3==True:
        print("sterkt passord")
    else:
        print("svakt passord")


print(sterktpassord("hemmelig"))


