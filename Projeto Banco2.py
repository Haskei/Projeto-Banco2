global saldo
saldo = float(0)
extrato=[]
i=0
nun_saque = int(0)
saque_limite = int(3)
def saque_check(nun_saque):
    if nun_saque < saque_limite:
        return True
    else:
        return False
def saque(saldo):
    if nun_saque >= 3:
        print("Numero de saque diários excedidos!")
    else:
        print("Quanto dinheiro você gostaria de sacar?(Limite de R$500,00)")
        din=float(input())
        if din>saldo:
            print("Não há saldo suficiente.")
        elif din>500:
            print("Limite de saque excedido.")
        else:
            din = -din
            saldo = saldo + din
            format(din, ".2f")  
            extrato.append(din)
            print("Seu saldo mudo por R$",din,". Seu saldo atual é R$:",saldo)
            return din
def deposito(saldo):
    print("Quanto dinheiro você ira depósitar?")
    depo=float(input())
    format(depo, ".2f")
    extrato.append(depo)
    saldo = saldo + depo
    print("Foram adicionados R$",depo," a sua conta.")
    print("Seu saldo agora é R$",saldo)
    return depo
def extratoV():
    if len(extrato)>0:
        for j in extrato:
            print("R$",extrato[j])
            j= j+1
    else:
        print("Não foram realizadas movimentações.")
while i != 1:
    print("""
          Aperte S e enter parra fazer Saque
          Aperte D e enter para fazer um deposito
          Aperte E e enter para ver o extrato
          aperte T e enterpara Terminar o programa
          Favor utilize letras maiusculas para a navegação deste menu""")
    menu=input()
    if menu=="S":
        if saque_check(nun_saque) is True:
            mon = saque(saldo)
            if mon is float:
                saldo = saldo + mon
                nun_saque = nun_saque + 1
        else:
            print("Limite de saque excedidos")
    elif menu=="D":
        saldo = saldo + deposito(saldo)
    elif menu=="E":
        extratoV()
    elif menu=="T":
        print("Muito Obrigado, Volte sempre")
        i=1
