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