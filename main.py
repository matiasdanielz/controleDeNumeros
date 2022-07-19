class validacaoDeNumeros:
    def __init__(self, _num):
        self.numero = int(_num)

    def numeroPar(self):
        numero_escolhido = self.numero
        resultado = numero_escolhido % 2

        if resultado == 1:
            print("numero é impar")
        else:
            print('numero é par')


if __name__ == '__main__':
    numeroEscolhidoPorUsuario = str(input('Digite um numero: '))
    numeroAValidar = validacaoDeNumeros(numeroEscolhidoPorUsuario)
    numeroAValidar.numeroPar()