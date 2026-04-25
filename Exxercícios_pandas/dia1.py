import pandas as pd

funcionarios = {
    'nome':         ['Alice', 'Bruno', 'Carla', 'Diego', 'Elena'],
    'departamento': ['TI', 'RH', 'TI', 'Financeiro', 'RH'],
    'salario':      [4500, 3200, 6800, 5400, 2900],
    'anos_empresa': [3, 7, 2, 9, 1]
}

df = pd.DataFrame(funcionarios)

# 1. Mostre as informações gerais do DataFrame (shape, tipos, estatísticas)
# 2. Filtre apenas os funcionários do departamento TI
# 3. Crie uma coluna 'salario_anual' com o salário multiplicado por 12
# 4. Qual funcionário tem o maior salário? (retorne o nome)
# 5. Filtre funcionários com mais de 3 anos de empresa E salário acima de 4000

#1
print(df.shape)
print(df.info())
print(df.describe())

#2
print(df[df['departamento'] == 'TI'])

#3
df['salario_anual'] = df['salario']*12
print(df)

#4
print(df.loc[df['salario'].idxmax(), 'nome'])

#5
print(df[(df['anos_empresa'] > 3) & (df['salario'] > 4000)])

##################################################################################################################################################################

vendas = {
    'produto':    ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset', 'Webcam'],
    'categoria':  ['Informática', 'Periférico', 'Periférico', 'Informática', 'Periférico', 'Informática'],
    'preco':      [3500, 85, 220, 1200, 350, 480],
    'quantidade': [15, 120, 80, 25, 60, 40],
    'avaliacao':  [4.8, 4.2, 3.9, 4.5, 4.1, None]  # None = dado faltante
}

df = pd.DataFrame(vendas)

# 1. Existe algum dado faltante no DataFrame? Em qual coluna?
#    Dica: pesquise df.isnull()
# 2. Substitua o dado faltante pela média das avaliações
#    Dica: pesquise df.fillna()
# 3. Crie uma coluna 'receita' (preco * quantidade)
# 4. Qual categoria tem a maior receita total?
#    Dica: pesquise df.groupby()
# 5. Ordene o DataFrame pela receita, do maior para o menor
#    Dica: pesquise df.sort_values()