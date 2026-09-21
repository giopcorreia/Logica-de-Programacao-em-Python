#Listas, Tuplas e Dicionários

#1. Listas
#Utilizadas para armazenar vários valores dentro de uma única variável.
nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes)


#2. Acessando Elementos da Lista
print(nomes[0])
#Podemos acessar o último elemento usando o -1.
print(nomes[-1])


#3.Alterando Elementos
nomes[0] = "Pedro"
print(nomes)


#4. Adicionar Elementos
#append() adiciona um elemento no final da lista
nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma posição específica.
nomes.insert(1, "Mariana")
print(nomes)


#5.Removendo Elementos
#remove um elemento pelo valor
nomes.remove("Lucas")
print(nomes)

#pop() remove um elemento pelo índice
nomes.pop(0)
print(nomes)


#6. Tamanho da Lista
#len() informa a quantidade de elementos
print(len(nomes))


#7. Percorrendo uma Lista
for nome in nomes:
    print(nome)


#8. Verificando se um elemento existe

if "João" in nomes:
    print("João está na lista.")
else:
    print("João não está na lista.")



#9. Lista com diferentes tipos de dados
dados = ["João", 18, 1.75, True]
print(dados)

#10. lista de números
notas = [7.5, 8.0, 8.5, 9.0]
soma = 0

for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(f"Média: {media}")


#11. Tuplas
#tuplas são semelhantes as listas. As tuplas não podem ser alteradas.

coordenadas = (10, 20)
print(coordenadas)

print(coordenadas[0])


#12. Dicionários
#Dicionários armazenam informações no formato: chave: valor
aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}
print(aluno)