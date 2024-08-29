dicionario = {
"A": "Abacate",
 "B": "Bola",
 "C": "Cachorro"
}
# importante entender: 
# dicionario = {'A': 'Abacate', 'B': 'Bola', 'C': 'Cachorro'}
# pra cada item do dicionario, temos uma chave e um valor
# chave = A, valor = Abacate, então estamos atribuindo estes valores a chave e valor
# é o mesmo caso de atribuição multipla de items de uma tupla, o desempacotamento: 
# tupla = (1, 2, 3)
# a, b, c = tupla ou
# a, b, c = (1, 2, 3)
for chave, valor in dicionario.items(): #poderia usar a função .items()
    print(chave, valor) # ex:for chave, valor in zip(dicionario.keys(), dicionario.values()):