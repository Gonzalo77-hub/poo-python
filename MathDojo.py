


class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for numeros in nums:
            self.result += numeros
        return self
            
    def subtract(self, num, *nums):
        self.result -= num
        for numeros in nums:
            self.result -= numeros
        return self
    def desviacionE(self, *nums):
        suma = 0
        cuadradomedia = 0
        desviacion = 0
        media = 0
        for x in nums:
            suma += x
        media = suma/(len(nums))
        for x in nums:
            cuadradomedia += (x-(media))**2
        sumatoria = cuadradomedia/len(nums)
        desviacion = (sumatoria ** (0.5))
        return f"la desviacion estandar del conjunto de numeros es {desviacion}"
        




md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(f"el resultado es {x}")
# corre cada uno de los metodos algunos mas veces y valida el resultado!
w = md.add(3).add(5,5,2).subtract(5).result
print(f"el resultado es {w}")
z = md.desviacionE(6,2,3,1)
print(z)
