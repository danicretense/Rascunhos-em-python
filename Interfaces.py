import customtkinter


janela=customtkinter.CTk()
janela.geometry('595x842')
area1=customtkinter.CTkEntry(janela,placeholder_text='Adicione um titulo').place(x=10,y=40)
janela.mainloop()