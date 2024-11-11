
#Definicion del error custom ##################################
class ElementoDuplicadoError(ValueError):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f'Aca hay un error: {self.mensaje} y de clase: {self.__class__}'
################################################################

def agregar_una_vez(lista, elem) -> ElementoDuplicadoError:
    if elem in lista:
        raise ElementoDuplicadoError(f"Error: Imposible añadir elementos duplicados => {elem} ya existe en la lista")
    else:
        lista.append(elem)

################################################################
def main():
    listaOriginal = [1, 5, -2]
    agregar = [10, -2, "Hola", 7, "Arroz"]
    sumar = [10, 2, -7, 3]
    
    for valor in agregar + sumar: #Agregar + sumar
        try:
            agregar_una_vez(listaOriginal, valor)
        except ElementoDuplicadoError as e:
            print(f'{e}, {e.__class__}')


    print("Elementos de la lista:", listaOriginal)

if __name__ == "__main__":
    main()