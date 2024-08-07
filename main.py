#pega todas as variaveis e junta tudo em uma string dentro de outra variavel
carros = ['gol', 'fusca', 'variante', 'opala', 'brasilia', 'uno']

#define o separador
traco_traco = ' -- '

#variavel que armazena todos os itens da lista em uma string
lista_carro = traco_traco.join(carros)

print(lista_carro)

#resultado no prompt
#gol -- fusca -- variante -- opala -- brasilia -- uno