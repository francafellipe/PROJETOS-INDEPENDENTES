import mysql.connector
from tkinter import *

config = {
    "host": "localhost",
    "user": "root",
    "password": ""
}

connector = mysql.connector.connect(**config)

cursor = connector.cursor()
query = "CREATE DATABASE IF NOT EXISTS futureIndustrie"
cursor.execute(query)

use = "USE futureIndustrie"
cursor.execute(use)

tabela = "CREATE TABLE IF NOT EXISTS usuario (id INT PRIMARY KEY AUTO_INCREMENT, usuario VARCHAR(255), senha VARCHAR(255))"
cursor.execute(tabela)
def new_user():
    def addUser():
        name = login_entry.get()
        password = senha_entry.get()
        addUser_query = "INSERT INTO usuario (usuario, senha) VALUES (%s, %s)"
        values = (name, password)
        cursor.execute(addUser_query, values)
        connector.commit()
        new_user_janela.destroy()
    new_user_janela = Toplevel(janela)
    new_user_janela.title("Adicionar usuario ")
    label_usuario = Label(new_user_janela,text="Digite o Login")
    label_usuario.pack()
    login_entry = Entry(new_user_janela)
    login_entry.pack()
    label_senha = Label(new_user_janela,text="Defina uma senha de no minimo 6 Digitos :")
    label_senha.pack()
    senha_entry = Entry(new_user_janela)
    senha_entry.pack()
    botao_cadastrar = Button(new_user_janela,text="Cadastrar",command=addUser)
    botao_cadastrar.pack()
    
def destroybank():
    dropdatabase = "DROP DATABASE futureIndustrie"
    cursor.execute(dropdatabase)
    

def alterpassword():

    def botaosave():
        senhaupdate = "UPDATE usuario SET senha = (%s)  WHERE usuario = (%s) "
        novapassword = entry_passnew.get()
        login = entry_loginconf.get()
        values = (novapassword,login)
        cursor.execute(senhaupdate,values)
        connector.commit()
        new_pass_janela.destroy()


    new_pass_janela = Toplevel(janela)
    new_pass_janela.title("Cadastrar nova senha")
    label_login = Label(new_pass_janela,text='Digite o seu login :')
    label_login.pack()
    entry_loginconf = Entry(new_pass_janela)
    entry_loginconf.pack()
    label_passnew = Label (new_pass_janela,text="Digite a nova senha:")
    label_passnew.pack()
    entry_passnew = Entry(new_pass_janela,show="*")
    entry_passnew.pack() 
    botaosave_newpassword = Button(new_pass_janela,text="Salvar Senha",command=botaosave)
    botaosave_newpassword.pack()



janela=Tk()
janela.title("Pagina de Cadastro e login")
janela.geometry("500x400")

     #labels 
#label escolha 
label_escolha = Label(janela,text="Administrador Escolha uma opção !")
label_escolha.pack()
#botões 
# 1 - Adicionar usuario
adicionar_usuario = Button(janela,text="CRIAR NOVO CADASTRO ",command=new_user)
adicionar_usuario.pack()
 #2 - Alterar usuario
alterar_usuario = Button(janela,text="ALTERAR SENHA",command=alterpassword)
alterar_usuario.pack()
 #3 - Excluir usuario
excluir_usuario = Button(janela,text="EXCLUIR BANCO DE DADOS ",command=destroybank)
excluir_usuario.pack()
 #4 - Sair''
finalizar = Button(janela,text="Finalizar")
finalizar.pack()



#    change == "1":
#        name = input("Digite um usuario:")
#        password = input("Digite uma senha:")
# #       addUser(name, password)
#
#    change == "2":
#        
#    change == "4":
#        curso.close()
#        break

janela.mainloop()