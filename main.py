from stegano import lsb
secret = lsb.hide("./assets/sitch.png", "receba")
secret.save("./segredo.png")
