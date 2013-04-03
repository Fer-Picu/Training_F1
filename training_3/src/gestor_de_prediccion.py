class Gestor():
    def __init__(self):
        self.clave_palabra = ''
        self.diccionario_claves_de_palabras = {}
        self.diccionario_de_botones = {\
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
        self.lista_palabras = [\
                         'hola', 'gola', 'bien', 'horario', 'termo',
                         'temple', 'accion', 'cancion', 'estar',
                         'escribo', 'aviso', 'que', 'veces', 'burundanga',
                         'hey'
                         ]
        self.make_diccionario_claves()

    def get_clave_palabra(self, string):
        """
        por cada letra de la string recorro cada
        item del diccionario e identifico el boton al que pertenece
        luego concateno la clave de la palabra con la clave hallada
        """
        self.clave_palabra = ''
        self.index_string = 0
        while self.index_string < len(string):
            for cada_tupla in self.diccionario_de_botones.items():
                self.tupla_actual = cada_tupla
                for letra_del_diccionario in cada_tupla[1]:
                    if letra_del_diccionario == string[self.index_string]:
                        self.clave_palabra = self.clave_palabra + cada_tupla[0]
            self.index_string = self.index_string + 1
        return self.clave_palabra

    def make_diccionario_claves(self):
        for cada_item in self.lista_palabras:
            self.diccionario_claves_de_palabras[cada_item] = \
                                self.get_clave_palabra(cada_item)

    def buscar_opciones(self, palabra):
        self.lista_posibilidades = []
        clave_palabra_escribiendo = self.get_clave_palabra(palabra)
        for tupla in self.diccionario_claves_de_palabras.items():
            if tupla[1].split(clave_palabra_escribiendo)[0] == '':
                self.lista_posibilidades.append(tupla[0])
        return self.lista_posibilidades
