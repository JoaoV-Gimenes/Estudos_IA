import numpy as np

np.random.seed(7)
salarios = np.random.randint(1500, 15000, size=(8,))

# 1. Normalize os salários para escala 0 a 1
# 2. Quais funcionários ganham acima da média?  
#    (retorne os índices E os valores)
# 3. Qual a diferença entre o maior e o menor salário?
# 4. Substitua todos os salários abaixo de 3000 por 3000
#    (piso salarial)

#1
calculo = np.round((salarios - salarios.min()) / (salarios.max() - salarios.min()), 2)
print(calculo.tolist())

#2
salarios_m = np.where(salarios > np.mean(salarios))[0]
print(salarios_m.tolist())
print(salarios[salarios_m].tolist())

#3
print(f'a diferença é de {np.ptp(salarios)}')

#4
print(np.clip(salarios, 3000, None))

##################################################################################################################################################################

np.random.seed(15)
estoque = np.random.randint(0, 50, size=(5, 6))
# 5 categorias de produto, 6 meses de estoque

# 1. Qual categoria teve o maior estoque total no período?
# 2. Em quais meses o estoque total de todas as categorias
#    ficou abaixo da média geral dos meses?
# 3. Normalize o estoque por categoria
#    (cada categoria na sua própria escala — diferente do exercício anterior!)
# 4. Crie um array booleano indicando quais células têm estoque crítico
#    (abaixo de 10 unidades)
# 5. Quantas células críticas existem no total?
#    Dica: pesquise o que acontece quando você soma um array booleano

#1
print(np.argmax(np.sum(estoque, axis=1)))

#2
total_categoria = np.sum(estoque, axis=0)
media = np.where(total_categoria < np.mean(total_categoria))[0]
print(media)

#3
maximos = estoque.max(axis= 1, keepdims=True)
minimos = estoque.min(axis=1, keepdims=True)
norm = np.round((estoque - minimos) / (maximos - minimos), 2)
print(norm)

#4
estoque2 = estoque < 10
print(estoque2)

#5
print(np.sum(estoque2))

##################################################################################################################################################################

np.random.seed(99)
dados = np.random.randint(1, 100, size=(4, 5))

# 1. Inverta a ordem das linhas da matriz
#    Dica: pesquise slicing com [::-1]
# 2. Inverta a ordem das colunas da matriz
# 3. Achate a matriz em um array 1D
#    Dica: pesquise np.flatten()
# 4. Transforme o array 1D de volta numa matriz 4x5
#    Dica: pesquise np.reshape()

#1
print(dados[::-1])

#2
print(dados[:, ::-1])

#3
lista1d = dados.flatten()
print(lista1d.tolist())

#4
print(np.reshape(lista1d, (4, 5), 'C' ))

##################################################################################################################################################################

np.random.seed(3)
# Simulando pixels de uma imagem em escala de cinza (0-255)
imagem = np.random.randint(0, 256, size=(8, 8))

# 1. Normalize a imagem para escala 0 a 1
# 2. Quantos pixels têm valor acima de 200? (pixels claros)
# 3. Substitua todos os pixels abaixo de 50 por 0
#    (escurecer pixels já escuros — técnica real de processamento)
# 4. Calcule a média de cada linha da imagem
# 5. Qual linha tem os pixels mais claros em média?

#1
print(np.round((imagem - imagem.min()) / (imagem.max() - imagem.min()), 2))

#2
print(np.sum(imagem > 200))

#3
sub = np.where(imagem < 50, 0, imagem)
print(sub)

#4
media = np.mean(imagem, axis=1)
print(media.tolist())

#5
print(np.argmax(media))

##################################################################################################################################################################

np.random.seed(42)
# Simulando 6 sensores medindo temperatura a cada hora por 24 horas
leituras = np.random.uniform(15.0, 40.0, size=(6, 24))

# 1. Qual sensor registrou a maior temperatura? Retorne o sensor E a hora
# 2. Calcule a média móvel de 3 horas do sensor 0
#    (média de cada janela de 3 horas consecutivas)
#    Dica: pesquise np.convolve()
# 3. Normalize cada sensor na sua própria escala (igual nível 3 anterior)
# 4. Identifique quais sensores tiveram alguma leitura acima de 37 graus
#    (retorne os índices dos sensores)
# 5. Crie uma matriz de correlação entre os 6 sensores
#    Dica: pesquise np.corrcoef()
#    O que os valores próximos de 1 e -1 significam?

#1
maximo_colunas = np.max(leituras, axis=0)
print(f'Hora: {np.round(maximo_colunas.argmax(), 2 )}')
maximo_linhas = np.max(leituras, axis=1)
print(f'Sensor: {np.round(maximo_linhas.argmax(), 2 )}')

sensor, hora = np.unravel_index(np.argmax(leituras), leituras.shape)
print(f'Sensor: {sensor}, Hora: {hora}')
#2
print(np.round(np.convolve(leituras[0], np.ones(3) / 3, mode='valid'), 2).tolist())

#3
maximos = leituras.max(axis = 1, keepdims=True)
minimo = leituras.min(axis = 1, keepdims=True)
print(np.round((leituras - minimo) / (maximos - minimo), 2).tolist())

#4
indices_maiores = np.where(np.any(leituras > 37, axis=1))[0]
print(indices_maiores.tolist())

#5
print(np.corrcoef(leituras))
#valores próximos de 1 significam elevada proporcionalidade, ao contrário do -1

##################################################################################################################################################################