# Mottu - Visão Computacional para Detecção de Motos

Este projeto é parte da 1ª Sprint do Desafio de Mapeamento Inteligente do Pátio da Mottu, com foco na implementação de um sistema de **detecção e classificação de motos via visão computacional**, utilizando **Python** e **OpenCV**.

---

## Objetivo

Desenvolver uma solução capaz de identificar o modelo das motos da Mottu (Pop, E, Sport) por meio de imagens ou vídeos, simulando o ambiente real dos pátios das filiais.

---

## 📁 Estrutura do Projeto

```
mottu_visao_computacional/
├── dataset/                       # Dataset simulado com imagens por tipo de moto
│   ├── mottu_e/
│   ├── mottu_pop/
│   └── mottu_sport/
├── detectar_motos.py             # Script de detecção/classificação visual (simulado)
├── 
├── mottu_classificacao_motos.ipynb  # Notebook com modelo de CNN para classificar imagens
├── README.md                     # Instruções e explicações do projeto
```

---

## Tecnologias Utilizadas

- Python 3.10
- OpenCV
- TensorFlow/Keras (CNN)
- Google Colab (para treinamento)
- Matplotlib

## Como Executar o Projeto

Treine o modelo no seu colab e salve o modelo treinado

Clone esse repositorio na sua maquina e coloque o modelo treinado dentro dele 

### Pré-requisitos

Certifique-se de ter instalado:

- Python 3.10
- Pip atualizado

Instale as dependências com:

```bash
pip install tensorflow opencv-python
```

Execute o script dentro da pasta da sua aplicação

```bash
python detectar_motos.py
```

---

Projeto desenvolvido por Fernando Henrique Vilela Aguiar (557525), Gabrielly Campos Macedo (558962) e Rafael Mocoto Magalhães Seo (554992) — FIAP

