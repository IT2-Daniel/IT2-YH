def konverter_tid(sekunder):
    timer=sekunder//3600
    sekunder-=timer*3600
    minutter=sekunder//60
    sekunder-=minutter*60
    sekund=sekunder%60
    print(f"{timer} timer, {minutter} minutter, {sekund} sekunder")


print(konverter_tid(4000))