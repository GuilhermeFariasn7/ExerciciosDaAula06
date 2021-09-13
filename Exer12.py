temperatura = int(input("Digite a temperatura atual\n: "))
if(temperatura <= 18):
    print("Frio!")
elif(temperatura >= 21)and(temperatura <= 27):
    print("Agradável!")

elif(temperatura >= 27)and(temperatura < 41):
    print("calor!")

else:
    print("tá pegando fogo bixo!")
