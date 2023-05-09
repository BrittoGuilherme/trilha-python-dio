def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")


def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    return a / b

def multiplcacao(a, b):
    return a * b

def exibir_funcao(a, b, funcao):
    resultado = funcao(a, b)
    print (f"O resultado da operação é = {resultado}")
    
exibir_funcao(10, 5, soma)
exibir_funcao(10, 5, subtracao)
exibir_funcao(10, 5, divisao)
exibir_funcao(10, 5, multiplcacao)