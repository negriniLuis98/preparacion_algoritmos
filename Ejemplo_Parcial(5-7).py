"""
    - El programa tenga una función que contenga toda su lógica
    - Un control de script
    - Al menos una función con parámetros que devuelva algo
"""


"""
    4. Determinar cuántas palabras incluyen la expresión "ra" (con 
    cualquiera de sus letras en minúscula o mayúscula) pero de tal forma 
    que la palabra además tenga una vocal (mayúscula o minúscula) entre 
    sus dos primeros caracteres.
    Ej.:  "Otra rara ocasion para esos tarados."
"""
def es_consonante(car):
    res = car.lower() in 'bcdfghjklmnñpqrstvwxyz'
    return res

def es_vocal(car):
    res = car.lower() in 'aeiouáéíóú'
    return res

def es_numero(car):
    res = car in '0123456789'
    return res

def promedio(suma, divisor):
    res = 0

    if (divisor > 0):
        res = suma // divisor

    return res

def test ():
    f = open('entrada.txt', 'r')
    cad = f.readline()
    # x = len(cad)

    cant_voc = 0
    cant_cons = 0
    car = 0
    cont_1 = 0

    cont_nros = 0
    acum_lon_pal = 0
    es_p = False

    acum_car_3 = 0
    cont_pal_3 = 0
    es_s = False

    ant_car = ''
    ult_car = ''
    es_vocal_prin = False
    tiene_exp = False
    cont_4 = 0
    for i in cad:
        if i == ' ' or i == '.':
            if (car % 2) == 0:
                if cant_voc == cant_cons:
                   cont_1 += 1

            if cont_nros >= 1 and es_p == False:
                if acum_lon_pal < car:
                    acum_lon_pal = car

            if car > 2 and es_s == True:
                acum_car_3 += car
                cont_pal_3 += 1

            if tiene_exp == True and es_vocal_prin == True:
                cont_4 += 1

            car = 0
            cant_voc = 0
            cant_cons = 0
            cont_nros = 0
            es_p = False
            es_s = False
            tiene_exp = False
            es_vocal_prin = False
        else:
            # Operaciones para el primer item
            car += 1

            ant_car = ult_car
            ult_car = i

            band_vocal = es_vocal(i)
            band_cons = es_consonante(i)
            band_nro = es_numero(i)

            if band_vocal == True:
                cant_voc += 1
            elif band_cons == True:
                cant_cons += 1
            elif band_nro == True:
                cont_nros += 1

            if es_p == False:
                es_p = i.lower() == 'p'

            if es_s == False:
                es_s = i.lower() == 's'

            if car == 2:
                band_ult_vocal = es_vocal(ult_car)
                band_ant_vocal = es_vocal(ant_car)
                if band_ult_vocal == True or band_ant_vocal == True:
                    es_vocal_prin = True

            if ant_car == 'r' and ult_car == 'a':
                tiene_exp = True
    f.close()
    r1 = cont_1
    r2 = acum_lon_pal
    r3 = promedio(acum_car_3, cont_pal_3)
    r4 = cont_4

    print('El resultado del item 1 es:', r1)
    print('El resultado del item 2 es:', r2)
    print('El resultado del item 3 es:', r3)
    print('El resultado del item 4 es:', r4)

if __name__ == '__main__':
    test()