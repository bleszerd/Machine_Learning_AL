import pandas as pd
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('../csv/buscas.csv')

y_df = df['comprou']
X_df = df[['home', 'busca', 'logado']]

Xdummies_df = pd.get_dummies(X_df)
ydummies_df = y_df

X = Xdummies_df.values
y = ydummies_df.values

porcentagem_treino = 0.9

tamanho_treino = int(porcentagem_treino * len(X))
tamanho_teste = len(X) - tamanho_treino

X_treino = X[:tamanho_treino]
y_treino = y[:tamanho_treino]

X_teste = X[-tamanho_teste:]
y_teste = y[-tamanho_teste:]

model = MultinomialNB()
model.fit(X_treino, y_treino)

result = model.predict(X_teste)
diff = result - y_teste

acertos = [d for d in diff if d == 0]
total_acertos = len(acertos)
total_elements = len(X_teste)
taxa_acerto = 100.0 * total_acertos / total_elements

print(taxa_acerto)
print(total_elements)
