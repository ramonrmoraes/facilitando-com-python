# Projeto: Facilitando com Python
# Descrição: Robô que automatiza o cadastro de produtos em um sistema web

import pyautogui
import time
import pandas as pd

# Pequena pausa automática entre comandos do PyAutoGUI
pyautogui.PAUSE = 0.3


# Abre o navegador Google Chrome
def abrir_navegador():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    time.sleep(2)

    # Coloca o navegador em tela cheia
    pyautogui.press("f11")
    time.sleep(1)


# Seleciona o modo visitante do Chrome
def selecionar_modo_visitante():
    pyautogui.click(x=90, y=840)

    time.sleep(1)

    # Maximiza a janela
    pyautogui.hotkey("win", "up")

    time.sleep(1)


# Acessa o sistema web
def acessar_sistema():
    pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.press("enter")

    time.sleep(3)


# Realiza login no sistema
def fazer_login():

    pyautogui.click(x=1830, y=374)

    pyautogui.write("pythonimpressionador@gmail.com")
    pyautogui.press("tab")

    pyautogui.write("SENHA_AQUI")

    pyautogui.click(x=2087, y=527)

    time.sleep(5)


# Carrega a base de dados de produtos
def carregar_tabela():

    tabela = pd.read_csv("produtos.csv")

    return tabela


# Cadastra os produtos no sistema
def cadastrar_produtos(tabela):

    for linha in tabela.index:

        pyautogui.click(x=1830, y=260)

        pyautogui.write(str(tabela.loc[linha, "codigo"]))
        pyautogui.press("tab")

        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")

        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")

        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")

        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab")

        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab")

        obs = tabela.loc[linha, "obs"]

        if not pd.isna(obs):
            pyautogui.write(str(obs))

        pyautogui.press("tab")
        pyautogui.press("enter")

        pyautogui.scroll(5000)


# Função principal do projeto
def main():

    abrir_navegador()

    selecionar_modo_visitante()

    acessar_sistema()

    fazer_login()

    tabela = carregar_tabela()

    cadastrar_produtos(tabela)


# Executa o programa
if __name__ == "__main__":
    main()
