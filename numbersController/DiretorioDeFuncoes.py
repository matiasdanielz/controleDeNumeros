class validacaoDeNumeros:

    def VerificaSenumeroEPar(self):
        numeroEscolhido = int(input('Escolha um numero: '))
        resultado = numeroEscolhido % 2

        if resultado == 1:
            print("numero é impar")
        else:
            print('numero é par')


    def RetornarSomaDeValores(self):
        Primeironumero = int(input('Digite um numero: '))
        SegundoNumero = int(input('Digite o segundo numero: '))
        soma = Primeironumero + SegundoNumero
        print(f'A soma dos valores e: {soma}')

