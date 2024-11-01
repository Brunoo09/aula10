nome = input('digite seu nome:')
senha = int(input('digite uma senha:'))
print('usuario cadastrado')
print('-digite os seus dados para acessar sua conta-')
meu_nome = input('digite o nome do usuario:')
minha_senha = int(input('digite sua senha:'))

if minha_senha == senha and nome:
        print('bem-vindo', nome)
        print('saldo disponivel: R$4000')

def extrato():
    print('''
    mostra extrato:
    transação do dia 12/10
    deposito do dia 02/10
    ''')
    

def deposito():
     fazer_deposito = input('digite o valor do deposito:')
     print('deposito efetuado de R$', fazer_deposito)

def saque():
    fazer_saque = int(input('digite o valor que deseja sacar:'))
    if fazer_saque > 4000:
        print('saldo insuficiente')
    else:
        print('saque realizado com sucesso R$', fazer_saque)
        
    

def sair():
    print('saiu do sistema')
    

def banco():
    print('ESCOLHA O QUE DESEJA:')
    escolha = input('extrato, deposito, saque, sair:')
    if escolha == 'extrato':
        extrato()
    elif escolha == 'deposito':
        deposito() 
    elif escolha == 'saque':
        saque()       
    elif escolha == 'sair':
        sair()
    else:
        print('digite algo valido')
banco()

loop = True

while True:
    escolha = input('deseja continuar? s/n: ')

    if escolha == 's':
        banco()
    else:
        print('saiu do sistema')
        break
else:
    print('saiu')
            

    

        


    








       

       