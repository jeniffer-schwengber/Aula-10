# for numero in range (1, 10, 2):
# #     print(numero)
# palavra = "Determinado"
# for i in palavra:
#     print(i)

# nomes = ["Ana", "João", "Maria", "Pedro", "José"]
# for nome in nomes:
#     print(nome)


"""
FUNÇÕES NO PYTHON

- REUTILIZAR TRECHOS DE CÓDIGO
"""
#
# # Código sem uso de função
# base = 2
# expoente = 3
# potencia = base ** expoente
# print(potencia)


# def potencia(base, expoente):
#     return base ** expoente
#
#
# print(potencia(3,5))
# print(potencia(4,8))

#CALCULADORA

# def operacoes_basicas(x, y):
#     soma = x + y
#     subtracao = x - y
#     multiplicacao = x * y
#     divisao = x / y
#     return soma, subtracao, multiplicacao, divisao
# print(operacoes_basicas(10, 2 ))

# Crie uma função que simplismente imprima como resultado um nome, uma idade e Cidade qualquer.
#
# def formulario(nome , idade, cidade ):
#     return print(nome, idade, cidade)
#
#
# formulario("Jeniffer", 32 , "Curitiba")

"""
1) Criar uma função que imprima a seguinte frase "Olá, Mundo!"
2) Criar uma função que calcule a area do retangulo 
3) Criar uma função que imprima o dobro e o triplo de um numero 
4) Criar uma função para checar se o numero é par.
5) Criar uma função para converter Celsios e F 

"""
#1
# def informação(frase):
#     return print(frase)
#
# informação("Olá, Mundo!")
#2
#
# def area_retangulo(base, altura):
#     return base * altura
#
# print(area_retangulo(5, 3))
#3
# def dobro_triplo(numero):
#     return numero * 2, numero * 3
#
# print(dobro_triplo(5))
#4
# def par_impar(numero):
#     if numero % 2 == 0:
#         print("numero par")
#     else:
#         print("Numero impar")
#printe par_impar(20)

#5
#
# def convercao(temperatura):
#     return temperatura*9/5 + 32
# print(convercao(10))


