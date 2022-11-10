arreglo = [1, 2, 3, 4, 5]

print("Arreglo a analizar: " + ' '.join(map(str, arreglo)))
if len(arreglo) > 2:
    maximaDiferencia = max(abs(int(a) - int(b))
                           for a, b in zip(arreglo, arreglo[1:]))
    print("La maxima diferencia entre dos numeros sucesivos es: " +
          str(maximaDiferencia))
else:
    print("La maxima diferencia entre dos numeros sucesivos es: 0")

# Para ejecutar el programa pegar el codigo en https://www.programiz.com/python-programming/online-compiler/
