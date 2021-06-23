class Producto:
    def __init__(self, nombreProducto ="producto", precio = 0, categoria = "categoria"):
        self.nombreProducto = nombreProducto
        self.precio = precio
        self.categoria = categoria

    def update_price(self, percent_change, is_increased = True ) :
        if is_increased is True:
            self.precio += round(self.precio * percent_change)
        elif is_increased is False:
            self.precio -= round(self.precio * percent_change)
        
    
    def print_info (self) :
        print(f" el nombre del producto es {self.nombreProducto}, su categoria es {self.categoria} y su precio es {self.precio}")
        return self