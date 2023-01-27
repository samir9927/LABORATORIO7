def subCadenaMasLarga(s):
 
    ventana = {}
    inicio = fin = 0
    bajo = alto = 0
 
    while alto < len(s):
 
        # si el carácter actual está presente en la ventana actual
        if ventana.get(s[alto]):
 
            # eliminar caracteres de la izquierda de la ventana hasta
            # nos encontramos con el personaje actual
            while s[bajo] != s[alto]:
                ventana[s[bajo]] = False
                bajo = bajo + 1
 
            bajo = bajo + 1        # eliminar el carácter actual
        else:
            # si el carácter actual no está presente en el actual
            # Ventana #, inclúyela
            ventana[s[alto]] = True
 
            # actualice el tamaño máximo de la ventana si es necesario
            if fin - inicio < alto - bajo:
                inicio = bajo
                fin = alto
 
        alto = alto + 1
 
    # devuelve la subcadena más larga que se encuentra en `s[begin…end]`
    return s[inicio:fin + 1]
 
 
s = "6896644512375"
print(subCadenaMasLarga(s))