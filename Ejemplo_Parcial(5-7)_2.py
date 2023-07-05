"""
    2. Determine la cantidad de palabras que contienen al menos un dígitos y
    que son de longitud impar.
"""
def es_vocal(car):
    res = car.lower() in 'aeiouáéíóú'
    return res

def es_consonante(car):
    res = car.lower() in 'bcdfghjklmnñpqrstvwxyz'
    return res

def es_numero(car):
    res = car in '0123456789'
    return res

def test():
    f = open('entrada.txt', 'r')
    cad = f.read()

    car = 0
    es_cons = False
    ult_car = ''
    cont_1 = 0

    cont_nros = 0
    cont_2 = 0
    for i in cad:
        if (i == ' ') or (i == '.'):
            band_vocal = es_vocal(ult_car)
            if (es_cons == True) and (band_vocal == True):
                cont_1 += 1

            if (cont_nros >= 1) and ((car % 2) != 0):
                                # dividendo % divisor

                cont_2 += 1
            es_cons = False
            car = 0
            cont_nros = 0
        else:
            car += 1
            ult_car = i
            if ((car == 3) or (car == 5)) and es_cons == False:
                es_cons = es_consonante(i)

            band_nro = es_numero(i)
            if (band_nro == True):
                cont_nros += 1

    f.close()

if __name__ == '__main__':
    test()