def subCadenaMasLarga(s):
 
    ventana = {}
    inicio = fin = 0
    bajo = alto = 0
 
    while alto < len(s):
        if ventana.get(s[alto]):
 
            while s[bajo] != s[alto]:
                ventana[s[bajo]] = False
                bajo = bajo + 1
 
            bajo = bajo + 1        
        else:
            ventana[s[alto]] = True
 
            if fin - inicio < alto - bajo:
                inicio = bajo
                fin = alto
 
        alto = alto + 1
 
    return s[inicio:fin + 1]
 
s = "6896644512375"
print(subCadenaMasLarga(s))