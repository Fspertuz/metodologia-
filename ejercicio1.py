class Articulo:
    def __init__(self, descripcion, costo):
        self.__descripcion = descripcion  # Atributo privado
        if costo <= 0:
            raise ValueError("El costo debe ser mayor que cero.")
        self.__costo = costo  # Atributo privado
    
    # Método para actualizar el costo del artículo
    def actualizar_costo(self, nuevo_costo):
        if nuevo_costo <= 0:
            raise ValueError("El nuevo costo debe ser mayor que cero.")
        self.__costo = nuevo_costo
    
    # Método para obtener el costo actual
    def obtener_costo(self):
        return self.__costo
    
    # Método para obtener la descripción del artículo
    def obtener_descripcion(self):
        return self.__descripcion
    
    # Método para aplicar un descuento sobre el costo
    def aplicar_oferta(self, porcentaje_oferta):
        if porcentaje_oferta < 0 or porcentaje_oferta > 100:
            raise ValueError("El porcentaje de la oferta debe estar entre 0 y 100.")
        descuento = (self.__costo * porcentaje_oferta) / 100
        self.__costo -= descuento
    
# Ejemplo
try:
    # Crear un artículo con descripción y costo
    articulo = Articulo("Pantalón", 40)
    
    # Consultar la descripción y el costo
    print(f"Artículo: {articulo.obtener_descripcion()}")
    print(f"Costo inicial: ${articulo.obtener_costo():.2f}")
    
    # Actualizar el costo del artículo
    articulo.actualizar_costo(50)
    print(f"Nuevo costo: ${articulo.obtener_costo():.2f}")
    
    # Aplicar una oferta del 15%
    articulo.aplicar_oferta(15)
    print(f"Costo después de la oferta: ${articulo.obtener_costo():.2f}")
    
    # Intentar actualizar el costo a un valor no válido (negativo)
    articulo.actualizar_costo(-10)
except ValueError as e:
    print(e)
