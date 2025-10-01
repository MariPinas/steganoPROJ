# Programa de Esteganografia – Segurança da Infomação 

Este repositório reúne o código referente a esteganografia. É possível esconder uma mensagem em uma imagem e depois revelar o texto escondido.

- Curso **Análise e Desenvolvimento de Sistemas**  
  **`Integrantes`**:
  - ANDRIEL HENRIQUE
  - FLÁVIA GOES 
  - MARIANA SANTOS  

---

## 📂 Estrutura do Repositório  

- **`assets/`**  
  Essa pasta contém as imagens disponíveis para realizar a esteganografia, imagens geradas também ficam armazenadas nesta pasta. 

- **`main/`**  
  O main importa os arquivos hide e reveal, para acessar cada função de forma dinâmica um menu foi estruturado.

- **`hide/`**  
  Nesse arquivo está a função hide_message, com ela é possível esconder uma mensagem em alguma imagem que existe no projeto ou em **`assets/`**

- **`reveal/`**  
  Nesse arquivo está a função reveal_message, com ela é possível revelar uma mensagem em alguma imagem secreta.

---

## 🔧 Como Executar  (Comandos)

1. Certifique de ter o python instalado
2. Instale dependências importantes:
- pip install opencv-python
- pip install rich
3. Insira as imagens que deseja utilizar na pasta assets.  
4. Execute o arquivo **`main/`**.
