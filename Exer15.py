nota1 = float(input("Digite a primeira nota(a de peso 5 que você fez)\n: "))
nota2 = float(input("Digite a segunda nota(a de peso 5 que você fez)\n: "))
nota3 = float(input("Digite a terceira nota\n: "))

media = ((nota1+nota2+nota3)/2)

if(media>=6):
    print("Aluno aprovado com média: {:.1f}".format(media))