class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    @property
    def nombre(self) -> str:
        """nombre getter"""
        return self._nombre
    
    @nombre.setter
    def nombre(self, new_nombre: str) -> None:
        """nombre setter
        -------------
            new_nombre: str
                str no vacia
        """
        if type(new_nombre) != str:
            raise Exception('El nombre del producto debe ser un string.')
        if not new_nombre.strip():
            raise Exception('El nombre no puede estar vacío.')
        self._nombre = new_nombre
    
    @property
    def precio(self) -> float:
        """precio getter"""
        return self._precio

    @precio.setter
    def precio(self, new_precio: float) -> None:
        """precio setter
        -------------
            new_precio: float or int
                flotante o entero positivo no nulo
        """
        try:
            new_precio = float(new_precio)
        except ValueError:
            print('El precio del producto debe ser un número')
            exit(-1)
        if new_precio <= 0:
            raise Exception('El precio no puede ser un número negativo')

        self._precio = new_precio
    
    @property
    def cantidad(self) -> float:
        """getter cantidad"""
        return self._cantidad

    @cantidad.setter
    def cantidad(self, new_cantidad: int) -> None:
        """cantidad setter
        -------------
            new_cantidad: int
                entero positivo no nulo
        """
        try:
            new_cantidad = int(new_cantidad)
        except ValueError:
            print('La cantidad debe ser un número')
            exit(-1)
        if new_cantidad < 0:
            raise Exception('La cantidad del producto no puede ser negativa')
        self._cantidad = new_cantidad

    def aplicar_descuento(self, descuento : float) -> None:
        """aplica un descuento sobre el precio del producto dado el valor porcentual"""
        try:
            descuento = float(descuento)
        except ValueError:
            print('El descuento a aplicar debe ser un número')
            exit(-1)
        if (descuento <= 0):
            raise Exception('No se puede aplicar un descuento negativo')
        
        self.precio -= self.precio * descuento / 100

    def __str__(self):
        return f'Producto: {self.nombre} - ${self.precio} - Cantidad: {self.cantidad}'