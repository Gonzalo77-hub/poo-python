import tienda as ti
import producto as pr

producto1 = pr.Producto("Tomate", 100, "Verdura" )
producto2 = pr.Producto("Brocoli", 120, "Verdura")
producto3 = pr.Producto("Manzana", 80, "Fruta")
producto4 = pr.Producto("Naranja", 90, "Fruta")
producto5 = pr.Producto("Cerveza", 200, "Liquidos")


tienda1 = ti.Tienda("dondejuanita")
tienda1.add_product(producto1).add_product(producto2).add_product(producto3).add_product(producto4).add_product(producto5)
""" tienda1.mostrarlistaproductos() """
""" tienda1.inflation(10) """
tienda1.mostrarlistaproductos()
tienda1.set_clearance("Verdura", 10)
""" tienda1.mostrarlistaproductos() """

tienda1.sell_product(2)
tienda1.mostrarlistaproductos()
print(tienda1)