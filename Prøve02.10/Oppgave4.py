studentbevis=False
Alder=int(input("Skriv inn alderen din"))
sb=str(input("Har du studentbevis? Ja eller Nei"))
if sb=="ja":
    studentbevis=True
elif sb=="Ja":
    studentbevis=True
elif sb=="JA":
    studentbevis=True
elif sb=="jA":
    studentbevis=True
else:
    studentbevis=False
#Vet d e en mye lettere og ryddigere måte å gjøre dette på, men der må eg bare være ærlig og si at eg ikke husker kordan


if Alder>120:
    print("For gammel, sannsynligvis dau")
elif Alder>=67:
    print("Honnør, 100kr")
elif Alder >=31:
    print("Alle andre, 150kr")
elif Alder>=12 and studentbevis==True:
    print("Student, 110kr")
elif Alder>=12 and not studentbevis:
    print("Alle andre, 150kr")
elif Alder >0:
    print("Under 12 år, 80kr")
else:
    print("Det kan da umulig stemme")