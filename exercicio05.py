nota1= float(input("Digite a primeira nota:"))
nota2= float(input("Digite a segunda nota:"))
nota3= float(input("Digitr a terceira nota:"))
media= (nota1+nota2+nota3)/3


if media >= 7:
    print(f"Aluno aprovado {media}")
else:
    if media < 4:
        print(f"Aluno recuperacao {media}")
    else:
        print(f"Aluno em recuperacao {media}")