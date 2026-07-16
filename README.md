# Image Compression with K-Means

Image compression through color quantization using the K-Means clustering algorithm implemented from scratch in Python.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-✓-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-✓-green)

## Overview

This project implements the K-Means clustering algorithm from scratch to perform image compression by reducing the number of colors in an image.

The project evaluates how the number of clusters and the convergence tolerance affect:

- Image quality
- Mean Squared Error (MSE)
- Compression ratio
- Execution time

---

## Features

- K-Means implemented from scratch
- Image color quantization
- Adjustable number of clusters
- Adjustable convergence tolerance
- MSE calculation
- Compression ratio analysis
- Execution time measurement
- Result visualization

---

## Project Structure

```
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

## Results

### Original image

<img src="/images/paisagem.png>

### Compressed images

*adicionar gif*

---

### MSE

*adicionar gráfico*

---

### Execution Time

*adicionar gráfico*

---

### File Size

*adicionar gráfico*

---

## Technologies

- Python
- NumPy
- Matplotlib
- Opencv

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Vitornunees38/image-compression-kmeans.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## Algorithm

The implementation follows the traditional K-Means workflow:

1. Initialize centroids
2. Assign each pixel to its nearest centroid
3. Recalculate centroids
4. Repeat until convergence
5. Reconstruct the image using centroid colors

---

## Academic Context

This project was developed as the final assignment for the Scientific Computing course at the Federal University of Rio de Janeiro (UFRJ).
