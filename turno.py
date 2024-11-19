turno = input("Digite M, V ou N de acordo com o turno que você estuda: ")

if (turno == 'M' or turno == 'm'):
    print("Bom dia!")
elif (turno == 'v' or turno == 'V'):
    print("Boa tarde!")
elif (turno == 'n' or turno == 'N'):
    print("Boa noite!")
else:
    print("Valor invalido")