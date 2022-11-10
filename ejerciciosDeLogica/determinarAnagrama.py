def determinarAnagrama(palabra1, palabra2):
    if sorted(palabra1) == sorted(palabra2):
        print("Son Anagramas")
    else:
        print("No son Anagramas")
    return


palabra1 = (input("Ingresa tu primer palabra: "))
palabra2 = (input("Ingresa tu segunda palabra:  "))
determinarAnagrama(palabra1.lower(), palabra2.lower())
# Para ejecutar el programa pegar el codigo en https://www.programiz.com/python-programming/online-compiler/
