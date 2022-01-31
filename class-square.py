class Square:
    def __init__(self, sideSize):
        self.sideSize = sideSize

    def set_sideSize(self, size):
        self.sideSize = size

    def get_sideSize(self):
        area = (self.sideSize * self.sideSize)
        return self.sideSize, area

testSquare = Square(15)

print(f'Square side size: {testSquare.get_sideSize()[0]}cm')
print(f'Square area: {testSquare.get_sideSize()[1]}cm2')

testSquare.set_sideSize(17)

print(f'New Square side size: {testSquare.get_sideSize()[0]}cm')
print(f'New Square area: {testSquare.get_sideSize()[1]}cm2')


