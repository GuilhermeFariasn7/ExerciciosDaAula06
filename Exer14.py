altura = float(input("Informe sua altura\n: "))
sexo = input("Digite seu sexo(M ou F)\n:")
if(sexo == "M") or (sexo=="m"):
    PesoIdeal = ((72.7*altura)-58)
    print("Seu peso ideal será: {:.1f}".format(PesoIdeal))
elif(sexo == "F") or (sexo=="f"):
    PesoIdeal = ((62.1*altura)-44.7)
    print("Seu peso ideal será: {:.1f}".format(PesoIdeal))
else:
    print("Algo deu errado, tente novamente!")
