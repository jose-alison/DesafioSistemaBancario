def Menu():
  print("""
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [X] Sair
    """)

def Deposito():
  global saldo
  valorDeposito = float(input('Informe o valor do depósito: '))
  if valorDeposito > 0:
    saldo += valorDeposito
    extrato.append(['Depósito', f'+ R$ {valorDeposito:.2f}'])
  else:
    print('Operação inválida, informe um valor válido.')

def Saque():
  global saldo, saquesRealizados
  if saquesRealizados < 3:
    valorSaque = float(input('Informe o valor do saque: '))
    if valorSaque <= saldo:
      if valorSaque > 500:
        print('Você deve informar um valor abaixo de R$ 500')
      else:
        saldo -= valorSaque
        extrato.append(['Saque', f'- R$ {valorSaque:.2f}'])
        saquesRealizados += 1
    
    else:
      print('Você não possui saldo disponível')
  
  else:
      print('Você já realizou a quantidade máxima de saques disponíveis')

def Extrato():
  print('\n ================== EXTRATO ==================')
  for i in range(len(extrato)):
    print(extrato[i][0], '.......................', extrato[i][1])
  print('---------------------------------------------')
  print(f'Saldo atual ....................... R$ {saldo:.2f}')
  print('---------------------------------------------')
  print('=============================================')

saldo = 0.00
limiteSaque = 500
qtdMaxSaque = 3
saquesRealizados = 0
extrato = [['Saldo Inicial', f'R$ {saldo:.2f}']]

while True:
  Menu()
  escolha = input().upper()
  if escolha == 'D':
    Deposito()
  elif escolha == 'S':
    Saque()
  elif escolha == 'E':
    Extrato()
  elif escolha == 'X':
    break
  else:
    print('Operação inválida, escolha uma operação.')
