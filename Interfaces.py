import customtkinter


janela=customtkinter.CTk()
janela.geometry('595x500')
area1=customtkinter.CTkEntry(janela,placeholder_text='Adicione um titulo',width=250).place(x=10,y=40)
titulo=customtkinter.CTkLabel(janela,text='TITULO').place(x=15,y=10)
area2=customtkinter.CTkEntry(janela,placeholder_text="",width=300,height=330).place(x=10,y=100)
descricao=customtkinter.CTkLabel(janela,text='DESCRIÇÃO').place(x=15,y=70)
salvar=customtkinter.CTkButton(janela,text='SALVAR').place(x=10,y=440)
sair=customtkinter.CTkButton(janela,text='SAIR').place(x=160,y=440)
janela.mainloop()