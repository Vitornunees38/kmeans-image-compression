import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path



def carrega_imagem():

    BASE_DIR = Path(__file__).resolve().parent.parent
    IMAGE_PATH = BASE_DIR / "images" / "paisagem.png"

    img = cv2.imread(str(IMAGE_PATH))
    print(img.shape)

    #Converte de BGR para RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #Divide os valores por 255  para que vão de 0 a 1
    img = img / 255.0

    return img

def comprime_imagem(centroides, indice, img, clusters):
  
  BASE_DIR = Path(__file__).resolve().parent.parent
  OUTPUT_DIR = BASE_DIR / "images" / "compressed"
  OUTPUT_DIR.mkdir(parents=True, exist_ok=True) # cria a pasta se não existir

  # Recupera a imagem comprimida, associando cada pixel ao centroide correspondente
  centroide = np.array(centroides)
  recuperado = centroide[indice.astype(int), :]

  # Retorna à matriz 3D (linha, coluna, rgb(3))
  recuperado = recuperado.reshape(img.shape)

  # Plotando e salvando a imagem comprimida
  plt.figure(figsize=(10,5))

  plt.subplot(1,2,1)
  plt.imshow(img)
  plt.title("Original")
  plt.axis("off")

  plt.subplot(1,2,2)
  plt.imshow(recuperado)
  plt.title(f"{clusters} cores")
  plt.axis("off")

  plt.show()

  # Para salvar com cv2.imwrite, a imagem deve estar em BGR e com valores de 0 a 255 (uint8)
  # Primeiro, converte de RGB [0,1] para RGB [0,255]
  recuperado_scaled = (recuperado * 255).astype(np.uint8)
  # Depois, converte de RGB para BGR para cv2.imwrite
  recuperado_bgr = cv2.cvtColor(recuperado_scaled, cv2.COLOR_RGB2BGR)

  arquivo = OUTPUT_DIR / f"imagem_comprimida_{clusters}_cores.png"

  cv2.imwrite(str(arquivo), recuperado_bgr)

  return recuperado