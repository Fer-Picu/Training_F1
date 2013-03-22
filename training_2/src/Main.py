'''
Created on 22/03/2013

@author: fernando
'''

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
# ACA FALTA DESARROLLAR TERMINAR DE CALCULAR EL NUMERO IDENTIFICADOR
    suma_digito_impar = 0
    suma_digito_par = 0
    while i > 0:
        if patente[i] % 2 != 0:
            suma_digito_impar = patente[i] + suma_digito_impar 
        else:
            h_par = 0
            suma_digito_par = patente[i] + suma_digito_par
            while suma_digito_par > 10:
                while h_par < len(suma_digito_par):
                    pass
