'''Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para
 o local.'''

class Rectangle():
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB
    
    #seters
    def set_sideA(self, a):
        self.sideA = a
    
    def set_sideB(self, b):
        self.sideB = b

    #geters
    def get_sidesValues(self):
        return self.set_sideA, self.set_sideB
    
    def get_area(self):
        return self.sideA * self.sideB

    def get_perimeter(self):
        return (self.sideA + self.sideB) * 2  

sideSizeA = int(input('Informe o tamanho do lado a (em metros): '))
sideSizeB = int(input('Informe o tamanho do lado b (em metros): '))

rectangle = Rectangle(sideSizeA, sideSizeB)

print(f'Quantidade de pisos necessários: {rectangle.get_area()}')
print(f'Quantidade de rodapés - em metros: {rectangle.get_perimeter()}m')