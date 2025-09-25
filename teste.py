import cv2
import numpy as np

# === 1. Ler a imagem colorida ===
input_img = cv2.imread('golem.png')  # BGR
input_img = cv2.resize(input_img, (512, 512))

# === 2. Mensagem ===
message = 'geeksforgeeks'
binary_message = ''.join([format(ord(char), '08b') for char in message])
len_message = len(binary_message)

# === 3. Trabalhar no canal azul apenas ===
b, g, r = cv2.split(input_img)
blue_channel = b.copy()

embed_counter = 0
height, width = blue_channel.shape

for i in range(height):
    for j in range(width):
        if embed_counter < len_message:
            pixel = blue_channel[i, j]
            bit_to_embed = int(binary_message[embed_counter])
            pixel &= 0b11111110  # Zera o LSB
            pixel |= bit_to_embed  # Insere o bit
            blue_channel[i, j] = pixel
            embed_counter += 1

# === 4. Junta os canais e salva ===
encoded_img = cv2.merge((blue_channel, g, r))
cv2.imwrite('stego_colorida.png', encoded_img)
