#1. Cadastro de filmes

filmes = ["Zootopia", "Barbie", "Waves", "Batman", "Fuga das Galinhas"]
print("Lista de 5 filmes: ",filmes)

print("Primeiro filme da lista: ",filmes[0])

print("Último filme da lista: ",filmes[-1])

filmes.append("Star Wars")
print(filmes)

filmes.insert(1, "Cleopatra")
print(filmes)

filmes.remove("Waves")
print(filmes)

print("Quantidade de elementos: ",len(filmes))

if "Fuga das Galinhas" in filmes:
    print("Fuga das Galinhas está na lista.")
else:
    print("Fuga das Galinhas não está na lista.")

print("\n\n")
#2. Controle de notas

notas = [7.5, 8.0, 8.5, 9.0, 10.0]
print("Lista de notas: ", notas)

soma = 0

for nota in notas:
    soma = soma + nota
print("A soma das notas é de: ",soma)

media = soma / len(notas)
print(f"A média das notas é de: {media}")

maior_nota = notas[0]
for nota in notas:
    if nota > maior_nota:
        maior_nota = nota
print(f"A maior nota encontrada foi: {maior_nota}")

menor_nota = notas[0]
for nota in notas:
    if nota < menor_nota:
        menor_nota = nota
print(f"A menor nota encontrada foi: {menor_nota}")

if "10.0" in notas:
    print("Existe uma nota igual a 10.")
else:
    print("Não existe uma nota igual a 10.")

if media >= 7.0:
    print("O estudante foi aprovado.")
else:
    print("O estudante não foi .")

print("\n\n")


#3. Informações de um produto

produto = {
    "nome": "Iphone 16",
    "categoria": "Celular",
    "preço": 6.999,
    "código do produto": 1234
}
print(produto)

print(produto["nome"])
print(produto["categoria"])
print(produto["preço"])
print(produto["código do produto"])

print("A quantidade de informações armazenadas:",len(produto))

produto["preço"] = 6.899
print(produto)


