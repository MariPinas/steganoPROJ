import cv2
from rich import print

def reveal_message():
    file_name = input("Insira o nome do arquivo da imagem: ")
    
    read_image = cv2.imread(file_name)

    if read_image is None:
        print("[red]Imagem nao encontrada![/red]")
        return
    
    b, g, r = cv2.split(read_image)
    blue_layer = b.copy()

    binary_message = ""
    decoded_message = ""

    height, width = blue_layer.shape

    for i in range(height):
        for j in range(width):
            pixel = blue_layer[i, j]
            lsb = pixel & 1
            binary_message += str(lsb)

            # quando acumular 8 bits, transformar em caractere
            if len(binary_message) >= 8:
                byte = binary_message[:8]
                binary_message = binary_message[8:]
                char = chr(int(byte, 2))
                decoded_message += char

                if decoded_message.endswith("#####"):
                    decoded_message = decoded_message.replace("#####", "")
                    print(f"\n[green]Mensagem revelada:[/green] {decoded_message}")
                    return decoded_message

    print("[red]Nenhuma mensagem encontrada![/red]")
    return ""
