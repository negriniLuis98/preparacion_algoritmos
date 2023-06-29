"""
Se pide desarrollar un programa en Python que permita cargar por teclado un texto
completo en una variable de tipo cadena de caracteres. El texto finaliza con '.'
y se supone que el usuario cargará el punto para indicar el final del texto, y
que cada palabra de ese texto está separada de las demás por un espacio en blanco.
El programa debe incluir:
	-Una función principal para lanzar el programa
	-Control de ejecución del script principal con la variable __name__
	-Al menos una función simple con parámetros y retorno de resultado
"""

def es_vocal(letra):
    # 'a' != 'A'
    res = letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'
    return res

def es_nsp(letra):
    res = letra == 'n' or letra == 's' or letra == 'p'
    return res

def test():
    cad = input('Ingrese una cadena de texto. Recuerde que debe finalizar con punto: ')
    x = len(cad)
    while cad[x-1] != '.':
        cad = input('Error. La cadena debe finalizar con un punto. Intente nuevamente: ')

    """
    4. Determinar cuántas palabras incluyen la expresión "pa" (con cualquiera de sus
    letras en minúscula o en mayúscula) pero no contienen al mismo tiempo una "t".
    Ej.: "La patada hizo que el tiro raspara el palo". Hay dos palabras ('raspara' y
    'palo') que cumplen con la condición. La palabra 'patada' por otro lado, si bien
    tiene "pa", también tiene una "t".
    """
    cont_pal_4_vocales = 0
    cont_carac = 0
    cont_vocal = 0

    cont_nsp = 0
    acum_carac = 0
    cont_pal_nsp = 0

    empieza_pal = True

    pr_carac = ''
    ult_carac = ''

    letra_p = ''
    letra_a = ''

    hay_t = False
    hay_pa = False

    contador_pa_no_t = 0
    cont_pal_mismo_carac = 0
    for i in range(x):
        if cad[i] == " ":
            if empieza_pal == False:
                empieza_pal = True
            # Comprobación de Punto 1
            if cont_carac >= 4 and cont_vocal >= 3:
                cont_pal_4_vocales += 1
            # Comprobación de Punto 2
            if cont_nsp >= 1:
                acum_carac += cont_carac
                cont_pal_nsp += 1
            # Comprobación de Punto 3
            if pr_carac.lower() == ult_carac.lower():
                cont_pal_mismo_carac += 1
            if hay_pa == True and hay_t == False:
                contador_pa_no_t += 1

            # Reinicio de Contadores
            cont_carac = 0
            cont_vocal = 0
            cont_nsp = 0
            # Reinicio de contenedores de caracteres
            pr_carac = ''
            ult_carac = ''
            # Reinicio de banderas
            hay_pa = False
            hay_t = False
        else:
            # Comprobación de si es inicio de palabra
            # Lógica del Punto 3
            ult_carac = cad[i]
            if empieza_pal == True:
                pr_carac = ult_carac
                empieza_pal = False
            cont_carac = cont_carac + 1
            # Lógica de Punto 1
            es_v = es_vocal(cad[i].lower())
            if es_v == True:
                cont_vocal += 1
            # Lógica de Punto 2
            es_cons = es_nsp(cad[i].lower())
            if es_cons == True:
                cont_nsp += 1
            # Lógica de Punto 4
            letra_p = letra_a
            letra_a = cad[i].lower()

            concatenacion = letra_p + letra_a
            if concatenacion == 'pa':
                hay_pa = True

            if cad[i] == 't':
                hay_t = True

    print('La cantidad de palabras que tienen 4 o más caracteres y 3 o más vocales es:', cont_pal_4_vocales)
    # prom = acum_carac // cont_pal_nsp
    if cont_pal_nsp > 0:
        prom = acum_carac // cont_pal_nsp
        print('El promedio de caracteres por palabras que contienen una (o mas) \'n\', \'s\', o \'p\' es:', prom)
    else:
        print('No hay un promedio calculado puesto a que no hubieron palabras que cumplían con la condición')
    print('La cantidad de palabras que empiezan y terminan con el mismo caracter es:', cont_pal_mismo_carac)
    print('La cantidad de palabras que incluyen la expresión \'pa\' pero no incluyen una \'t\' es:', contador_pa_no_t)
# i = 0
# while cad[i] == '.':
# while i < len(cad):
    # ...
    # i += 1
    # ...
if __name__ == '__main__':
    test()