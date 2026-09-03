a=0.6 #startakselerasjon
s=0#startfart
t=0 #starttid
v0=4.5 #startfart
dt=0.0001 #tidsintervall
tf=2.3 #sluttid

while t<=tf: #endre fart, posisjon og tid
    a=0.6 
    v0+=a*dt
    s+=v0*dt
    t+=dt

print(f"sluttid = {round(t,2)} sekunder" )
print(f"sluttposisjon = {round(s,2)} meter" )
print(f"sluttfart = {round(v0,2)} m/s" )
print(f"sluttakselerasjon = {round(a,2)} m/s^2" )