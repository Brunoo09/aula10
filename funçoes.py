def soma():
    n1 = int(input('digite um numero'))
    n2 = int(input('digite um numero'))
    soma = n1 + n2
    print(soma)
soma()

def subtracao():
    n1 = int(input('digite um numero'))
    n2 = int(input('digite um numero'))
    subtracao = n1 - n2
    print(subtracao)
subtracao()

def multiplicacao():
    n1 = int(input('digite um numero'))
    n2 = int(input('digite um numero'))
    multiplicacao = n1 * n2
    print(multiplicacao)
multiplicacao()

def divisao():
    n1 = int(input('digite um numero'))
    n2 = int(input('digite um numero'))
    divisao = n1 / n2
    print(divisao)
divisao()

def calculadora():
    operacao = input('+ - * /')
    if operacao == '+':
        soma()
    elif operacao == '-':
        subtracao()
    elif operacao == '*':
        multiplicacao()
    elif operacao == '/':
        divisao()    
    else:
        print('digite algo valido')
calculadora()    

loop = True

while True:
    escolha = input('deseja continuar? s/n')

    if escolha == 's':
        calculadora()
    else:
        print('saiu do sistema')
        break
else:
    print('saiu')
            