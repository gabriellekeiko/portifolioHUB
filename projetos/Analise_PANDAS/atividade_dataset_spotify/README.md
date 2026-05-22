# Spotify Tracks Analysis & Dashboard

Aqui encontras uma análise exploratória de dados combinada com um painel web interativo baseado no design escuro do Spotify. O projeto estuda as características de faixas musicais e a popularidade de diferentes géneros.

---

## Sobre o Projeto

Este repositório divide-se em duas partes complementares:
1. **Análise de Dados (`.ipynb`):** Um notebook (Colab) onde os dados são processados com *Pandas* e visualizados através de gráficos da biblioteca *Plotly*.
2. **Dashboard Web (`index.html`):** Uma interface web responsiva criada com HTML/CSS e gráficos dinâmicos, ideal para alojamento gratuito no **GitHub Pages**.

---

## O Conjunto de Dados

O estudo baseia-se num ficheiro de dados que contém mais de **114.000 músicas** distribuídas por **114 géneros musicais**. Cada música possui atributos analíticos como:

* **Métricas Acústicas:** `danceability` (dançabilidade), `energy` (energia), `loudness` (volume), `acousticness`, `instrumentalness` e `tempo` (BPM).
* **Métricas de Sucesso:** `popularity` (popularidade de 0 a 100).
* **Metadados:** `track_id`, `artists`, `album_name`, `track_name` e `explicit` (conteúdo explícito).

---

## Principais Insights e Gráficos

A partir do processamento feito no Python, destacam-se análises como o **Top 10 Géneros com Maior Média de Popularidade**. O gráfico interativo permite filtrar e visualizar diretamente métricas de géneros de grande sucesso como *pop-film*, *k-pop*, *chill*, *sertanejo*, entre outros.

---

## Estrutura do Repositório

* `Atv_Spotify_Tracks_Dataset.ipynb` -> Jupyter Notebook com toda a análise exploratória.
* `index.html` -> Código do Dashboard interativo (GitHub Pages).
* `dataset.csv` -> Base de dados em formato CSV (se incluída no repositório).

---

## Tecnologias Utilizadas

* **Python 3** (Pandas, NumPy) — Para a engenharia e tratamento dos dados.
* **Plotly / Plotly.js (Colab)** — Para a criação de gráficos dinâmicos e interativos.
* **HTML5 & CSS3** — Para a estilização personalizada com a paleta de cores do Spotify.
* **Font Awesome** — Biblioteca de ícones vetoriais integrados na página.
* **Git Bash** — Para versionamento e 'push'

---

## Autoria
Este projeto foi desenvolvido por:
* **Gabrielle Keiko**
  * Aluna de Ciência de Dados e Machine Learning no **CEUB**
  * Introdução a Ciência de Dados 2026
  * E-mail institucional: gabrielle.keiko@sempreceub.com | E-mail pessoal: gkeiko.05@gmail.com
  * Meu Perfil no LinkedIn: https://www.linkedin.com/in/gabrielle-keiko-9baa6a2b3/
