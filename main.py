from hide import *
from reveal import *

def Steganography():
    while True:
        print("\n" + "="*25)
        print("    Esteganografia em LSB")
        print("="*25)
        print("1. Codificar mensagem em imagem")
        print("2. Decodificar mensagem de imagem")
        print("3. Sair")
        user_option_str = input("Insira uma opção: ")

        if user_option_str == '1':
            print("\n--- Modo de Codificação ---")
            encode_text()
        elif user_option_str == '2':
            print("\n--- Modo de Decodificação ---")
            decoded_message = decode_text()
            print("\n--- Mensagem Decodificada ---")
            print(decoded_message)
            print("-----------------------------")
        elif user_option_str == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, por favor insira um número de 1 a 3.")

        input("\nPressione Enter para voltar ao menu...")

if __name__ == '__main__':
    Steganography()