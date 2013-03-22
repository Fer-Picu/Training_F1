'''
Created on 21/03/2013

@author: fernando
'''

lista_para_valor_1 = []
prefijo = 0
dni_con_prefijo = 0
valor_1 = 0


def convertir_int_to_list(i):
    return [int(x) for x in str(i).zfill(8)]


def establecer_prefijo(genero, dni, tipo_de_registro):
    if tipo_de_registro == 'CUIL':
        if genero == 'HOMBRE':
            prefijo = 20
        else:
            prefijo = 27
    elif tipo_de_registro == 'CUIT':
        prefijo = 30
    dni_con_prefijo = 100000000 * prefijo + int(dni)
    return dni_con_prefijo


def cuentas_del_algoritmo(lista_para_valor_1):
    i = 0
    valor_1 = 0
    while i < 10:
        valor_1 = valor_1 + lista_para_valor_1[i]
        i = i + 1
    valor_2 = valor_1 % 11
    codigo_identificador = 11 - valor_2
    if codigo_identificador == 10:
        codigo_identificador = 9
    if codigo_identificador == 11:
        codigo_identificador = 0
    return codigo_identificador


def calcular_identificacion(dni, genero, tipo_de_registro):
    lista_algoritmo = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    dni_con_prefijo = establecer_prefijo(dni, genero, tipo_de_registro)
    lista_dni = convertir_int_to_list(dni_con_prefijo)
    for h in range(10):
        lista_para_valor_1.append(lista_algoritmo[h] * lista_dni[h])
    numero_identificador = cuentas_del_algoritmo(lista_para_valor_1)
    return numero_identificador
