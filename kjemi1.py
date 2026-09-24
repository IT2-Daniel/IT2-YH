from mendeleev import *
from matplotlib import *


grunnstoff=["K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br",]

Radiuser=[]

Elektronegativiteter=[]


    

Symboler=[]

for symbol in grunnstoff:
    stoff=element(symbol)
    Symboler.append(symbol)
    Radiuser.append(stoff.atomic_radius)
    Elektronegativiteter.append(stoff.en_pauling)

print(Symboler)
print(Radiuser)
print(Elektronegativiteter)