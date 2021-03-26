from sklearn.naive_bayes import MultinomialNB
from utils.data import read_csv

# Classificação de compra paginas web
# Comprou: 1
# Não comprou: 0

# home, como_funciona, contato, comprou
X, y = read_csv("acesso")

treino_X = X[:90]
treino_y = y[:90]

teste_X = X[-9:]
teste_y = y[-9:]

model = MultinomialNB()
model.fit(treino_X, treino_y)

result = model.predict(teste_X)
dif = result - teste_y

acertos = [d for d in dif if d == 0]
total_acertos = len(acertos)
total_elementos = len(teste_X)
taxa_acerto = 100.0 * total_acertos / total_elementos

print(taxa_acerto)
print(total_elementos)