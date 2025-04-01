time1= (input("Digite o nome do time :"))
gols1= int(input("Digite o numero de gols do time1:"))
time2= (input("Digite o nome do time2 :"))
gols2= int(input("Digite o numero de gols do time2:"))

if gols1 > gols2:
    print(f"O time vencedor é o {time1} com um total de {gols1} gols")
else:
    if gols2 == gols1:
        print("Os times empataram")
    else:
        print(f"O time vencedor é o {time2} com um total de {gols2} gols")
