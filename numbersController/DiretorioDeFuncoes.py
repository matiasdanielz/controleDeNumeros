class validacaoDeNumeros:

    def VerificaSeNumeroEPar(self):
        numeroEscolhido = int(input('Escolha um numero: '))
        resultado = numeroEscolhido % 2

        if resultado == 1:
            print("numero é impar")
        else:
            print('numero é par')


    def SomarValores(self):

        Primeironumero = int(input('Digite um numero: '))
        SegundoNumero = int(input('Digite o segundo numero: '))

        soma = Primeironumero + SegundoNumero
        print(f'A soma dos valores e: {soma}')

    def BuscaDeMenorNumeroEmArray(self):
        listaDeNumeros = []

        for i in range(4):
            numero = int(input(f'Digite o {i + 1}º numero: '))
            listaDeNumeros.append(numero)
        listaDeNumeros.sort()
        print(listaDeNumeros[0])