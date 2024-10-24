class ElementoDuplicadoError(ValueError):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f'{self.mensaje}'

def agregar_una_vez(lista, elem) -> ElementoDuplicadoError:
    if elem in lista:
        raise ElementoDuplicadoError(f"Error: Imposible añadir elementos duplicados => {elem} ya existe en la lista")
    else:
        lista.append(elem)

def main():
    listaOriginal = [1, 5, -2]
    agregar = [10, -2, "Hola", 7, "Arroz"]
    sumar = [10, 2, -7, 3]
    agregar_una_vez(listaOriginal, 5)

    for valor in agregar:
        try:
            agregar_una_vez(listaOriginal, valor)
        except ElementoDuplicadoError as e:
            print(f'{e}, {e.__class__}')
            
    for valor in sumar:
        try:
            agregar_una_vez(listaOriginal, valor)
        except ValueError as e:
            print(f'{e}')
            


    print("Elementos de la lista:", listaOriginal)

if __name__ == "__main__":
    main()