from stegano import lsb
clear_message = lsb.reveal("./segredo.png")
print(clear_message)