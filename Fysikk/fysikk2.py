v=0
s=0
a=9.81
t=0
dt=0.001
k=0.25
m=10

while s<250:
    a=9.81-k/m*v**2
    v=v+a*dt
    s=s+v*dt
    t=t+dt

print(f"strekning:{s}m fart:{v}m/s tid:{t}sek akelerasjon:{a}m/s^2")