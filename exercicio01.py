nome= input("Digite seu nome:")
idade= input("Digite sua idade:")
salario= float(input("Digite o valor da sua renda mensal:"))
aumento= float(input("Digite o numero correspondente ao seu aumento:"))
total= (salario*aumento)/100
print(f"O seu nome é {nome} , voce tem {idade} anos , e recebia {salario} , com o aumento de {aumento} ira receber: {salario+total}")
