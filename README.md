# Compressão de Imagens com K-Means

Implementação do algoritmo K-Means, desenvolvido do zero em Python, para compressão de imagens por meio da quantização de cores.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-✓-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-✓-green)

---

## Visão Geral

Este projeto implementa o algoritmo de clusterização K-Means do zero para realizar compressão de imagens por meio da redução da quantidade de cores (quantização de cores).
Representando a imagem como uma matriz de componentes tridimensionais (R,G,B) e realizando a clusterização dos pixels, subistitui-se cada pixel pelo valor do centróide do cluster ao qual é associado no espaço RGB.

<img src="/results/3dplot_8clusters.png">

Além da implementação do algoritmo, foram realizados experimentos para analisar como o número de clusters e o critério de convergência influenciam:

- Qualidade visual da imagem
- Erro Quadrático Médio (MSE)
- Tempo de execução
- Tamanho do arquivo gerado

---

## Funcionalidades

- Implementação do algoritmo K-Means sem bibliotecas de clusterização
- Quantização de cores em imagens
- Número de clusters configurável
- Tolerância de convergência configurável
- Cálculo do Erro Quadrático Médio (MSE)
- Comparação do tamanho dos arquivos
- Medição do tempo de execução
- Geração de gráficos para análise dos resultados

---

## Estrutura do Projeto

```text
.
├── images/
│   └── compressed/
├── results/
├── src/
│   ├── kmeans.py
│   ├── image_utils.py
│   ├── metrics.py
│   └── plotting.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Resultados

### Imagem Original

<img src="/images/paisagem.png">

### Imagens Comprimidas

<img src="https://i.imgflip.com/awps2h.gif">

### Erro Quadrático Médio (MSE)

<img src="/results/KxMSE.png">

### Tempo de Execução

<img src="/results/KxT.png">

### Tamanho do Arquivo

| Número de Clusters (K)     | Tamanho do arquivo (KB) |
| -------------------------- | ----------------------- |
| Imagem Original            | 419                     |
| 2                          | 20,5                    |
| 4                          | 34,3                    |
| 8                          | 55,8                    |
| 16                         | 151                     |
| 32                         | 201                     |
| 64                         | 247                     |

---

## Tecnologias Utilizadas

- Python
- NumPy
- OpenCV
- Matplotlib

---

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/Vitornunees38/image-compression-kmeans.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python main.py
```

---

## Funcionamento do Algoritmo

A implementação segue o fluxo clássico do algoritmo K-Means:

1. Inicialização dos centróides
2. Associação de cada pixel ao centróide mais próximo
3. Atualização dos centróides
4. Repetição até que o critério de convergência seja atingido
5. Reconstrução da imagem utilizando as cores dos centróides

---

## Contexto Acadêmico

Este projeto foi desenvolvido como trabalho final da disciplina de Computação Científica da Universidade Federal do Rio de Janeiro (UFRJ).

---

## Autor

Vitor Nunes

- GitHub: github.com/Vitornunees38
