import cv2

def hide_message():
    message = input("Insira uma mensagem: ")
    file_name = input("Insira o nome do arquivo da imagem: ")

    read_image = cv2.imread(file_name)
    image_resize = cv2.resize(read_image, (512, 512))
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    lenght_message = len(binary_message)

    b, g, r = cv2.split(image_resize)
    blue_layer = b.copy()

    counter = 0
    height, width = blue_layer.shape

    for i in range(height):
        for j in range(width):
            if(counter < lenght_message):
                pixel = blue_layer[i, j]
                bit_input = int(binary_message[counter])
                pixel &= 0b11111110
                pixel |= bit_input
                blue_layer[i, j] = pixel
                counter += 1
    
    hide_image = cv2.merge((blue_layer, g, r))
    cv2.imwrite('secret_image.png', hide_image)