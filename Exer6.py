nome = input("Digite um nome(somente uma palavra!)\n:")
case = input("Você gosta dessa nome?\n:")

if(case == "Sim")or(case == "sim"):
    print("Ok obrigado, volte sempre!")

elif(case == "Não")or(case == "não"):
   outronome = input("Então digite outro nome: ")
   print("Ok obrigado, volte sempre!")

else:
    print("Erro, não entendi o que você digitou, verifique os acentos...")