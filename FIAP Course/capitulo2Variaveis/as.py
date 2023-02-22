nome =input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
doencaContagiosa = input("Suspeita de doença contagiosa? g").upper()

# Suspeita de doença contagiosa
if doencaContagiosa=="SIM":
    print("Encaminhe o paciente para a sala branca")
elif doencaContagiosa=="NAO":
    print("Encaminhe o paciente para a sala amarela")
else:
    print("Responda o questionário com SIM ou NAO")

# Prioridade por idade ou gestante
if idade >= 65:
    print("Paciente com prioridade")
else:
    genero =input("Digite o gênero do paciente")
    if genero=="feminino" and idade>10:
        gravidez==input("A paciente está grávida?")
        if gravidez=="SIM":
            print("paciente com prioridade")
        else:
            print("Paciente sem prioridade")
    else:
        print("Paciente sem prioridade")


