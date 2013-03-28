from gestor_de_prediccion import Gestor
from modelo_boton import Modelo_Boton
#import gestor_de_prediccion
#from gestor_de_prediccion import Gestor
#from gestor_de_prediccion import Gestor

mi_gestor = Gestor()
lista_botones = []


def main():
    print mi_gestor.buscar_opciones('h')
    for i in range(11):
        lista_botones.append(Modelo_Boton())
        lista_botones[i].id = i
    for boton in lista_botones:
        print boton.id
if __name__ == "__main__":
    main()
