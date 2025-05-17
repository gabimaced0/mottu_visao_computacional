import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model

# Carregar o modelo treinado
modelo = load_model("modelo_mottu.keras")

# Definir as classes na mesma ordem usada no treino
classes = ["mottu_e", "mottu_pop", "mottu_sport"]

# Caminho da imagem para teste
imagem_path = "dataset/mottu_pop/mottu_pop_5.jpg"

# Verifica se o arquivo existe
if not os.path.exists(imagem_path):
    raise FileNotFoundError(f"Imagem não encontrada: {imagem_path}")

# Carregar e pré-processar a imagem
imagem = cv2.imread(imagem_path)
img_resized = cv2.resize(imagem, (224, 224)) / 255.0
img_input = img_resized.reshape((1, 224, 224, 3))

# Fazer predição com o modelo
pred = modelo.predict(img_input)
indice_classe = np.argmax(pred)
label = classes[indice_classe]

# Mostrar resultado na imagem
output = imagem.copy()
cv2.rectangle(output, (30, 30), (190, 190), (0, 255, 0), 2)
cv2.putText(output, label, (30, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Exibir a imagem
cv2.imshow("Detecção de Moto com Modelo Real", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
