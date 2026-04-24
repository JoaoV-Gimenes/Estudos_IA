import numpy as np

# Você tem as notas de 5 alunos em 3 matérias
notas = np.array([
    [6.0, 7.5, 8.0],
    [9.0, 5.0, 7.0],
    [4.5, 6.0, 5.5],
    [8.0, 9.0, 9.5],
    [7.0, 6.5, 8.5]
])

# Tente calcular:
# 1. A média de cada aluno (média das 3 matérias)
# 2. A média de cada matéria (média dos 5 alunos)
# 3. Quais alunos têm média >= 7.0
# 4. A nota máxima da turma inteira

#1
media_alunos = np.round(np.mean(notas, axis=1), 2).tolist()
print(media_alunos)

#2
media_materias = np.round(np.mean(notas, axis=0), 2).tolist()
print(media_materias)

#3
media_alunos = np.round(np.mean(notas, axis=1))
aprovados_mask = media_alunos >= 7
indices = np.where(aprovados_mask)[0]
print(indices)

##################################################################################################################################################################

# Dado esse array:
temperaturas = np.array([23.5, 28.0, 19.2, 31.4, 25.7, 22.1, 30.0])

# 1. Qual foi a temperatura máxima e mínima?
# 2. Qual a média das temperaturas?
# 3. Quais dias tiveram temperatura acima de 25 graus?
# 4. Substitua todas as temperaturas abaixo de 23 por 23 (temperatura mínima aceitável)
#    Dica: pesquise np.clip()

#1
print(f'A temperatura máxima foi de: {np.max(temperaturas)}')
print(f'A temperatura mínima foi de: {np.min(temperaturas)}')

#2
print(f'A média das temperaturas foi de: {np.mean(temperaturas)}')

#3
print(np.where(temperaturas > 25)[0] + 1)

#4
print(np.clip(temperaturas, 23, None))

##################################################################################################################################################################

# Matriz de vendas: 4 vendedores, 3 meses (jan, fev, mar)
vendas = np.array([
    [1500, 2300, 1800],
    [3200, 2800, 3500],
    [900,  1200, 1100],
    [2100, 1900, 2400]
])

# 1. Qual o total vendido por cada vendedor nos 3 meses?
# 2. Qual o total vendido em cada mês pelos 4 vendedores?
# 3. Qual vendedor teve a maior venda em um único mês? (retorne o índice)
# 4. Normalize as vendas para uma escala de 0 a 1
#    Fórmula: (valor - min) / (max - min)

#1
print(np.sum(vendas, axis=1).tolist())

#2
print(np.sum(vendas, axis=0).tolist())

#3
print(f'Vendedor {np.argmax(np.max(vendas, axis=1))}')

#4
conta = np.round((vendas - vendas.min())/ (vendas.max() - vendas.min()), 2)

##################################################################################################################################################################

np.random.seed(42)  # garante que todos teremos os mesmos números aleatórios
dados = np.random.randint(0, 100, size=(10, 5))

# Imagine que são notas de 10 alunos em 5 provas
# 1. Calcule a média de cada aluno
# 2. Calcule o desvio padrão de cada aluno (np.std)
#    (desvio padrão mede o quanto as notas variam — um aluno consistente tem desvio baixo)
# 3. Qual aluno foi mais consistente (menor desvio padrão)?
# 4. Crie um novo array apenas com as notas dos alunos que têm média >= 60
# 5. Quantos alunos foram aprovados?

#1
medias = np.round(np.mean(dados, axis=1), 2)
print(medias.tolist())

#2
desv_p = np.round(np.std(dados, axis=1), 2)
print(desv_p.tolist())

#3
print(np.argmin(desv_p))

#4
alunos = np.where(medias >= 60)[0]
novos_dados = dados[alunos]
print(novos_dados.tolist())

#5
print(len(novos_dados))

##################################################################################################################################################################

produtos = np.array([
    [12.50, 8.00, 15.00, 9.50],   # loja 1: preços de 4 produtos
    [11.00, 9.50, 14.00, 10.00],  # loja 2
    [13.00, 7.50, 16.00, 8.00]    # loja 3
])

# 1. Qual o preço médio de cada loja?
# 2. Qual o preço médio de cada produto entre as lojas?
# 3. Qual loja tem o maior gasto total?
# 4. Qual produto é mais barato em média?

#1
print(np.round(np.mean(produtos, axis=1),2).tolist())

#2
media_p = np.round(np.mean(produtos, axis=0))
print(media_p.tolist())

#3
gasto_total = np.sum(produtos, axis=1)
print(gasto_total.max())
print(f'o vendedor {np.argmax(gasto_total)} foi o que tem maior gasto total')

#4
print(f'O produto mais barato em média é o {np.argmin(media_p)}')

##################################################################################################################################################################