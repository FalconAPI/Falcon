
import os
from tkinter import Tk
from tkinter import *
from random import randrange, choice

def Destroi_itens(lista: list):
    for item in lista:
        item.destroy()

class Login:
    def Iniciar(self, jan):
        self.jan = jan
        
        path = os.path.dirname(__file__)

        # imagem = PhotoImage(file=f'{path}/git.png')
        # self.img = Label(self.jan, image=imagem).pack()
        # self.img.place(x=0, y=0)
        
        self.login_name = Label(self.jan, text='Login', fg='red', font=('Arial', 100))
        self.login_name.place(x=500, y=300)

        self.user = Label(self.jan, text='Usuario', font=('Arial', 20), fg='blue')
        self.user.place(x=500, y=500)

        self.user_entry = Entry(self.jan, width=25)
        self.user_entry.place(x=610, y=515)

        self.pasw = Label(self.jan, text='Senha', font=('Arial', 20), fg='blue')
        self.pasw.place(x=500, y=600)

        self.pasw_entry = Entry(self.jan, width=25)
        self.pasw_entry.place(x=610, y=615)

        self.login_button = Button(self.jan, text='Login', font=('Arial', 15), fg='blue', command=lambda: Destroi_itens(self.lista_de_teste))
        self.login_button.place(x=700, y=700)

        self.register_button = Button(self.jan, text='Registrar-se', font=('Arial', 12), fg='blue', command=self.Apertei_no_login)
        self.register_button.place(x=500, y=700)

        self.lista_de_teste = [self.user, self.user_entry, self.pasw,self.pasw_entry, self.login_button, self.register_button, self.login_name]

    def Login(self):
        item = choice(self.lista_de_teste)
        item.destroy()

    def Apertei_no_login(self):
        x = randrange(10, 700)
        y = randrange(10, 700)
        Label(text='Apertei no botão de Login', font=('Arial', 20), fg='blue').place(x=x, y=y)

        




jan = Tk()

Login().Iniciar(jan)

jan.mainloop()
