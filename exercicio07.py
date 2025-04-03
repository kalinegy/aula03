Tipo= input("Digite qual tipo de combustivel\n"
            "G para Gasolina \n"
            "E para Etanol")
quantidade= float(input("Digite quantos litros você abasteceu:"))

vGas= 5.8
vEtal= 4.9
valor= 0
if Tipo == "g" or Tipo == "G":
    valor= vGas*quantidade
else:
    if Tipo == "e" or Tipo== "E":
        valor= vEtal*quantidade
    else:
        print(f"Opção inválida")

print(f"Você gastou R$ {valor}")
