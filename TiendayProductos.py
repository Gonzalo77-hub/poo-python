class Tienda:
    def __init__(self, nombre="tienda"):
        self.nombre = nombre
        self.listaProductos = []
    def __str__(self):
        atributos = "la tienda es: {}".format(self.nombre)
        return atributos
    def add_product (self, new_product) :
        self.listaProductos.append(new_product)
        return self
    def sell_product (self, id):
        x =self.listaProductos.pop(id)
        return print(f"el producto vendido fue {x.nombreProducto}")

        
        
    def inflation(self, percent_increase):
        for n in self.listaProductos:
            n.update_price(percent_increase/100)
    def set_clearance (self, category, percent_discount) :
        for x in self.listaProductos:
            if x.categoria == category:
                x.update_price(percent_discount/100, False)
    def mostrarlistaproductos(self):
        for n in self.listaProductos:
            n.print_info()

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

producto1 = Producto("Tomate", 100, "Verdura" )
producto2 = Producto("Brocoli", 120, "Verdura")
producto3 = Producto("Manzana", 80, "Fruta")
producto4 = Producto("Naranja", 90, "Fruta")
producto5 = Producto("Cerveza", 200, "Liquidos")


tienda1 = Tienda("dondejuanita")
tienda1.add_product(producto1).add_product(producto2).add_product(producto3).add_product(producto4).add_product(producto5)
""" tienda1.mostrarlistaproductos() """
""" tienda1.inflation(10) """
tienda1.mostrarlistaproductos()
tienda1.set_clearance("Verdura", 10)
""" tienda1.mostrarlistaproductos() """

tienda1.sell_product(2)
tienda1.mostrarlistaproductos()
print(tienda1)
