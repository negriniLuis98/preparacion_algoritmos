# f = open('entrada.txt', 'r')
# Método de Lectura (r)
# Método de Escritura (w)
# Método de Añadido (a)
# a = f.readline()

# f.close()

"""
    Condiciones:
    -Tener una única función que controle la lógica del programa
    -Tener un control de script
    -Tener -al menos- una función con parámetros y que devuelva algo
"""

"""
    4. Determinar cuántas palabras incluyen dos o más veces la expresión que 
    conforman la letra "d" mas una vocal (con cualquiera de sus letras en 
    minúscula o mayúscula) pero de tal forma que la palabra termine además 
    con una vocal
"""

def es_numero_impar (car):
    res = car in '13579'
    return res

def es_vocal(car):
    res = car in 'aeiouáéíóú'
    return res

def es_consonante(car):
    res = car in 'bcdfghjklmnñpqrstvwxyz'
    return res

def promedio(suma, cant):
    if cant != 0:
        res = suma // cant
    else:
        res = 0
    return res

def test ():
    f = open('entrada.txt', 'r')
    cad = f.readline()

    x = len(cad)
    cont_item_1 = 0
    empieza_pal = True
    es_min = True
    empieza_con_nro = False
    empieza_con_vocal = False
    acum_item_2 = 0
    es_b = False
    car = 0

    cant_vocales = 0
    cant_cons = 0

    es_a = False
    es_m = False

    cont_vocal_cons = 0
    acum_vocal_cons = 0

    ant_car = ''
    ult_car = ''

    es_vocal_d = False
    cont_d_vocal = 0
    cant_d_vocal = 0

    for i in range(x):
        if cad[i] == ' ':
            empieza_pal = True
            # Contador del Primer Item
            if es_min == True and empieza_con_nro == True:
                cont_item_1 += 1
            # Contador del Segundo Item
            if es_b == True and empieza_con_vocal == True:
                if acum_item_2 < car:
                    acum_item_2 = car
            # Contador del Tercer Item
            print(es_a)
            print(es_m)
            if (cant_cons > cant_vocales) and (es_a == False) and (es_m == False):
                cont_vocal_cons += 1
                acum_vocal_cons += car

            if es_vocal_d == True and cant_d_vocal >= 2:
                ult_car_vocal = es_vocal(ult_car.lower())
                if ult_car_vocal == True:
                    cont_d_vocal += 1

            es_min = True
            empieza_con_nro = False

            es_b = False
            empieza_con_vocal = False

            car = 0
        else:
            ant_car = ult_car
            ult_car = cad[i]

            if ant_car == 'd':
                # debido
                es_vocal_d = es_vocal(ult_car.lower())
                cant_d_vocal += 1
            car += 1
            # Lógica del Tercer Item
            vocal = es_vocal(cad[i].lower())

            if vocal == True:
                cant_vocales += 1
                es_a = es_a or (cad[i].lower() == 'a')

            else:
                cons = es_consonante(cad[i].lower())
                if cons == True:
                    cant_cons += 1
                    es_m = es_m or (cad[i].lower() == 'm')

            # Lógica del Primer Item
            if empieza_con_nro == True:
                # True and True = True
                # False and True = False
                es_min = es_min and cad[i].islower()

            if empieza_pal == True:
                primer_car = cad[i]
                es_impar = es_numero_impar(primer_car)
                if es_impar == True:
                    empieza_con_nro = True
                else:
                    empieza_con_vocal = es_vocal(cad[i].lower())
                empieza_pal = False

            # True or False = True
            # False or False = False
            es_b = es_b or (cad[i].lower() == 'b')

    f.close()

    r1 = cont_item_1
    r2 = acum_item_2
    print(acum_vocal_cons)
    print(cont_vocal_cons)
    r3 = promedio(acum_vocal_cons, cont_vocal_cons)
    r4 = cont_d_vocal

    print('Primer resultado:', r1)
    print('Segundo resultado:', r2)
    print('Tercer resultado:', r3)
    print('Cuarto resultado:', r4)


if __name__ == '__main__':
    test()