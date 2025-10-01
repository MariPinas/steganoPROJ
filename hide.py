import cv2
from rich import print
import os

def hide_message():
    message = input("Insira uma mensagem: ") + "#####"
    file_name = input("Insira o nome do arquivo da imagem: ")
    
    read_image = cv2.imread(file_name)

    if read_image is None:
        alt_path = os.path.join("assets", file_name)
        read_image = cv2.imread(alt_path)
    
        if read_image is None:
            print("[red]Imagem nao encontrada![/red]")
            return
        else:
            print(f"[yellow]Imagem encontrada na pasta 'assets': {alt_path}")
            file_name = alt_path
    else:
        print("[green]Imagem encontrada com sucesso![/green]")
    
    #image_resize = cv2.resize(read_image, (512, 512)) // comentei pra deixar a img do tamanho real que ela é
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    lenght_message = len(binary_message)

    b, g, r = cv2.split(read_image)
    blue_layer = b.copy()

    counter = 0
    height, width = blue_layer.shape

    if lenght_message > height * width:
        print("[red]Mensagem muito grande para essa imagem![/red]")
        return

    for i in range(height):
        for j in range(width):
            if counter < lenght_message:
                pixel = blue_layer[i, j]
                bit_input = int(binary_message[counter])
                pixel &= 0b11111110
                pixel |= bit_input
                blue_layer[i, j] = pixel
                counter += 1
    
    base_name = os.path.splitext(file_name)[0]  # pega o nome do arquivo sem a extensao
    output_name = f"{base_name}_secret.png"     # cria o nome do arquivo com o nome original + _secret.png

    hide_image = cv2.merge((blue_layer, g, r))
    cv2.imwrite(output_name, hide_image)
    print(f"[green]Mensagem escondida em '{output_name}' com sucesso![/green]")