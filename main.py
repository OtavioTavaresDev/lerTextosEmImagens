import pytesseract
from pathlib import Path
import cv2
import os
import pyautogui as pg
import PySimpleGUI as ps


def escan():
    global altura, largura
    caminho = values["inp"]
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    texto = pytesseract.image_to_string(caminho, lang="por")
    janela["txtescan"].update(value=texto)
    print(texto)

altura = 50
largura = 100
layout = [
    [ps.Text("Pegar textos em imagens")],
    [ps.Text("Caminho da imagem: "),ps.Input("", key="inp", size=(80,5)),ps.Button("Escanear"), ps.Button("Limpar Texto")],
    [ps.Multiline("", key="txtescan", size=(largura,altura))]
]
janela = ps.Window("Escanear textos em imagens", layout, resizable= True)

while True:
    event, values = janela.read()
    if event == ps.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == "Escanear":
        escan()

    if event == "Limpar Texto":
        janela["txtescan"].update(value="")


janela.close()



#lista = os.listdir(r"C:\Users\Cliente\pc\Imagens\Capturas de tela")
#    valor_de_lista = int(-2)
#    if "png" in lista[valor_de_lista] or "jpg" in lista[valor_de_lista] or "jpeg" in lista[valor_de_lista]:
#        os.rename(lista[valor_de_lista], )

#   elif "png" in lista[valor_de_lista] or "jpg" in lista[valor_de_lista] or "jpeg" in lista[valor_de_lista]:
#        valor_de_lista = int(-2)