def es_vocal(car):
    res = car.lower() in 'aeiouáéíóú'
    return res

f = open('entrada.txt', 'r')
cad = f.read()

cont_voc = 0
cont_pal = 0
for i in cad:
    if (i == ' ') or (i == '.'):
        if (cont_voc == 1):
            cont_pal += 1

        cont_voc = 0
    else:
        band_vocal = es_vocal(i)
        if band_vocal == True:
            cont_voc += 1

f.close()