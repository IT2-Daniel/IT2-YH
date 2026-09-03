a=-9.81 #startakselerasjon
s=20#startposisjon
t=0 #starttid
v0=125 #startfart
dt=0.001 #tidsintervall
tf=2.3 #sluttid

while s>=0: #endre fart, posisjon og tid
    a=-9.81 
    v0=v0+a*dt
    s=s+v0*dt
    t=t+dt

print(f"sluttid = {round(t,2)} sekunder" )
print(f"sluttposisjon = {round(s,2)} meter" )
print(f"sluttfart = {round(v0,2)} m/s" )
print(f"sluttakselerasjon = {round(a,2)} m/s^2" )