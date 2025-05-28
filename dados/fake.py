from faker import Faker
import pandas as pd
import random

fake = Faker()

#Lista de produtos da padaria
produtos = ["Pao Frances", "Bolo de Chocolate", "Torta de Morango", "Pao de Queijo"]

#Lista de clientes
clientes = []

for i in range(50):
	cliente = {
		"Nome": fake.name(),
		"Idade": random.randint(18, 80),
		"Produto_Preferido": random.choice(produtos),
		"Frequência_Compra": random.randint(1, 7), #Vezes por semana
		"Gasto_Médio": round(random.uniform(5.0, 50.0), 2)
	}
	clientes.append(cliente)

df = pd.DataFrame(clientes)
df.to_csv("clientes_padaria.csv", index=False)
print('Arquivo gerado com sucesso.')

