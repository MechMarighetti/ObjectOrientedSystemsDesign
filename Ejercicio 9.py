class ListaDeTareas:
    def __init__(self):
        self.__lista_tareas = []

    # Agregar una tarea a la lista
    def agregarTarea(self, tarea):
        if tarea:  # Verifica que la tarea exista 
            self.__lista_tareas.append(tarea)
            return "Tarea agregada correctamente a la lista"
        else:
            return "La tarea no fue agregada a la lista"

    # Eliminar una tarea de la lista
    def eliminarTarea(self, tarea):
        if tarea in self.__lista_tareas:
            self.__lista_tareas.remove(tarea)
            return "Tarea eliminada correctamente de la lista"
        else:
            return "La tarea no fue eliminada de la lista"

    # Método para mostrar la lista de tareas
    def mostrarTareas(self):
        return self.__lista_tareas

if __name__ == '__main__':
    mi_lista = ListaDeTareas()

# Agregar tareas
    print(mi_lista.agregarTarea("Lavar ropa"))  
    print(mi_lista.agregarTarea("Pilates"))  
    print(mi_lista.agregarTarea("Regar plantas"))  

# Mostrar tareas
    print("Tareas actuales:", mi_lista.mostrarTareas()) 

# Eliminar una tarea
    print(mi_lista.eliminarTarea("Lavar ropa")) 

# Intentar quitar una tarea que no existe
    print(mi_lista.eliminarTarea("Estudiar"))  

# Mostrar las tareas restantes
    print("Tareas actuales:", mi_lista.mostrarTareas()) 