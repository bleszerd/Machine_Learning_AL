from sklearn.naive_bayes import MultinomialNB

# Classificação de Animais
# Porco: 1
# Cachorro: -1

# [Gordinho?] [Perna curta?] [Faz au au?]
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [
    porco1,
    porco2,
    porco3,
    cachorro1,
    cachorro2,
    cachorro3
]

marcacoes = [1, 1, 1, -1, -1, -1]  # Resultados conhecidos

misterioso1 = [1, 1, 1]  # Desconhecido 1
misterioso2 = [1, 0, 0]  # Desconhecido 2
misterioso3 = [0, 0, 1]  # Desconhecido 2

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

testes = [misterioso1, misterioso2, misterioso3]

resultado_teste = [-1, 1, -1]

resultado_predicao = modelo.predict(testes)

diferencas = resultado_predicao - resultado_teste

acertos = [d for d in diferencas if d == 0]
total_acertos = len(acertos)
total_elementos = len(testes)

taxa_acerto = 100.0 * total_acertos / total_elementos

print(taxa_acerto)