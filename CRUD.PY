import mysql.connector
from datetime import datetime
#configuracion de conexion--------------------------------------------------------------------------------------
conexion = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)
cursor = conexion.cursor(dictionary=True)

#funciones del crud-----------------------------------------------------------------------------------------

#1 funciones de socio--------------------------------------------------------------------------------------
def nuevo_socio(nombre,apellido,telefono,DNI):
    cursor.execute("INSERT INTO socio(nombre, apellido, telefono, DNI) VALUES(%s, %s, %s, %s)", (nombre,apellido,telefono,DNI))
    conexion.commit()

    print("Socio agregado correctamente.")

def ver_socio():
    cursor.execute("SELECT * FROM socio")
    socio = cursor.fetchall()

    if not socio:
        print(" \n No hay socios registrados. \n")
        return

    print("\n Lista de socios registrados. \n")

    print("{:<10}{:<15}{:<15}{:<15}{:<12}".format("ID_socio","nombre","apellido","telefono","DNI"))
    print("-"*60)

    for u in socio:
        print("{:<10}{:<15}{:<15}{:<15}{:<12}".format(u['ID_socio'],u['nombre'],u['apellido'],u['telefono'],u['DNI']))
        print("-"*60)

def actualizar_socio(ID_socio, nombre, apellido, telefono, DNI):

    cursor.execute("UPDATE socio SET nombre=%s, apellido=%s, telefono=%s, DNI=%s WHERE ID_socio=%s", (nombre,apellido,telefono,DNI,ID_socio))
    conexion.commit()

    if cursor.rowcount>0:
        print("Socio actualizado.")
    else:
        print("No se encontro un socio con ese ID.")

def eliminar_socio(ID_socio):
    cursor.execute("DELETE FROM socio WHERE ID_socio=%s", (ID_socio,))
    conexion.commit()


    if cursor.rowcount > 0:
        print("Socio eliminado correctamente.")
    else:
        print("No se encontro un socio con ese ID.")

#2 funciones de bibliotecario-----------------------------------------------------------------------------

def nuevo_bilbiotecario(nombre,apellido,DNI):
    cursor.execute("INSERT INTO bibliotecario(nombre, apellido, DNI) VALUES(%s, %s, %s)", (nombre, apellido, DNI))
    conexion.commit()

def ver_bibliotecario():
    cursor.execute("SELECT * FROM bibliotecario")
    bibliotecario = cursor.fetchall()
    
    if not bibliotecario:
            print(" \n No hay bibliotecarios registrados. \n")
            return
    
    print("\n Lista de bibliotecarios registrados. \n")
    
    print("{:<15}{:<15}{:<15}{:<15}".format("ID_biblio","nombre","apellido","DNI"))
    print("-"*60)
    
    for u in bibliotecario:
            print("{:<15}{:<15}{:<15}{:<15}".format(u['ID_bibliotecario'],u['nombre'],u['apellido'],u['DNI']))
            print("-"*60)

def actualizar_bibliotecario(ID_bibliotecario, nombre, apellido, DNI):
    cursor.execute("UPDATE bibliotecario SET nombre=%s, apellido=%s, DNI=%s WHERE ID_bibliotecario=%s", (nombre,apellido,DNI,ID_bibliotecario))
    conexion.commit()
    
    if cursor.rowcount>0:
            print("bilbiotecario actualizado.")
    else:
            print("No se encontro un bibliotecario con ese ID.")

def eliminar_bibliotecario(ID_bibliotecario):
    cursor.execute("DELETE FROM bibliotecario WHERE ID_bibliotecario=%s", (ID_bibliotecario,))
    conexion.commit()
     
     
    if cursor.rowcount > 0:
     print("bibliotecario eliminado correctamente.")
    else:
     print("No se encontro un bibliotecario con ese ID.")

#3 funciones de genero---------------------------------------------------------------------------------------

def nuevo_genero(nombre):
    cursor.execute("INSERT INTO genero(nombre) VALUES(%s)", (nombre,))
    conexion.commit()

def ver_genero():
    cursor.execute("SELECT * FROM genero")
    genero = cursor.fetchall()
    
    if not genero:
            print(" \n No hay generos registrados. \n")
            return
    
    print("\n Lista de generos registrados. \n")
    
    print("{:<10}{:<15}".format("ID_genero","nombre"))
    print("-"*60)
    
    for u in genero:
            print("{:<10}{:<15}".format(u['ID_genero'],u['nombre']))
            print("-"*60)

def actualizar_genero(ID_genero, nombre):
    cursor.execute("UPDATE genero SET nombre=%s WHERE ID_genero=%s", (nombre,ID_genero))
    conexion.commit()
    
    if cursor.rowcount>0:
            print("genero actualizado.")
    else:
            print("No se encontro ningun genero con ese ID.")

def eliminar_genero(ID_genero):
    cursor.execute("DELETE FROM genero WHERE ID_genero=%s", (ID_genero,))
    conexion.commit()
     
     
    if cursor.rowcount > 0:
     print("genero eliminado correctamente.")
    else:
     print("No se encontro un genero con ese ID.")

#4 funciones de autor----------------------------------------------------------------------------------------

def nuevo_autor(nombre, apellido, nacionalidad):
    cursor.execute("INSERT INTO autor(nombre, apellido, nacionalidad) VALUES(%s, %s, %s)", (nombre, apellido, nacionalidad))
    conexion.commit()       

def ver_autor():
    cursor.execute("SELECT * FROM autor")
    autor = cursor.fetchall()
    
    if not autor:
            print(" \n No hay autores registrados. \n")
            return
    
    print("\n Lista de autores registrados. \n")
    
    print("{:<10}{:<15}{:<15}{:<15}".format("ID_autor","nombre","apellido","nacionalidad"))
    print("-"*60)
    
    for u in autor:
            print("{:<10}{:<15}{:<15}{:<15}".format(u['ID_autor'],u['nombre'],u['apellido'],u['nacionalidad']))
            print("-"*60)

def actualizar_autor(ID_autor, nombre, apellido, nacionalidad):
    cursor.execute("UPDATE autor SET nombre=%s, apellido=%s, nacionalidad=%s WHERE ID_autor=%s", (nombre, apellido, nacionalidad, ID_autor))
    conexion.commit()
    
    if cursor.rowcount>0:
            print("autor actualizado.")
    else:
            print("No se encontro un autor con ese ID.")

def eliminar_autor(ID_autor):
    cursor.execute("DELETE FROM autor WHERE ID_autor=%s", (ID_autor,))
    conexion.commit()
     
     
    if cursor.rowcount > 0:
     print("autor eliminado correctamente.")
    else:
     print("No se encontro un autor con ese ID.")

#5 funciones de editorial------------------------------------------------------------------------------------

def nueva_editorial(nombre, pais):
    cursor.execute("INSERT INTO editorial(nombre, pais) VALUES(%s, %s)", (nombre, pais))
    conexion.commit()  

def ver_editorial():
    cursor.execute("SELECT * FROM editorial")
    editorial = cursor.fetchall()
    
    if not editorial:
            print(" \n No hay editoriales registradas. \n")
            return
    
    print("\n Lista de editoriales registradas. \n")
    
    print("{:<15}{:<15}{:<15}".format("ID_editorial","nombre","pais"))
    print("-"*60)
    
    for u in editorial:
            print("{:<15}{:<15}{:<15}".format(u['ID_editorial'],u['nombre'],u['pais']))
            print("-"*60)

def actualizar_editorial(ID_editorial,nombre, pais):
    cursor.execute("UPDATE editorial SET nombre=%s, pais=%s WHERE ID_editorial=%s", (nombre, pais, ID_editorial))
    conexion.commit()
    
    if cursor.rowcount>0:
            print("editorial actualizada.")
    else:
            print("No se encontro una editorial con ese ID.")

def eliminar_editorial(ID_editorial):
    cursor.execute("DELETE FROM editorial WHERE ID_editorial=%s", (ID_editorial,))
    conexion.commit()
     
    if cursor.rowcount > 0:
     print("editorial eliminada correctamente.")
    else:
     print("No se encontro una editorial con ese ID.")

#6 funciones de libro----------------------------------------------------------------------------------------

def nuevo_libro(titulo, año_pub, editorial,genero):
    cursor.execute("SELECT ID_editorial FROM editorial WHERE nombre=%s", (editorial,))
    resultado_editorial = cursor.fetchone()

    cursor.execute("SELECT ID_genero FROM genero WHERE nombre=%s", (genero,))
    resultado_genero = cursor.fetchone()

    if not resultado_editorial or not resultado_genero:
        print("la editorial o el genero  no existen.")
        return

    FK_editorial = resultado_editorial['ID_editorial']
    FK_genero = resultado_genero['ID_genero']

    cursor.execute("INSERT INTO libro(titulo, año_pub, FK_editorial, FK_genero) VALUES(%s, %s, %s, %s)", (titulo, año_pub,FK_editorial,FK_genero))
    conexion.commit()
    print("Libro agregado correctamente.")

def ver_libro():
    cursor.execute("""SELECT libro.ID_libro, libro.titulo, libro.año_pub, Editorial.nombre AS editorial, genero.nombre AS genero FROM libro INNER JOIN editorial ON libro.FK_editorial = Editorial.ID_editorial INNER JOIN genero ON libro.FK_genero = genero.ID_genero""")
    libro = cursor.fetchall()
    if not libro:
         print("\n no hay libros registrados. \n")
         return

    print("\n lista de libros registrados \n")
    print("{:<10}{:<25}{:<15}{:<20}{:<20}".format("ID_libro", "titulo", "año_pub", "editorial", "genero"))
    
    print("-"*60)

    for u in libro:
        print("{:<10}{:<25}{:<15}{:<20}{:<20}".format(u['ID_libro'], u['titulo'], u['año_pub'],u['editorial'], u['genero']
        ))
        print("-"*60)
     
def actualizar_libro(ID_libro, titulo, año_pub, editorial, genero):
    cursor.execute("SELECT ID_editorial FROM editorial WHERE nombre=%s", (editorial,))
    resultado_editorial = cursor.fetchone()

    cursor.execute("SELECT ID_genero FROM genero WHERE nombre=%s", (genero,))
    resultado_genero = cursor.fetchone()

    if not resultado_editorial or not resultado_genero:
        print("La editorial o el genero no existen.")
        return

    FK_editorial = resultado_editorial['ID_editorial']
    FK_genero = resultado_genero['ID_genero']

    cursor.execute(
        "UPDATE libro SET titulo=%s, año_pub=%s, FK_editorial=%s, FK_genero=%s WHERE ID_libro=%s",
        (titulo, año_pub, FK_editorial, FK_genero, ID_libro)
    )
    conexion.commit()

    if cursor.rowcount > 0:
        print("Libro actualizado correctamente.")
    else:
        print("No se encontro un libro con ese ID.")

def eliminar_libro(ID_libro):
    cursor.execute("DELETE FROM libro WHERE ID_libro=%s", (ID_libro,))
    conexion.commit()

    if cursor.rowcount > 0:
        print("Libro eliminado correctamente.")
    else:
        print("No se encontro un libro con ese ID.")

#7 funciones de ejemplar----------------------------------------------------------------------------------

def nuevo_ejemplar(estado, ubicacion, titulo):

    cursor.execute("SELECT ID_libro FROM libro WHERE titulo=%s", (titulo,))
    resultado = cursor.fetchone()

    if not resultado:
        print("No existe un libro con ese titulo.")
        return

    FK_libro = resultado['ID_libro']

    cursor.execute(
        "INSERT INTO ejemplar(estado, ubicacion, FK_libro) VALUES(%s, %s, %s)",(estado, ubicacion, FK_libro))
    conexion.commit()

    print("Ejemplar agregado correctamente.")

def ver_ejemplar():

    cursor.execute("""SELECT ejemplar.ID_ejemplar, ejemplar.estado, ejemplar.ubicacion, libro.titulo FROM ejemplar INNER JOIN libro ON ejemplar.FK_libro = libro.ID_libro""")
    ejemplar = cursor.fetchall()

    if not ejemplar:
        print("\nNo hay ejemplares registrados.\n")
        return

    print("\nLista de ejemplares registrados.\n")
    print("{:<15}{:<20}{:<25}{:<25}".format("ID_ejemplar", "estado", "ubicacion", "libro"))
    print("-"*60)

    for u in ejemplar:
        print("{:<15}{:<20}{:<25}{:<25}".format(u['ID_ejemplar'], u['estado'],u['ubicacion'], u['titulo']))
        print("-"*60)

def actualizar_ejemplar(ID_ejemplar, estado, ubicacion, titulo):

    cursor.execute("SELECT ID_libro FROM libro WHERE titulo=%s", (titulo,))
    resultado = cursor.fetchone()

    if not resultado:
        print("No existe un libro con ese titulo.")
        return

    FK_libro = resultado['ID_libro']

    cursor.execute("UPDATE ejemplar SET estado=%s, ubicacion=%s, FK_libro=%s WHERE ID_ejemplar=%s",(estado, ubicacion, FK_libro, ID_ejemplar))
    conexion.commit()

    if cursor.rowcount > 0:
        print("Ejemplar actualizado correctamente.")
    else:
        print("No se encontro un ejemplar con ese ID.")

def eliminar_ejemplar(ID_ejemplar):

    cursor.execute("DELETE FROM ejemplar WHERE ID_ejemplar=%s", (ID_ejemplar,))
    conexion.commit()

    if cursor.rowcount > 0:
        print("Ejemplar eliminado correctamente.")
    else:
        print("No se encontro un ejemplar con ese ID.")

#8 funciones de libro_autor-------------------------------------------------------------------------------

def nuevo_libro_autor(titulo, nombre, apellido):
    cursor.execute("SELECT ID_libro FROM libro WHERE titulo=%s", (titulo,))
    resultado_libro = cursor.fetchone()

    cursor.execute("SELECT ID_autor FROM autor WHERE nombre=%s AND apellido=%s",(nombre, apellido))
    resultado_autor = cursor.fetchone()

    if not resultado_libro or not resultado_autor:
        print("El libro o el autor no existen.")
        return

    FK_libro = resultado_libro['ID_libro']
    FK_autor = resultado_autor['ID_autor']

    cursor.execute(
        "INSERT INTO Libro_autor(FK_libro, FK_autor) VALUES(%s, %s)", (FK_libro, FK_autor))
    conexion.commit()

    print("Relacion entre libro y autor agregada correctamente.")

def ver_libro_autor():
    cursor.execute("""SELECT libro.titulo,autor.nombre,autor.apellido FROM Libro_autor INNER JOIN libro ON Libro_autor.FK_libro = libro.ID_libro INNER JOIN autor ON Libro_autor.FK_autor = autor.ID_autor""")
    libro_autor = cursor.fetchall()

    if not libro_autor:
        print("\nNo hay relaciones registradas.\n")
        return

    print("\nLibros y autores relacionados.\n")
    print("{:<30}{:<20}{:<20}".format("libro", "nombre", "apellido"))
    print("-"*60)

    for u in libro_autor:
        print("{:<30}{:<20}{:<20}".format(u['titulo'], u['nombre'], u['apellido']))
        print("-"*60)

def actualizar_libro_autor(titulo_anterior, nombre_anterior, apellido_anterior, titulo_nuevo, nombre_nuevo, apellido_nuevo):
    cursor.execute("SELECT ID_libro FROM libro WHERE titulo=%s", (titulo_anterior,))
    resultado_libro_anterior = cursor.fetchone()

    cursor.execute("SELECT ID_autor FROM autor WHERE nombre=%s AND apellido=%s",(nombre_anterior, apellido_anterior))
    resultado_autor_anterior = cursor.fetchone()

    cursor.execute("SELECT ID_libro FROM libro WHERE titulo=%s", (titulo_nuevo,))
    resultado_libro_nuevo = cursor.fetchone()

    cursor.execute("SELECT ID_autor FROM autor WHERE nombre=%s AND apellido=%s",(nombre_nuevo, apellido_nuevo))
    resultado_autor_nuevo = cursor.fetchone()

    if not resultado_libro_anterior or not resultado_autor_anterior or not resultado_libro_nuevo or not resultado_autor_nuevo:
        print("No se encontraron los datos ingresados.")
        return

    cursor.execute("UPDATE Libro_autor SET FK_libro=%s, FK_autor=%s WHERE FK_libro=%s AND FK_autor=%s",(resultado_libro_nuevo['ID_libro'],resultado_autor_nuevo['ID_autor'],resultado_libro_anterior['ID_libro'],resultado_autor_anterior['ID_autor']))
    conexion.commit()

    if cursor.rowcount > 0:
        print("Relacion actualizada correctamente.")
    else:
        print("No se encontro esa relacion.")

def eliminar_libro_autor(titulo, nombre, apellido):
    cursor.execute("SELECT ID_libro FROM libro WHERE titulo=%s", (titulo,))
    resultado_libro = cursor.fetchone()

    cursor.execute("SELECT ID_autor FROM autor WHERE nombre=%s AND apellido=%s",(nombre, apellido))
    resultado_autor = cursor.fetchone()

    if not resultado_libro or not resultado_autor:
        print("No se encontraron el libro o el autor.")
        return

    cursor.execute("DELETE FROM Libro_autor WHERE FK_libro=%s AND FK_autor=%s",(resultado_libro['ID_libro'], resultado_autor['ID_autor']))
    conexion.commit()

    if cursor.rowcount > 0:
        print("Relacion eliminada correctamente.")
    else:
        print("No se encontro esa relacion.")

#9 funciones de prestamo-----------------------------------------------------------------------------------

def nuevo_prestamo(fecha_prestamo, fecha_devolucion, DNI_socio, DNI_bibliotecario, ID_ejemplar):

    try:
        # Buscar socio
        cursor.execute(
            "SELECT ID_socio FROM socio WHERE DNI=%s",
            (DNI_socio,)
        )
        resultado_socio = cursor.fetchone()

        if not resultado_socio:
            print("No existe un socio con ese DNI.")
            return

        # Buscar bibliotecario
        cursor.execute(
            "SELECT ID_bibliotecario FROM bibliotecario WHERE DNI=%s",
            (DNI_bibliotecario,)
        )
        resultado_bibliotecario = cursor.fetchone()

        if not resultado_bibliotecario:
            print("No existe un bibliotecario con ese DNI.")
            return

        # Buscar ejemplar
        print("ID ingresado:", repr(ID_ejemplar))

        cursor.execute(
            "SELECT ID_ejemplar, estado FROM ejemplar WHERE ID_ejemplar=%s",
            (ID_ejemplar,)
        )
        resultado_ejemplar = cursor.fetchone()

        print("Resultado de la consulta:", resultado_ejemplar)

        if not resultado_ejemplar:
            print("No existe un ejemplar con ese ID.")
            return

        print("Estado leído por Python:", repr(resultado_ejemplar['estado']))

        if resultado_ejemplar['estado'].strip().lower() != "disponible":
            print("El ejemplar no está disponible.")
            return

        # Obtener las claves foráneas
        FK_socio = resultado_socio['ID_socio']
        FK_bibliotecario = resultado_bibliotecario['ID_bibliotecario']

        # Registrar préstamo
        cursor.execute(
            """INSERT INTO prestamo
            (fecha_prestamo, fecha_devolucion, FK_socio, FK_ejemplar, FK_bibliotecario)
            VALUES (%s, %s, %s, %s, %s)""",
            (fecha_prestamo, fecha_devolucion, FK_socio, ID_ejemplar, FK_bibliotecario)
        )

        # Cambiar estado del ejemplar
        cursor.execute(
            "UPDATE ejemplar SET estado='Prestado' WHERE ID_ejemplar=%s",
            (ID_ejemplar,)
        )

        conexion.commit()

        print("Préstamo registrado correctamente.")

    except mysql.connector.Error as error:
        conexion.rollback()
        print("Error al registrar el préstamo:", error)
def ver_prestamo():
    cursor.execute("""SELECT prestamo.ID_prestamo,prestamo.fecha_prestamo,prestamo.fecha_devolucion,socio.nombre AS nombre_socio,socio.apellido AS apellido_socio,libro.titulo AS libro,ejemplar.ID_ejemplar,bibliotecario.nombre AS nombre_bibliotecario,bibliotecario.apellido AS apellido_bibliotecario FROM prestamo INNER JOIN socio ON prestamo.FK_socio = socio.ID_socio INNER JOIN ejemplar ON prestamo.FK_ejemplar = ejemplar.ID_ejemplar INNER JOIN libro ON ejemplar.FK_libro = libro.ID_libro INNER JOIN bibliotecario ON prestamo.FK_bibliotecario = bibliotecario.ID_bibliotecario""")
    prestamo = cursor.fetchall()

    if not prestamo:
        print("\nNo hay prestamos registrados.\n")
        return

    print("\nLista de prestamos registrados.\n")

    print("{:<10}{:<22}{:<22}{:<25}{:<20}{:<15}{:<25}".format("ID", "fecha_prestamo", "fecha_devolucion","socio", "libro", "ejemplar", "bibliotecario"))
    print("-"*60)

    for u in prestamo:
        socio_nombre = u['nombre_socio'] + " " + u['apellido_socio']
        bibliotecario_nombre = u['nombre_bibliotecario'] + " " + u['apellido_bibliotecario']

        print("{:<10}{:<22}{:<22}{:<25}{:<20}{:<15}{:<25}".format(u['ID_prestamo'],str(u['fecha_prestamo']),str(u['fecha_devolucion']),socio_nombre,u['libro'],u['ID_ejemplar'],bibliotecario_nombre))
        print("-"*60)

def actualizar_prestamo(ID_prestamo, fecha_prestamo, fecha_devolucion, DNI_socio, DNI_bibliotecario, ID_ejemplar):
    cursor.execute("SELECT ID_socio FROM socio WHERE DNI=%s", (DNI_socio,))
    resultado_socio = cursor.fetchone()

    cursor.execute("SELECT ID_bibliotecario FROM bibliotecario WHERE DNI=%s",(DNI_bibliotecario,))
    resultado_bibliotecario = cursor.fetchone()

    cursor.execute("SELECT estado FROM ejemplar WHERE ID_ejemplar=%s",(ID_ejemplar,))
    resultado_ejemplar = cursor.fetchone()

    if not resultado_socio or not resultado_bibliotecario or not resultado_ejemplar:
        print("No se encontraron los datos ingresados.")
        return

    FK_socio = resultado_socio['ID_socio']
    FK_bibliotecario = resultado_bibliotecario['ID_bibliotecario']

    cursor.execute("UPDATE prestamo SET fecha_prestamo=%s, fecha_devolucion=%s, FK_socio=%s, FK_ejemplar=%s, FK_bibliotecario=%s WHERE ID_prestamo=%s",(fecha_prestamo, fecha_devolucion, FK_socio, ID_ejemplar, FK_bibliotecario, ID_prestamo))
    conexion.commit()

    if cursor.rowcount > 0:
        print("Prestamo actualizado correctamente.")
    else:
        print("No se encontro un prestamo con ese ID.")

def eliminar_prestamo(ID_prestamo):
    cursor.execute("SELECT FK_ejemplar FROM prestamo WHERE ID_prestamo=%s",(ID_prestamo,))
    resultado = cursor.fetchone()

    if not resultado:
        print("No se encontro un prestamo con ese ID.")
        return

    ID_ejemplar = resultado['FK_ejemplar']

    cursor.execute("DELETE FROM prestamo WHERE ID_prestamo=%s",(ID_prestamo,))

    cursor.execute("UPDATE ejemplar SET estado='Disponible' WHERE ID_ejemplar=%s",(ID_ejemplar,))
    conexion.commit()

    print("Prestamo eliminado correctamente.")

#menu principal---------------------------------------------------------------------------------------------

while True:
    
    print("1. opciones socios.")
    print("2. opciones bibliotecarios.")
    print("3. opciones genero.")
    print("4. opciones autor.")
    print("5. opciones editorial.")
    print("6. opciones libro.")
    print("7. opciones ejemplar.")
    print("8. opciones libro_autor.")
    print("9. opciones prestamo.")
    print("10. salir del programa.")

    opcion1 = input("Selecciona una opcion: ")

#si selecciona 1 = menu de socios--------------------------------------------------------------------------------
    if opcion1 == "1":
        while True:
            print("1. Nuevo socio.")
            print("2. Leer socios.")
            print("3. Actualizar socio.")
            print("4. Eliminar socio.")
            print("5. volver al menu principal")

            sub_op = input("ingresa tu siguente opcion: ")

            if sub_op == "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                telefono = input("Telefono: ")
                DNI = input ("DNI: ")
                nuevo_socio(nombre, apellido, telefono, DNI)

            elif sub_op == "2":
                ver_socio()

            elif sub_op == "3":
                ID_socio = input("ID del socio a actualizar: ")
                nombre =  input("Nuevo nombre: ")
                apellido = input("Nuevo apellido: ")
                telefono = input("Nuevo telefono: ")
                DNI = input ("DNI: ")  
                actualizar_socio(ID_socio, nombre, apellido, telefono, DNI)

            elif sub_op == "4":
                ID_socio = input("ID del socio a eliminar: ")
                eliminar_socio(ID_socio)

            elif sub_op == "5":
                print("regresando al menu principal...")
                break

            else: 
                print("opcion no valida")

#si selecciona 2 = menu de bibliotecario--------------------------------------------------------------------
    elif opcion1 == "2":
        while True:
            print("1. Nuevo bibliotecario.")
            print("2. Leer bibliotecarios.")
            print("3. Actualizar bibliotecario.")
            print("4. Eliminar bibliotecario.")
            print("5. volver al menu principal")
        
            sub_op = input("ingresa tu siguente opcion: ")
        
            if sub_op == "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                DNI = input ("DNI: ")
                nuevo_bilbiotecario(nombre, apellido, DNI)
        
            elif sub_op == "2":
                ver_bibliotecario()  

            elif sub_op == "3":
                ID_bibliotecario = input("ID del bibliotecario a actualizar: ")
                nombre =  input("Nuevo nombre: ")    
                apellido = input("Nuevo apellido: ")
                DNI = input ("DNI: ")  
                actualizar_bibliotecario(ID_bibliotecario, nombre, apellido, DNI)
        
            elif sub_op == "4":
                ID_bibliotecario = input("ID del bibliotecario a eliminar: ")
                eliminar_bibliotecario(ID_bibliotecario)
        
            elif sub_op == "5":
                print("regresando al menu principal...")
                break

#si selecciona 3 = menu de genero------------------------------------------------------------------------- 
    elif opcion1 == "3":
        while True:
            print("1. Nuevo genero.")
            print("2. Leer genero.")
            print("3. Actualizar genero.")
            print("4. Eliminar genero.")
            print("5. volver al menu principal")

            sub_op = input("Ingresa tu siguiente opcion: ")

            if sub_op == "1":
                nombre = input("Nombre del genero: ")
                nuevo_genero(nombre)

            elif sub_op == "2":
                ver_genero()

            elif sub_op == "3":
                ID_genero = input("ID del genero a actualizar: ")
                nombre = input("Nuevo nombre: ")
                actualizar_genero(ID_genero, nombre)

            elif sub_op == "4":
                ID_genero = input("ID del genero a eliminar: ")
                eliminar_genero(ID_genero)

            elif sub_op == "5":
                print("regresando al menu principal...")
                break

            else:
                print("Opcion no valida.")

#si selecciona 4 = menu de autor--------------------------------------------------------------------------
    elif opcion1 == "4":
        while True:
            print("1. Nuevo autor.")
            print("2. Leer autores.")
            print("3. Actualizar autor.")
            print("4. Eliminar autor.")
            print("5. Volver al menu principal.")

            sub_op = input("Ingresa tu siguiente opcion: ")

            if sub_op == "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                nacionalidad = input("Nacionalidad: ")
                nuevo_autor(nombre, apellido, nacionalidad)

            elif sub_op == "2":
                ver_autor()

            elif sub_op == "3":
                ID_autor = input("ID del autor a actualizar: ")
                nombre = input("Nuevo nombre: ")
                apellido = input("Nuevo apellido: ")
                nacionalidad = input("Nueva nacionalidad: ")
                actualizar_autor(ID_autor, nombre, apellido, nacionalidad)

            elif sub_op == "4":
                ID_autor = input("ID del autor a eliminar: ")
                eliminar_autor(ID_autor)

            elif sub_op == "5":
                print("volviendo al menu principal...")
                break

            else:
                print("Opcion no valida.")

#si selecciona 5 == menu de editorial---------------------------------------------------------------------
    elif opcion1 == "5":
        while True:
            print("1. Nueva editorial.")
            print("2. Leer editoriales.")
            print("3. Actualizar editorial.")
            print("4. Eliminar editorial.")
            print("5. Volver al menu principal.")

            sub_op = input("Ingresa tu siguiente opcion: ")

            if sub_op == "1":
                nombre = input("Nombre: ")
                pais = input("Pais: ")
                nueva_editorial(nombre, pais)

            elif sub_op == "2":
                ver_editorial()

            elif sub_op == "3":
                ID_editorial = input("ID de la editorial a actualizar: ")
                nombre = input("Nuevo nombre: ")
                pais = input("Nuevo pais: ")
                actualizar_editorial(ID_editorial, nombre, pais)

            elif sub_op == "4":
                ID_editorial = input("ID de la editorial a eliminar: ")
                eliminar_editorial(ID_editorial)

            elif sub_op == "5":
                print("volviendo al menu principal...")
                break

            else:
                print("Opcion no valida.")

#si selecciona 6 = menu de libro---------------------------------------------------------------------------
    elif opcion1 == "6":
        while True:
            print("1. Nuevo libro.")
            print("2. Leer libros.")
            print("3. Actualizar libro.")
            print("4. Eliminar libro.")
            print("5. Volver al menu principal.")

            sub_op = input("Ingresa tu siguiente opcion: ")

            if sub_op == "1":
                titulo = input("Titulo: ")
                anio_pub = input("Año de publicacion: ")
                editorial = input("Nombre de la editorial: ")
                genero = input("Nombre del genero: ")
                nuevo_libro(titulo, anio_pub, editorial, genero)

            elif sub_op == "2":
                ver_libro()

            elif sub_op == "3":
                ID_libro = input("ID del libro a actualizar: ")
                titulo = input("Nuevo titulo: ")
                anio_pub = input("Nuevo año de publicacion: ")
                editorial = input("Nombre de la editorial: ")
                genero = input("Nombre del genero: ")
                actualizar_libro(ID_libro, titulo, anio_pub, editorial, genero)

            elif sub_op == "4":
                ID_libro = input("ID del libro a eliminar: ")
                eliminar_libro(ID_libro)

            elif sub_op == "5":
                print("volviendo al menu principal..")
                break

            else:
                print("Opcion no valida.")

#si selecciona 7 = menu de ejemplar-------------------------------------------------------------------------
    elif opcion1 == "7":
        while True:
            print("1. Nuevo ejemplar.")
            print("2. Leer ejemplares.")
            print("3. Actualizar ejemplar.")
            print("4. Eliminar ejemplar.")
            print("5. Volver al menu principal.")

            sub_op = input("Ingresa tu siguiente opcion: ")

            if sub_op == "1":
                estado = input("Estado: ")
                ubicacion = input("Ubicacion: ")
                titulo = input("Titulo del libro: ")
                nuevo_ejemplar(estado, ubicacion, titulo)

            elif sub_op == "2":
                ver_ejemplar()

            elif sub_op == "3":
                ID_ejemplar = input("ID del ejemplar a actualizar: ")
                estado = input("Nuevo estado: ")
                ubicacion = input("Nueva ubicacion: ")
                titulo = input("Titulo del libro: ")
                actualizar_ejemplar(ID_ejemplar, estado, ubicacion, titulo)

            elif sub_op == "4":
                ID_ejemplar = input("ID del ejemplar a eliminar: ")
                eliminar_ejemplar(ID_ejemplar)

            elif sub_op == "5":
                print("volviendo al menu principal...")
                break

            else:
                print("Opcion no valida.")

#si selecciona 8 = menu de libro_autor--------------------------------------------------------------------
    elif opcion1 == "8":
        while True:
            print("1. Agregar relacion libro-autor.")
            print("2. Leer relaciones libro-autor.")
            print("3. Actualizar relacion libro-autor.")
            print("4. Eliminar relacion libro-autor.")
            print("5. Volver al menu principal.")

            sub_op = input("Ingresa tu siguiente opcion: ")

            if sub_op == "1":
                titulo = input("Titulo del libro: ")
                nombre = input("Nombre del autor: ")
                apellido = input("Apellido del autor: ")
                nuevo_libro_autor(titulo, nombre, apellido)

            elif sub_op == "2":
                ver_libro_autor()

            elif sub_op == "3":
                titulo_anterior = input("Titulo actual del libro: ")
                nombre_anterior = input("Nombre actual del autor: ")
                apellido_anterior = input("Apellido actual del autor: ")

                titulo_nuevo = input("Nuevo titulo del libro: ")
                nombre_nuevo = input("Nuevo nombre del autor: ")
                apellido_nuevo = input("Nuevo apellido del autor: ")

                actualizar_libro_autor(
                    titulo_anterior, nombre_anterior, apellido_anterior,
                    titulo_nuevo, nombre_nuevo, apellido_nuevo
                )

            elif sub_op == "4":
                titulo = input("Titulo del libro: ")
                nombre = input("Nombre del autor: ")
                apellido = input("Apellido del autor: ")
                eliminar_libro_autor(titulo, nombre, apellido)

            elif sub_op == "5":
                print("volviendo al menu principal...")
                break

            else:
                print("Opcion no valida.")

#si selecciona 9 = menu de prestamo-----------------------------------------------------------------------
    elif opcion1 == "9":
        while True:
            print("1. Nuevo prestamo.")
            print("2. Leer prestamos.")
            print("3. Actualizar prestamo.")
            print("4. Eliminar prestamo.")
            print("5. Volver al menu principal.")

            sub_op = input("Ingresa tu siguiente opcion: ")

            if sub_op == "1":
    
                fecha_prestamo = datetime.strptime(input("Fecha del prestamo (AAAA-MM-DD HH:MM:SS): "),"%Y-%m-%d %H:%M:%S")

                fecha_devolucion = datetime.strptime(input("Fecha de devolucion (AAAA-MM-DD HH:MM:SS): "), "%Y-%m-%d %H:%M:%S")

                DNI_socio = input("DNI del socio: ")
                DNI_bibliotecario = input("DNI del bibliotecario: ")
                ID_ejemplar = input("ID del ejemplar: ")

                nuevo_prestamo(fecha_prestamo,fecha_devolucion,DNI_socio,DNI_bibliotecario,ID_ejemplar)
                resultado_ejemplar = cursor.fetchone()
            elif sub_op == "2":
                ver_prestamo()

            elif sub_op == "3":
                ID_prestamo = input("ID del prestamo a actualizar: ")
                fecha_prestamo = input("Nueva fecha del prestamo: ")
                fecha_devolucion = input("Nueva fecha de devolucion: ")
                DNI_socio = input("DNI del socio: ")
                DNI_bibliotecario = input("DNI del bibliotecario: ")
                ID_ejemplar = input("ID del ejemplar: ")

                actualizar_prestamo(
                    ID_prestamo, fecha_prestamo, fecha_devolucion,
                    DNI_socio, DNI_bibliotecario, ID_ejemplar
                )

            elif sub_op == "4":
                ID_prestamo = input("ID del prestamo a eliminar: ")
                eliminar_prestamo(ID_prestamo)

            elif sub_op == "5":
                print("volviendo al menu principal...")
                break

            else:
                print("Opcion no valida.")

#si selecciona 10 = salir del programa-----------------------------------------------------------------------
    elif opcion1 == "10":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida.")

cursor.close()
conexion.close()
