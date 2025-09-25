import numpy as np
import cv2
import struct

def hideData(image, secret_message):
    """
    Esconde uma mensagem secreta em uma imagem usando LSB com NumPy vetorizado.
    Usa prefixo de tamanho para evitar falso-positivos.
    """
    # Converte mensagem para bytes
    secret_data_bytes = secret_message.encode('utf-8')

    # Prefixa o tamanho da mensagem (4 bytes)
    size_prefix = struct.pack(">I", len(secret_data_bytes))  # Big-endian
    full_data = size_prefix + secret_data_bytes

    # Calcula número máximo de bytes disponíveis
    n_bytes = image.size // 8
    if len(full_data) > n_bytes:
        raise ValueError("Erro: Mensagem muito grande para a imagem. Use uma imagem maior ou uma mensagem menor.")

    # Converte bytes para sequência de bits
    binary_secret_msg = np.unpackbits(np.frombuffer(full_data, dtype=np.uint8))

    # Achata a imagem para 1D
    flat_image = image.flatten()

    # Zera os LSBs dos primeiros N valores e insere os bits
    flat_image[:len(binary_secret_msg)] &= 0b11111110
    flat_image[:len(binary_secret_msg)] |= binary_secret_msg

    return flat_image.reshape(image.shape)

def showData(image):
    """
    Revela a mensagem escondida na imagem usando LSB.
    Lê o tamanho no início e depois apenas os bytes necessários.
    """
    flat_image = image.flatten()

    # Extrai os primeiros 32 bits (4 bytes) para saber o tamanho da mensagem
    size_bits = flat_image[:32] & 1
    size_bytes = np.packbits(size_bits).tobytes()
    msg_size = struct.unpack(">I", size_bytes)[0]

    # Extrai bits suficientes para a mensagem
    total_bits_needed = msg_size * 8
    msg_bits = flat_image[32:32 + total_bits_needed] & 1
    msg_bytes = np.packbits(msg_bits).tobytes()

    try:
        return msg_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return "ERRO: Não foi possível decodificar a mensagem (dados corrompidos)."

# --- Funções de Menu e Interação ---

def encode_text():
    image_name = input("Insira o nome da imagem (com extensão): ")
    try:
        image = cv2.imread(image_name)
        if image is None:
            print("Erro: Imagem não encontrada ou caminho incorreto.")
            return
        print("Dimensões da imagem:", image.shape)
        print("\n>> Uma janela com a imagem original vai aparecer.")
        print(">> Clique na janela e pressione qualquer tecla para continuar...")

        display_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
        cv2.imshow("Imagem Original", display_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return

    data = input("Insira a mensagem para ser codificada: ")
    if len(data) == 0:
        print("A mensagem não pode ser vazia.")
        return

    filename = input("Insira o nome da nova imagem (use .png ou .bmp): ").lower()
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        print("ERRO: Não use JPEG! Este formato comprime a imagem e corrompe os dados ocultos.")
        return
    if not (filename.endswith('.png') or filename.endswith('.bmp')):
        print("Aviso: É recomendável usar .png ou .bmp para preservar os dados.")

    try:
        encoded_image = hideData(image.copy(), data)
        cv2.imwrite(filename, encoded_image)
        print(f"Imagem '{filename}' salva com sucesso.")
    except ValueError as e:
        print(e)

def decode_text():
    image_name = input("Insira o nome da imagem codificada (com extensão): ")
    try:
        image = cv2.imread(image_name)
        if image is None:
            print("Erro: Imagem não encontrada ou caminho incorreto.")
            return ""

        print("\n>> Uma janela com a imagem codificada vai aparecer.")
        print(">> Clique na janela e pressione qualquer tecla para continuar...")

        display_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
        cv2.imshow("Imagem Codificada", display_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        text = showData(image)
        return text
    except Exception as e:
        print(f"Erro ao carregar ou decodificar a imagem: {e}")
        return ""

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