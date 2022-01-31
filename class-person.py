'''Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano 
que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Person():
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def getOld(self, years):
        if self.age < 21:
            self.height = self.height + (0,5 * float(years))
        self.age = self.age + years

    def gainWeight(self, kilos):
        self.weight = self.weight + kilos

    def loseWeight(self, kilos):
        self.weight = self.weight - kilos

    def growUp(self, cm):
        self.height = self.height + float(cm)

#tests

#buiding a person
sandro = Person('Sandro Seidel', 18, 80, 1.83)

#Sandro in 2022
print(f'''Name: {sandro.name}\n
          Age: {sandro.age}\n
          weight: {sandro.weight}\n
          height: {sandro.height}''')
        
#Sandro in 2030 
#geting old 
sandro.getOld(8)
#gaing weight, just a little bit cuz babe ima workout machine
sandro.gainWeight(8)
#Growing up (fisically)
sandro.growUp(3)

print(f'''Name: {sandro.name}\n
          Age: {sandro.age}\n
          weight: {sandro.weight}\n
          height: {sandro.height}''')
        