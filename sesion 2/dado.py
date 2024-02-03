import random

lanzamientos = 0
resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

while lanzamientos < 10:
    resultado_dado = random.randint(1, 6)
    
    lanzamientos += 1
    
    print("Resultado del dado:", resultado_dado)
    
    resultados[resultado_dado] += 1

for cara, cantidad in resultados.items():
    porcentaje = cantidad / 10
    print(f"Porcentaje de {cara}: {porcentaje * 100}%")
