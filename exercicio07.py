
Tipo= input("Digite qual tipo de combustivel\n"
            "g para Gasolina \n"
            "E para Etanol")
quantidade= float(input("Digite quantos litros você abasteceu:"))

vGas= 5.8
vEtal= 4.9
if Tipo == "g":
    valor= vGas*quantidade
else:
    valor= vEtal*quantidade
print(f" Você gastou um total de R${valor}")
