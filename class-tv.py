"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class Tv:
    def __init__(self, channel=1, volume=10):
        self.channel = channel 
        self.volume = volume 
        self.__number_of_channels = list(range(1, 25))
        self.__volume_range = list(range(0, 100))

    def set_channel(self, channel):
        if channel in self.__number_of_channels:
            self.channel = channel 
        else:
            print("Channel out of range")
    
    def set_volume(self, volume):
        if volume in self.__volume_range:
            self.volume = volume
        if volume >= 100:
            print("Maximum volume reached")
        if volume <= 0:
            print("Mute")

#tests

lg = Tv()

print(f"Channel: {lg.channel}\nVolume: {lg.volume}")

lg.set_channel(18)
lg.set_volume(58)

print(f"Channel: {lg.channel}\nVolume: {lg.volume}")

lg.set_channel(34)
lg.set_volume(130)
lg.set_volume(0)
