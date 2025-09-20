# script de cadastrop simples
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
mensagem = "Olá {}, você tem {} anos e mora em {}.".format(nome, idade, cidade)
            # ou f"Olá {nome}, você tem {idade} anos e mora em {cidade}."
print(mensagem)