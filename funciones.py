import libros.txt as txt
Libros=[]

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

    libros = {
            'libro':libro,
            'autor':autor,
            'año':año,
            'genero':genero,
        }
    libros.append(libros)
    print("libro ingresado correctamente :)\n");
    return

def vertodoslibros():
    if not libros:
        print("no hay libros registrados :,<");
    else:
        print("libros registrados:")
        for libros in Libros:
            print(f"Libro: {Libros['libro']}, Autor: {Libros['autor']}, Año:{Libros['año']}, Genero:{Libros['genero']}") 
            print()

def modificarlibros():
    with open(f"libros.txt", 'w',newline='',encoding='Utf-8') as guardalibros:


def eliminarlibros():
    print(libros);
    libro_eliminar=input("Ingrese el nombre del libro que desea eliminar-->");
    autor_eliminar=input("Ingrese el nombre del autor del libro que desea eliminar-->");
    if libro_eliminar in Libros:
        print("error el libro que desea eliminar no se encuentra registrado :<");
    else:
        Libros.remove(libro_eliminar);
        print("libro eliminado correctamente :)\n");
    


def Guardarlibros():
    if not Libros:
     print("No se encuentran libros registrados.")
    return    

with open(f"libros.txt", 'a',newline='',encoding='Utf-8') as guardalibros:
    for libros in Libros:
    file.write(newline='',encoding='Utf-8') 