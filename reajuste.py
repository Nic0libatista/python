salario = int(input("Digite seu salário e descubra seu reajuste: "))

if (salario <=280):
    reajuste =float(salario * 0.20)
    valor =float (salario + reajuste)
    print(f"seu salario de R${salario} teve aumento de 20%, ou seja, de R${reajuste}. seu sálario será de R${valor}")

elif (salario <700):
    reajuste =float(salario * 0.15)
    valor =float  (salario + reajuste)
    print(f"seu salario de R${salario} teve aumento de 15%, ou seja, de R${reajuste}. seu sálario será de R${valor}")

elif (salario <1500):
    reajuste =float(salario * 0.10)
    valor =float (salario + reajuste)
    print(f"seu salario de R${salario} teve aumento de 10%, ou seja, de R${reajuste}. seu sálario será de R${valor}")

else:
    reajuste =float(salario * 0.05)
    valor =float (salario + reajuste)
    print(f"seu salario de R${salario} teve aumento de 5%, ou seja, de R${reajuste}. seu sálario será de R${valor}")
