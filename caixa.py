from classes import Cliente, Conta

#funções do caixa eletronico

class CaixaEletronico():
  def __init__(self):
    nome = input('Qual o seu Nome ?')
    cpf = input('Digite seu cpf: ')
    cliente = Cliente(nome, cpf)
    self.conta = Conta(cliente)

    print(f"Olá {self.conta.titular.nome}, sua conta é: {self.conta.numero}")


  def exibir_menu(self):

    print("1- Consultar saldo\n 2- Depositar\n 3- Sacar")
  
    opcao = input('Digite uma opção: ')

    if opcao == '1':
      valor = self.conta.consultar_saldo()
      print (f'Seu saldo é de {valor}')

    elif opcao == '2':
      valor = float(input('Valor do deposito: '))
      self.conta.deposito(valor)
      print(f'Depósito efetuado de {valor}')

    elif opcao == '3':
      valor = float(input('Valor do saque: '))

      if self.conta.sacar(valor):
        print('saque efetuado')

      else:
        print('não tem saldo')

    # else:
    #   print('Opção invalida')



