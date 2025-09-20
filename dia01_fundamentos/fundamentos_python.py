# 🚀 Dia 1 – Fundamentos do Python
# 1. Conceitos-chave de hoje
# Variáveis → guardam informações na memória.
# Tipos básicos → int (número inteiro), float (número decimal), str (texto), bool (verdadeiro/falso).
# Print → exibe informações na tela.
# Input → recebe dados do usuário.
# If/Else → toma decisões.
# Operadores lógicos → ==, !=, >, <, >=, <=, and, or.

# Exemplos : 
# Variáveis 

nome = "Beto"
idade = 31
altura = 1.79
estudando_python = True 

print(
    "Nome:", nome , 
    "Idade:", idade, 
    "Altura:", altura, 
    "Estudando Python:", estudando_python)

# input do usuário
usuario = input("Qual seu nome? ")
print("Seja Bem Vindo,", usuario)

# Condições 
idade = int(input("Digite sua idade: "))

if idade >= 18: 
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.") 
    
# Operadores lógicos
nota = float(input("Digite sua nota final: "))

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação!")
else:
    print("Reprovado!")