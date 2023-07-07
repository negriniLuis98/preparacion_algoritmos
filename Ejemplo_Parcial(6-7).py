"""
    5. Determinar cuántas palabras incluyen al menos un dígito en la primer
    mitad de la palabra. Considere que si la longitud de la palabra es
    impar, entonces el caracter central no pertenece a ninguna de las dos
    mitades.
    Ej.: "hg3djh jui8 3ko4 5 uj6ui."
"""

def es_numero (car):
    res = car in '0123456789'
    return res

def es_cons_mayus (car):
    res = car in 'BCDFGHJKLMNÑPQRSTVWXYZ'
    return res

def es_nro_impar (car):
    res = car in '13579'
    return res

def es_vocal (car):
    res = car.lower() in 'aeiouáéíóú'
    return res

def porcentaje (pal_cond, total):
    res = (pal_cond * 100) // total
    return res

def test ():
    f = open('entrada.txt', 'r')
    cad = f.read()

    car = 0
    pos_nro = 0
    cont_5 = 0

    band_impar = True
    band_cons_may = True
    cont_1 = 0

    mayor_lon_2 = 0
    prm_car = ''
    es_prin = True

    cont_a = 0
    cont_e = 0
    cont_cond_3 = 0
    cont_total = 0

    ant_car = ''
    ult_car = ''
    cont_cond_4 = 0
    cont_di = 0
    for i in cad:
        # tiempo
        if i == ' ' or i == '.':
            mitad = car // 2

            if pos_nro > 0:
                if pos_nro <= mitad:
                    cont_5 += 1

            if (band_cons_may == True) and (band_impar == True):
                cont_1 += 1

            band_vocal = es_vocal(prm_car)
            if (band_vocal == True) and (mayor_lon_2 < car):
                mayor_lon_2 = car

            if cont_a > cont_e:
                cont_cond_3 += 1

            band_vocal_4 = es_vocal(ult_car)
            if (cont_di >= 2) and (band_vocal_4 == True):
                cont_cond_4 += 1

            car = 0
            pos_nro = 0
            band_impar = True
            band_cons_may = True
            es_prin = True
            cont_di = 0
            ult_car = ''
            ant_car = ''
            prm_car = ''
            cont_a = 0
            cont_e = 0
        else:
            car += 1
            ant_car = ult_car
            ult_car = i

            if es_prin == True:
                es_prin = False
                prm_car = i
                cont_total += 1

            band_nro = es_numero(i)
            if (band_nro == True) and (pos_nro == 0):
                pos_nro = car

            if i.isalpha():
                if band_cons_may == True:
                    band_cons_may = es_cons_mayus(i)
            else:
                if band_impar == True:
                    band_impar = es_nro_impar(i)

            if i.lower() == 'a':
                cont_a += 1
            elif i.lower() == 'e':
                cont_e += 1

            if (ant_car == 'd') and (ult_car == 'i'):
                cont_di += 1

    f.close()
    # hg3djh j2ui8 3ko4 5 uj36ui.
    print('La cantidad de palabras que tienen un dígito en su primer mitad es:', cont_5)

if __name__ == '__main__':
    test()

# cad[i-1]