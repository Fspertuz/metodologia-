class Book:
    def __init__(self, name, writer, total_pages):
        self.__name = name  # Atributo privado
        self.__writer = writer  # Atributo privado
        self.__total_pages = total_pages  # Atributo privado
        self.__current_page = 1  # El lector comienza en la página 1

    # Método para avanzar un número de páginas
    def move_forward(self, pages):
        if self.__current_page + pages > self.__total_pages:
            raise ValueError(f"No puedes avanzar más allá de la página {self.__total_pages}.")
        self.__current_page += pages

    # Método para retroceder un número de páginas
    def move_back(self, pages):
        if self.__current_page - pages < 1:
            raise ValueError("No puedes retroceder más allá de la página 1.")
        self.__current_page -= pages

    # Método para consultar la página actual
    def get_current_page(self):
        return self.__current_page

    # Método para obtener la información completa del libro
    def get_book_info(self):
        return f"Nombre: {self.__name}\nEscritor: {self.__writer}\nTotal de Páginas: {self.__total_pages}\nPágina Actual: {self.__current_page}"

# Ejemplo
try:
    book = Book("El amor en los tiempos del cólera", "Gabriel García Márquez", 400)
    
    # Avanzar 80 páginas
    book.move_forward(80)
    print(f"Página actual después de avanzar 80 páginas: {book.get_current_page()}")
    
    # Retroceder 30 páginas
    book.move_back(30)
    print(f"Página actual después de retroceder 30 páginas: {book.get_current_page()}")
    
    # Intentar retroceder más allá de la página 1 (esto lanzará un error)
    book.move_back(500)
except ValueError as e:
    print(e)

# Obtener la información completa del libro
print("\nInformación del libro:")
print(book.get_book_info())
