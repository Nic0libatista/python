def somalista(valores =[]):
    """
    A função somalista, recebe  uma lista de números e faz a soma
    de todos os números e retorna o resultado da soma

    parameters
    -----------------------------------
    valores: int[]
        lista de números para a soma 

    returns
    -----------------------------------
    retorna a soma de uma lista
    """
    resultado = 0
    for i in valores:
        resultado+=i

    return resultado


def maiorvalor(lista =[]):
    """"
    A função maiorvalor encontra o maior valor em uma lista númerica

    parameters
    -----------------------------------
        lista: int[]
    
    returns
    -----------------------------------
    retorna o maior valor na lista
    
    """

    m = lista[0]
    for i in lista:
        if i > m:
            m = i

    return m 

def inverter(palavra=""):
    #Vamos utilizar o comando len (length-comprimento) para obter
    #a quantidade de caracteres da palavra
    qtd = len(palavra)
    invertida =""
    for i in range(qtd -1,-1,-1):
        invertida+=palavra[i]
    return invertida

def palindromo(palavra=""):
    org = inverter(palavra).lower()
    if palavra.lower()==org:
        return "É um palindromo"
    else:
        return "Não é um palindromo"
