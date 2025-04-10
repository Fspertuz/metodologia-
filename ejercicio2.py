class Cuadrilatero:
    def __init__(self, base, altura):
        # Asegurarse de que tanto la base como la altura sean mayores que cero
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero.")
        self.__base = base  # Atributo privado
        self.__altura = altura  # Atributo privado
    
    # Método para actualizar las dimensiones del cuadrilátero
    def actualizar_dimensiones(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero.")
        self.__base = base
        self.__altura = altura
    
    # Método para calcular el área del cuadrilátero
    def calcular_area(self):
        return self.__base * self.__altura
    
    # Método para calcular el perímetro del cuadrilátero
    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)
    
    # Método para obtener las dimensiones actuales
    def obtener_dimensiones(self):
        return f"Base: {self.__base}, Altura: {self.__altura}"

# Ejemplo
try:
    # Crear un cuadrilátero con base 6 y altura 4
    cuadrilatero = Cuadrilatero(6, 4)
    
    # Consultar las dimensiones actuales
    print(f"Dimensiones iniciales: {cuadrilatero.obtener_dimensiones()}")
    
    # Calcular y mostrar el área
    print(f"Área del cuadrilátero: {cuadrilatero.calcular_area()} unidades cuadradas")
    
    # Calcular y mostrar el perímetro
    print(f"Perímetro del cuadrilátero: {cuadrilatero.calcular_perimetro()} unidades")
    
    # Cambiar las dimensiones del cuadrilátero
    cuadrilatero.actualizar_dimensiones(10, 5)
    print(f"Dimensiones después de cambiar: {cuadrilatero.obtener_dimensiones()}")
    
    # Intentar cambiar las dimensiones a valores no válidos (negativos)
    cuadrilatero.actualizar_dimensiones(-3, 4)
except ValueError as e:
    print(e)
