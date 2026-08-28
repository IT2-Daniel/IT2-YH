alder=int(input())

if alder>=21:
    print("Du kan ta førerkort for buss, bil, moped og mc")
elif alder>=18:
    print("Du kan ta førerkort for bil, moped, lett mc og mc")
elif alder>=16:
    print("Du kan ta førerkort for moped og lett mc")
else:
    print("for ung")