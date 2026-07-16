import numpy as np
import time
from src.kmeans import inicializa_means, k_means
from src.image_utils import carrega_imagem, comprime_imagem
from src.metrics import calcular_mse
from src.plotting import plot3d

np.random.seed(42) #Seed definida para garantir resultados reproduzíveis

img = carrega_imagem()

pontos = img.reshape((-1, img.shape[2]))

tolerancia = 1e-2

#clusters_default = 16
#clusters_input = input(f'Insira o número de cores (clusters) na imagem comprimida (default = {clusters_default}): ')
#clusters = int(clusters_input) if clusters_input else clusters_default
clusters_opt = [2, 4, 8, 16, 32, 64]


for clusters in clusters_opt:
  pontos, centroides = inicializa_means(img,clusters)

  inicio = time.time() #Inicia tempo de execução do k-means
  centroides, indice, iteracoes = k_means(pontos, centroides, clusters, tolerancia)
  fim = time.time() #Finaliza tempo de execução do k-means

  print(f"\nGerando gráfico 3D para {clusters} cores...")
  plot3d(pontos, centroides, clusters)

  recuperado = comprime_imagem(centroides, indice, img, clusters)
  mse = calcular_mse(img, recuperado)


  print(f"-------Tolerancia: {tolerancia}--------")
  print(f"Convergencia atingida em {iteracoes} iteracoes")
  print(f"Tempo de execução do K-Means com {clusters} clusters: {fim - inicio:.4f} segundos")
  print(f"Erro Quadratico: {mse}")