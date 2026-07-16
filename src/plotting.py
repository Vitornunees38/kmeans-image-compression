import numpy as np
import matplotlib.pyplot as plt


def plot3d(pontos, centroides, clusters, max_pontos=3000):

    m, n = pontos.shape
    if m > max_pontos:
        indices_aleatorios = np.random.choice(m, max_pontos, replace=False)
        amostra = pontos[indices_aleatorios]
    else:
        amostra = pontos

    # Pixels originais
    r_pontos = amostra[:, 0]
    g_pontos = amostra[:, 1]
    b_pontos = amostra[:, 2]

    # Centróides
    r_cent = centroides[:, 0]
    g_cent = centroides[:, 1]
    b_cent = centroides[:, 2]

    # Setup do Grafico
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    #Plot dos pixels originais
    ax.scatter(r_pontos, g_pontos, b_pontos, c=amostra, s=10, alpha=0.3)

    # Plot dos centroides
    ax.scatter(r_cent, g_cent, b_cent, c=centroides, s=300, marker='o', edgecolors='k', depthshade=False)

    ax.set_title(f"Espaço RGB com {clusters} Centróides")
    ax.set_xlabel(' Vermelho (R)')
    ax.set_ylabel(' Verde (G)')
    ax.set_zlabel(' Azul (B)')

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    plt.show()