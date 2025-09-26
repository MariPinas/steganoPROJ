from hide import *
from reveal import *

def menu():
    while True:
        print("\n" + "="*25)
        print("   Esteganografia")
        print("="*25)
        print("1. Esconder mensagem em imagem")
        print("2. Revelar mensagem da imagem")
        print("3. Sair")
        user_option_str = input("Insira uma opção: ")

        match user_option_str:
            case '1':
                print("\n --- Esconder Mensagem")
            case '2':
                print("\n --- Revelar Mensagem")
                mensagem_revelada = 'Mensagem Revelada'
                print("Mensagem revelada: "), mensagem_revelada
                print("-----------------------------")
            case '3':
                print('Finalizando Esteganografia')
                break
            case _:
                print('Opção inválida')
                
        input("\nPressione Enter para voltar ao menu...")

if __name__ == '__main__':
    menu()