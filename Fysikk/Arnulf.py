import math as m

a=9.81
s=3.6
v0=0

x=v0+0.5*a
print(x)

t2=s/x
t=m.sqrt(t2)
print(t)


v=v0+a*t
print(v)

s=1.1
t=0.47

v=v0+a*t
print(v)



v=6.2

s2=-1*((v**2)/(2*a)-3.6)
print(s2)


t=v/a
print(t)