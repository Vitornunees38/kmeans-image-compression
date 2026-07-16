import numpy as np

def inicializa_means(img, clusters):

    # Transforma em formato de matriz 2d
    pontos = img.reshape((-1, img.shape[2]))
    m, n = pontos.shape

    centroides = np.zeros((clusters, n))

    # inicializa centroides de forma aleatória
    for i in range(clusters):
        rand_indices = np.random.randint(m)
        centroides[i] = np.mean(pontos[rand_indices], axis=0)

    return pontos, centroides

def k_means(pontos, centroides, clusters, tolerancia):
  max_iter  = 100 # número de iterações
  deslocamento = float('inf')

  m, n = pontos.shape

  # Armazena o cluster correspondente a cada pixel
  indice = np.zeros(m)

  # Agoritmo k-means em si
  for i in range(max_iter):
    centroides_antigos = centroides.copy()

    # associa cada ponto ao centroide mais próximo
    for j in range(m):
      min_dist = float('inf')
      closest_centroid_idx = -1

      for k in range(clusters):
        # Distância Euclidiana entre vetores RGB de 3 dimensões
        dist = np.linalg.norm(pontos[j] - centroides[k])
        if dist < min_dist:
          min_dist = dist
          closest_centroid_idx = k
      indice[j] = closest_centroid_idx # Atribui o índice do centroide mais próximo

    # Atualiza os centroides
    for k in range(clusters):
      cluster_pontos = pontos[indice == k]
      if len(cluster_pontos) > 0:
        centroides[k] = np.mean(cluster_pontos, axis=0)


     # Critério de convergência
    deslocamento = np.linalg.norm(centroides - centroides_antigos)

    if deslocamento < tolerancia:
        iteracoes = i+1
        break

  return centroides, indice, iteracoes