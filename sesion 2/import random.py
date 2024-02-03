import random

lanzamientos = 0
cescu=0
cuno=0
while lanzamientos < 10:
    moneda = random.randint(0,1)
    
    lanzamientos +=1
    if moneda == 0:
        print("escudo")
        cescu+=1
    else: 
        print("uno")
        cuno +=1
por_un = cuno/10
por_esc = cescu/10

print("porcentaje escudo",por_esc)
print("porcentaje  uno",por_un)
