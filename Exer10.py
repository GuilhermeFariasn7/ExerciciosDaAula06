num1 = int(input("Insira um número real\n: "))
num2 = int(input("Insira outro número real\n: "))

escolha = int(input("que tipo de conta você quer fazer?\n1 - soma\n2 - subtração\n:"))
if(escolha == 1):
    print("O resultado da soma deu: ",(num1+num2))
elif(escolha == 2):
    print("O resultado da subtração deu: ",(num1-num2))
else:
    print("Erro...")
