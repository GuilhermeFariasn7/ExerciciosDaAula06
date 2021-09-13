num1 = int(input("Insira um número real\n: "))
num2 = int(input("Insira outro número real\n: "))
if(num1>num2):
    print(num1,"é o maior deles!")
elif(num2>num1):
    print(num2,"é o maior número")
elif(num1 == num2):
    print(num1,"é igual a ",num2) 
else:
    print("ERRO... não faço a minima ideia do erro")

