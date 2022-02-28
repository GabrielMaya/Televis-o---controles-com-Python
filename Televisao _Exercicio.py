class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        self.canal += 1

    def diminui_canal(self):
        self.canal -= 1


televisao = Televisao()
print('A televisão está ligada? {} ' .format(televisao.ligada))

if not televisao.ligada:
    a = input('Televisão desligada! Deseja ligar?')
    if a == 'sim':
        televisao.power()
        print('ligando...')
    else:
        print('Televisão continua desligada!')

else:
    b = input('Televisao ligada! Deseja desligar?')
    if b == 'sim':
        televisao.power()
    else:
        print('Televisão continua ligada!')


if televisao.ligada is True:
    print('A televisão está no canal: {}' .format(televisao.canal))
    c = input('Deseja mudar de canal? ')
    while c == 'sim':
        if c == 'sim':
            d = input('Tecle "+" para aumentar o canal e "-" para diminuir o canal: ')
            if d == "+":
                televisao.aumenta_canal()
                print('Canal {}' .format(televisao.canal))
            else:
                televisao.diminui_canal()
            c = input('Deseja mudar de canal? ')
            print('Canal {}' .format(televisao.canal))

    print('Você está assistindo o canal: {}' .format(televisao.canal))
