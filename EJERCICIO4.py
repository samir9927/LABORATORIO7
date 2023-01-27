texto = """Hola, mundo. Esto es una cadena, se supone que debe tener 
varias palabras pues vamos a realizar un conteo de frecuencia de las 
mismas usando el lenguaje de programación Python. Ya no sé qué escribir
 pero sigo escribiendo para que poco a poco la cadena sea más larga y 
 el ejercicio de programación sea demostrable. Creo que con todo
  esto que he escrito es suficiente"""

quitar = ",;:.\n!\"'"
for caracter in quitar:
    texto = texto.replace(caracter,"")  

texto = texto.lower()

palabras = texto.split(" ")

diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")