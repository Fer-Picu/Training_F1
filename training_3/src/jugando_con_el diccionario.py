dic_2 = {\
      '0': '',
      '1': '',
      '2': ['a', 'b', 'c'],
      '3': ['d', 'e', 'f'],
      '4': ['g', 'h', 'i'],
      '5': ['j', 'k', 'l'],
      '6': ['m', 'n', 'o'],
      '7': ['p', 'q', 'r', 's'],
      '8': ['t', 'u', 'v'],
      '9': ['w', 'x', 'y', 'z'],
       '#': ' ', '*': ''
      }

lista_palabras = [\
                 'hola', 'bien', 'horario', 'termo',
                 'temple', 'accion', 'cancion', 'estar',
                 'escribo', 'aviso', 'que', 'veces', 'burundanga',
                 'hey'
                 ]

def get_boton(string):
    for cada_tupla in dic_2.items():
        tupla_actual = cada_tupla
        for letra in cada_tupla[1]:
            if letra == string:
                return tupla_actual[0]

clave_palabra = ['4','6']
lista_posibilidades = []
print "q343".split("q")
def buscar_opciones():
    for palabra in lista_palabras:
        if clave_palabra[0] == get_boton(palabra[0]):
            lista_posibilidades.append(palabra)
    print lista_posibilidades    
buscar_opciones()