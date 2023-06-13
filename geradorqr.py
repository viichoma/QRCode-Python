from pyqrcode import *
from png import *
import tkinter
from tkinter import *
import os
from PIL import Image, ImageTk

#TELA
janela = Tk()
janela.title("Gerador QRCode")
janela.iconbitmap("icone.ico")
janela.geometry("600x500+700+300")
frame = Frame(janela, bg="#A7C7E7")
frame.place(width=2000, height=1100)

#imagem do diretorio da aplicacao
botaoimg = Image.open("botaogerar.png")
botaoimg = botaoimg.resize((110,35), Image.ANTIALIAS)
botaoimg = ImageTk.PhotoImage(botaoimg)
#PEGAR USUARIO
usuario = os.getlogin()

texto_orientacao = Label(janela, text="Insira o url que deseja transformar em QRCode", font=("ARIAL BLACK",16),bg='#A7C7E7',fg="#000000")
texto_orientacao.place( x=30, y=20)

texto_url = Entry(janela, text="", font=("bold",10), border=1, borderwidth=3)
texto_url.place(x=115, y=80, width=350, height= 35)

#MUDAR DIRETORIO PARA ONDE O ARQUIVO SERA SALVO
os.chdir(f'C:/Users/{usuario}/Desktop/')

#GERAR QRCODE
def gerarqrcode():
    url = pyqrcode.create(texto_url.get(), error='L', version=10)
    if texto_url.get()!="":
        url.png('qrcode.png', scale=4, module_color=(0, 0, 0), background=(255, 255, 255, 255))
        diretorio = (f'C:/Users/{usuario}/Desktop/qrcode.png')

        texto_geracao = Label(janela, text="Codigo gerado com sucesso!", font=("ARIAL BLACK",15),bg='#A7C7E7',fg="#000000")
        texto_geracao.place(x=150, y=130)

        imgqr = ImageTk.PhotoImage(Image.open(f'{diretorio}'))
        imagemqr = tkinter.Label(image=imgqr)
        imagemqr.image = imgqr
        imagemqr.place(x=180, y=190)



botao_gerar = Button(janela, image= botaoimg, command=(gerarqrcode), bd=0, bg='#A7C7E7')
botao_gerar.place(x=480, y=80, width=110, height=35)

janela.mainloop()
