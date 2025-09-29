from hide import *
from reveal import *
from rich import print

def menu():
    while True:
        print("\n" + "="*25)
        print("[italic red]Esteganografia[/italic red]")
        print("="*25)
        print("1. Esconder mensagem em imagem")
        print("2. Revelar mensagem da imagem")
        print("3. Sair")
        option = input("Insira uma opção: ")

        match option:
            case '1':
                print("\n --- Esconder Mensagem")
                hide_message()
                print("\n---------------------------------------")
            case '2':
                print("\n --- Revelar Mensagem")
                reveal_message()
                print("\n---------------------------------------")
            case '3':
                print('Finalizando Esteganografia')
                break
            case _:
                print('Opção inválida')
                
        input("\nPressione Enter para voltar ao menu...")

if __name__ == '__main__':
    menu()