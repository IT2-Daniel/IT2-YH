a=20 #startakselerasjon
s=0#startposisjon
t=0 #starttid
v0=0 #startfart
dt=0.001 #tidsintervall
tf=2.5 #sluttid



while t<=10: #endre fart, posisjon og tid
    a=20
    v0=v0+a*dt
    s=s+v0*dt
    t=t+dt

print(f"sluttid = {round(t,2)} sekunder" )
print(f"sluttposisjon = {round(s,2)} meter" )
print(f"sluttfart = {round(v0,2)} m/s" )
print(f"sluttakselerasjon = {round(a,2)} m/s^2" )
