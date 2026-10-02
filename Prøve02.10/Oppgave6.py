temperaturer = [4.5, -2.0, 1.5, -6.5, 0.0, 3.0, -1.5, 7.0, 5.5, -3.5]


print(f"{len(temperaturer)} målinger")

print(f"Første måling: {temperaturer[0]} grader, siste måling:{temperaturer[-1]} grader")

gjennomsnitt=sum(temperaturer)/len(temperaturer)
print(f"Gjennomsnitt:{round(gjennomsnitt,1)} grader")


kaldDag=0

for temp in temperaturer:
    if temp<0:
        kaldDag+=1

print(f"{kaldDag} dager under 0 grader")

nye=[]

for temps in temperaturer:
    if temps>0:
        nye.append(temps)

nye.sort(reverse=True)
print(f"temperaturer over 0: {nye}")



