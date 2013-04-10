'''
Created on 22/03/2013

@author: fernando
'''


def arreglo_de_digito(numero):
    numero = str(numero)
    auxiliar = 0
    for i in range(len(numero)):
        auxiliar = auxiliar + int(numero[i])
    numero = auxiliar
    x = str(numero)
    if len(x) >= 2:
        arreglo_de_digito(int(x))
    return numero
if __name__ == '__main__':
    diccionario_de_patente = {'a': '14', 'b': '01', 'c': '00',\
                          'd': '16', 'e': '05', 'f': '20',\
                          'g': '19', 'h': '09', 'i': '24',\
                          'j': '07', 'k': '21', 'l': '08',\
                          'm': '04', 'n': '13', 'o': '25',\
                          'p': '22', 'q': '18', 'r': '10',\
                          's': '02', 't': '06', 'u': '12',\
                          'v': '23', 'w': '11', 'x': '05',\
                          'y': '15', 'z': '17'}
    patente = raw_input('ingrese patente: ')
    patente = patente.lower()
    i = 0
    while i < len(patente):
        try:
            patente = patente.replace(patente[i], diccionario_de_patente[patente[i]])
            i = i + 1
        except:
            i = i + 1
    patente = str(patente)
# ACA FALTA DESARROLLAR TERMINAR DE CALCULAR EL NUMERO IDENTIFICADOR
    i -= 1
    suma_digito_impar = 0
    suma_digito_par = 0
    while i >= 0:
        if i % 2 == 0:
            suma_digito_par = int(patente[i]) + suma_digito_par
        else:
            suma_digito_impar = int(patente[i]) + suma_digito_impar
        i -= 1
    if len(str(suma_digito_impar)) >= 2:
        suma_digito_impar = arreglo_de_digito(suma_digito_impar)
    if len(str(suma_digito_par)) >= 2:
        suma_digito_par = arreglo_de_digito(suma_digito_par)
    digito_identificador = str(suma_digito_par) + str(suma_digito_impar)
    print 'digito_identificador= ', digito_identificador
