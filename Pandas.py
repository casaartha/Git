import pandas as pd

# Nome do arquivo CSV
nome_arquivo = 'C:/Python/Estudo/Input/TABELA_PARCELAS_25Jan2024.csv'

# Usar a função read_csv para ler o arquivo CSV e criar um DataFrame
df = pd.read_csv(nome_arquivo)

# Imprimir o DataFrame
print(df)