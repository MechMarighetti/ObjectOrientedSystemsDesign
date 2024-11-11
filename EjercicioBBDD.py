import sqlite3

def conectar():
    return sqlite3.connect('empleados.db')

def crearTabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nro_legajo INTEGER NOT NULL UNIQUE,
            dni INTEGER NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            area TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insertar_empleado():
    try:
        conn = conectar()
        cursor = conn.cursor()
        nro_legajo = int(input("Ingrese el número de legajo: "))
        dni = int(input("Ingrese el DNI: "))
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        area = input("Ingrese el área: ")

        cursor.execute('''
            INSERT INTO empleados (nro_legajo, dni, nombre, apellido, area)
            VALUES (?, ?, ?, ?, ?)
        ''', (nro_legajo, dni, nombre, apellido, area))
        conn.commit()
        print("Empleado insertado correctamente.")
    except sqlite3.IntegrityError as e:
        print(f"Error al insertar el empleado: {e}")
    finally:
        conn.close()

def seleccionar_empleado_por_dni():
    try:
        conn = conectar()
        cursor = conn.cursor()
        dni = int(input("Ingrese el DNI del empleado: "))
        cursor.execute('SELECT * FROM empleados WHERE dni = ?', (dni,))
        empleado = cursor.fetchone()
        if empleado:
            print(f"Empleado encontrado: {empleado}")
        else:
            print("Empleado no encontrado.")
    finally:
        conn.close()

def seleccionar_todos_los_empleados():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM empleados')
        empleados = cursor.fetchall()
        for empleado in empleados:
            print(empleado)
    finally:
        conn.close()

def modificar_area_empleado():
    try:
        conn = conectar()
        cursor = conn.cursor()
        nro_legajo = int(input("Ingrese el número de legajo del empleado: "))
        nuevo_area = input("Ingrese el nuevo área: ")
        cursor.execute('''
            UPDATE empleados
            SET area = ?
            WHERE nro_legajo = ?
        ''', (nuevo_area, nro_legajo))
        conn.commit()
        if cursor.rowcount > 0:
            print("Área del empleado modificada correctamente.")
        else:
            print("Empleado no encontrado.")
    finally:
        conn.close()

def eliminar_empleado():
    try:
        conn = conectar()
        cursor = conn.cursor()
        nro_legajo = int(input("Ingrese el número de legajo del empleado: "))
        cursor.execute('DELETE FROM empleados WHERE nro_legajo = ?', (nro_legajo,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Empleado eliminado correctamente.")
        else:
            print("Empleado no encontrado.")
    finally:
        conn.close()

def main():
    crearTabla()
    while True:
        print("\nOpciones:")
        print("1. Insertar un registro de empleado.")
        print("2. Seleccionar un registro de empleado a partir de su número DNI.")
        print("3. Seleccionar todos los empleados o los registros de la tabla.")
        print("4. Modificar el área de un empleado en función de su número de legajo.")
        print("5. Eliminar un empleado a partir del número de legajo.")
        print("6. Finalizar.")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            insertar_empleado()
        elif opcion == '2':
            seleccionar_empleado_por_dni()
        elif opcion == '3':
            seleccionar_todos_los_empleados()
        elif opcion == '4':
            modificar_area_empleado()
        elif opcion == '5':
            eliminar_empleado()
        elif opcion == '6':
            print("Finalizando...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()