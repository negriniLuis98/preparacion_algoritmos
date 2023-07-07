''' Por ejemplo, el texto: los mandriles en Brasil peligran su actual situacion
contiene 2 palabras con la última letra de la palabra anterior en la segunda mitad '''

#definicion de funciones
def es_vocal(car):
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    return car in vocales

def es_digito(car):
    digitos = '0123456789'
    return car in digitos

def es_consonante(car):
    res = False
    if not es_vocal(car) and not es_digito(car):
        res = True
    return res

def porcentaje(total, parcial):
    porcentaje = 0

    if total != 0:
        porcentaje = parcial * 100 / total
    return porcentaje

def promedio(suma, cantidad):
    promedio = 0
    if cantidad != 0:
        promedio = suma / cantidad
    return  promedio

#defeinir funcion principal
def test():
    #cargar la cadena
    f = open('entrada.txt', 'r')
    texto = f.read()

    cant_letras_porplabras = 0
    cant_palabra = 0
    #punto 1 determinar el porcentaje de vocales, de consonante y
    # de digitos en el total de caracteres del texto (3 porcentajes).

    porcenta_vocales = 0
    porcenta_consonantes = 0
    porcenta_digitos = 0
    cant_letras_total = 0
    #cantidades parciales en el texto
    cant_vocales = 0
    cant_digitos = 0
    cant_consonantes = 0

    #punto 2 determinar el promedio de las letras por palabra de las palabara
    # que tuvieron más vocales que consonantes
    promedio_2 = 0
    cant_letras_total_2 = 0
    cant_palabra_2 = 0
    cant_vocales_2 = 0
    cant_consonantes_2 = 0

    #punto 3 determinar el porcentaje de palabras que incluyeron
    # la última letra de la palabra anterior en la segunda mitad de la palabra

    porcentaje_3 = 0
    cant_palabra_3 = 0
    ult_letra = ' '
    pos_3 = 0
    car_ant = ' '
    #punto 4 determinar la cantidad de palabras que comenzaron con "ll"
    # y además incluyeron alguna "s"

    cant_palabra_4 = 0
    empezo_ll = False
    tiene_s = False


    #recorrer la cedena
    for car in texto:
       # anlaizar que pasa dentro de la palabra
       if car != ' ' and car != '.':
           cant_letras_porplabras += 1
           cant_letras_total += 1

           if es_vocal(car):
               cant_vocales += 1
               cant_vocales_2 += 1

           if es_digito(car):
               cant_digitos += 1

           if es_consonante(car):
                cant_consonantes += 1
                cant_consonantes_2 += 1

            #punto 3
           if car == ult_letra:
               pos_3 = cant_letras_porplabras

           #punto 4
           if cant_letras_porplabras == 2:
              if car.lower() == 'l' and car.lower() == 'l':
                  empezo_ll = True
              if car.lower() == 's':
                  tiene_s = True




               # analizar que pasa fuera de la palabra
       else:
           cant_palabra += 1

           if cant_vocales_2 > cant_consonantes_2:
               cant_letras_total_2 += cant_letras_porplabras
               cant_palabra_2 += 1
           #punto 3
           #guardar la ultma letra de la palabra anterior
               ult_letra = car_ant
               #calcular la mitad de la palabra
               mitad = cant_letras_porplabras // 2
               if pos_3 > 0 and pos_3 > mitad:
                   cant_palabra_3 += 1

               #4
               if tiene_s and empezo_ll:
                   cant_palabra_4 += 1


           #reset de variables
           cont_letras_porplabras = 0
           cant_vocales_2 = cant_consonantes_2 = 0
           pos_3 = 0
           tiene_s = empezo_ll = False

       car_ant = car
       #fin del recorrido

    f.close()

    #calculos finales
    porcenta_vocales = porcentaje(cant_letras_total, cant_vocales)
    porcenta_digitos = porcentaje(cant_letras_total, cant_digitos)
    porcenta_consonantes = porcentaje(cant_letras_total, cant_consonantes)

    promedio_2 = promedio(cant_letras_total_2, cant_palabra_2)
    #3
    porcentaje_3 = porcentaje(cant_palabra, cant_palabra_3)

    #mostrar resultados
    print('El porcentaje de vocales es: ', porcenta_vocales)
    print('El porcentaje de digitos es: ', porcenta_digitos)
    print('El porcentaje de consonantes es: ', porcenta_consonantes)
    print('Promedio del punto 2: ', promedio_2)
    print('Porcentaje del punto 3: ', porcentaje_3)
    print('La cantidad del punto 4 es: ', cant_palabra_4)

#invocar a la funcion principal
if __name__ == '__main__':
    test()