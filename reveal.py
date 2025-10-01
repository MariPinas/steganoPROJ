import cv2
from rich import print
import os

def reveal_message():
    file_name = input("Insira o nome do arquivo da imagem: ")
    
    if not os.path.isfile(file_name):
        alt_path = os.path.join("assets", file_name) 
        if not os.path.isfile(alt_path):
            print("[red]Arquivo nao encontrado![/red]")
            return
        else:
            print(f"[yellow]Imagem encontrada na pasta 'assets': {alt_path}")
            file_name = alt_path
    
    read_image = cv2.imread(file_name)

    if read_image is None:
        print("[red]Imagem inválida![/red]")
        return
    else:
        print("[green]Imagem válida! [/green]")
    
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

                if len(decoded_message) > 10000:
                    print("[yellow]Mensagem muito longa ou delimitador não encontrado. Busca encerrada![/yellow]")
                    return decoded_message

                if decoded_message.endswith("#####"):
                    decoded_message = decoded_message.replace("#####", "")
                    print(f"\n[green]Mensagem revelada:[/green] {decoded_message}")
                    return decoded_message

    print("[red]Nenhuma mensagem encontrada![/red]")
    return ""
