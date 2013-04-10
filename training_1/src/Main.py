'''
Created on 21/03/2013

@author: fernando
'''
from Formulario import Formulario
import funciones_calculo

dni = 0

nuevo_formulario = Formulario()
nuevo_formulario.peticion_de_datos()
dni = int (nuevo_formulario.dni)
genero = nuevo_formulario.genero
tipo_de_registro = nuevo_formulario.tipo_de_tramite
codigo_identificador = funciones_calculo.calcular_identificacion\
                                    (genero, dni, tipo_de_registro)
print 'Código identificador: ', codigo_identificador
