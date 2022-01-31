class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor 
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, cor):
        self.cor = cor
    
    def mostraCor(self):
        return self.cor

#atribui os valores para a classe vazia 
bola = Bola('vermelho', 10, 'borracha')

#printa os valores iniciais
print(f'cor = {bola.mostraCor()} \ncircunferencia = {bola.circunferencia} \nmaterial = {bola.material}')

#usa o método de trocar de cor 
bola.trocaCor('azul')

#mostra a nova cor
print(f'nova cor: {bola.mostraCor()}')

