from Capitulo3_Funcoes.IdentificadorDeFuncoes import *

minhaLista=[]
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista)

print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumoDosValores(minhaLista)