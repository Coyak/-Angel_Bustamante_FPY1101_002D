Libros=[]

def menu():
    while True:
        print("\nGestion de Biblioteca personal :)")
        opc = int(input("\n1.-Agregar un libro\n2.-Ver todos los libros\n3.Modificar un libro-\n4.-Eliminar un libro.\n5.-Guardar colección en un archivo\n6.-Salir del programa.\nPor favor Eliga una de las sigientes opciones: ").encode('utf-8'))
        if opc == 1:
            print("se seleciono Agregar un libro.")
            agregarlibros()
        elif opc == 2:
            print("se seleciono Ver todos los libros")
            vertodoslibros()
        elif opc == 3:
            print("se seleciono Modificar un libro")
        elif opc == 4:
            print("se seleciono Eliminar un libro")
            eliminarlibros()
        elif opc == 5:
            print("se seleciono Guardar colección en un archivo")
            Guardarlibros()
        elif opc == 6:
            print("se seleciono Salir")
            break
        else:
            print("ingrese una opcion valida del 1/6")

def agregarlibros():
    try:
        libro=input("Ingrese el nombre del libro-->");
    except ValueError:
        print("Error ingrese el nombre del libro nuevamente :(");
    else:
        try:
            autor=input("Ingrese el nombre del autor-->");
        except ValueError:
            print("error ingrese el nombre del autor nuevamente :<");
        else:
            try:
                año=input("Ingrese el año de publicacion del libro-->");
            except ValueError:
                print("error ingrese el año de publicacion del libro nuevamente :(");
            try:
                genero=input("Ingrese el genero del libro-->");
            except ValueError:
                print("error ingrese el genero del libro nuevamente :<");

    agregar_libros = {
            'libro':libro,
            'autor':autor,
            'año':año,
            'genero':genero,
        }
    Libros.append(agregar_libros)
    print("libro ingresado correctamente :)\n");
    return

def vertodoslibros():
    if not Libros:
        print("no hay libros registrados :,<");
    else:
        print("libros registrados:")
        for x in Libros:
            print(f"Libro: {x['libro']}, Autor: {x['autor']}, Año:{x['año']}, Genero:{x['genero']}") 
            print()

def modificarlibros():
    with open(f"libros.txt",'r+',newline='',encoding='Utf-8') as guardalibros:
        print(Libros)
        libro_modificar = input("Ingrese el nombre del libro que desea modificar: ").encode('utf-8')
        autor_modificar = input("Ingrese el nombre del autor que desea modificar: ").encode('utf-8')
        time_modificar = input("Ingrese el año de publicacion del libro que desea modificar: ").encode
        genero_modificar = input("Ingrese el genero del libro que desea modificar: ").encode('utf-8')
        if libro_modificar in Libros:
            for x in Libros:
                if x['libro'] == libro_modificar and x['autor'] == autor_modificar:
                    x['libro'] = libro_modificar
                    x['autor'] = autor_modificar
                    x['año'] = time_modificar
                    x['genero'] = genero_modificar
                    print("Libro modificado correctamente :)\n")
                    return
                else:
                    print("Libro ingresado no esta en la lista...")

"""""
def eliminarlibros():
"""""

def Guardarlibros():
    with open(f"libros.txt",'w',newline='',encoding='Utf-8') as guardalibros:
        for x in Libros:
            guardalibros.write(f"Libro: {x['libro']}, Autor: {x['autor']}, Año:{x['año']}, Genero:{x['genero']}") 
            guardalibros.write("\n") 
menu()