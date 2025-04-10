class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Las bases y la altura deben ser mayores que cero.")
        self.__base_mayor = base_mayor  
        self.__base_menor = base_menor  
        self.__altura = altura  
    
    
    def actualizar_dimensiones(self, base_mayor, base_menor, altura):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Las bases y la altura deben ser mayores que cero.")
        self.__base_mayor = base_mayor
        self.__base_menor = base_menor
        self.__altura = altura
    
   
    def calcular_area(self):
        return ((self.__base_mayor + self.__base_menor) * self.__altura) / 2
   
    def calcular_perimetro(self):
        lado_no_paralelo = ((self.__base_mayor - self.__base_menor) ** 2 + self.__altura ** 2) ** 0.5
        return self.__base_mayor + self.__base_menor + 2 * lado_no_paralelo
    
    def obtener_dimensiones(self):
        return f"Base mayor: {self.__base_mayor}, Base menor: {self.__base_menor}, Altura: {self.__altura}"


try:
   
    trapecio = Trapecio(6, 4, 3)
    
   
    print(f"Dimensiones iniciales: {trapecio.obtener_dimensiones()}")
    
    
    print(f"Área del trapecio: {trapecio.calcular_area()} unidades cuadradas")
    
    
    print(f"Perímetro del trapecio: {trapecio.calcular_perimetro()} unidades")
    
    
    trapecio.actualizar_dimensiones(8, 5, 4)
    print(f"Dimensiones después de cambiar: {trapecio.obtener_dimensiones()}")
    
   
    trapecio.actualizar_dimensiones(-3, 5, 4)
except ValueError as e:
    print(e)
