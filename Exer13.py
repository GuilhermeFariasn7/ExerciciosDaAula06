temp = int(input("Para que temperatura você quer que converta?\n1 - Fahrenheit para Celsius\n2 - Celsius para Fahrenheit.\n:"))

if(temp == 1):
    fahrenheit = float(input("Digite a temperatura em Fahrenheit\n:"))
    conversão1 = ((fahrenheit-32)/1.8)
    print("Conversão deu: {}".format(conversão1))
elif(temp == 2):
    celsius = float(input("Digite a temperatura em Celsius\n:"))
    conversão2 = ((celsius*1.8)+32)
    print("Conversão deu: {:.2f}".format(conversão2))

else:
    print("Digitação invalida...")