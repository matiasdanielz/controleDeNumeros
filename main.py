from numbersController import DiretorioDeFuncoes

if __name__ == '__main__':

    controleDeNumeros = DiretorioDeFuncoes.validacaoDeNumeros()

    opcao = int(input('Escolha uma opcao: '))

    if(opcao == 1):
        controleDeNumeros.RetornarSomaDeValores()
    else:
        controleDeNumeros.VerificaSenumeroEPar()