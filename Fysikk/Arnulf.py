import math as m 

s1=1.54 #Strekning
v=0 #sluttfart
v0=5.50 #startfart
a=9.81 #akselerasjon





t=s1/(0.5*v0) #tid
print(t)


s2=4.32-1.54
v0=0

t1=m.sqrt(2*s2/a)

print(t+t1)