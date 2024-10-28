import webbrowser
from tkinter import *
from datetime import datetime


url_nba = "https://v4.rnbastreams.com/live-index5"

def atualizar_hora():
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d/%m\n%H:%M:%S")
    texto_data.config(text=f"{data_formatada}")
    janela_principal.after(1000, atualizar_hora)


def abrir_nba():
    webbrowser.open(url_nba)


janela_principal = Tk()

janela_principal.update_idletasks()
janela_principal.minsize(janela_principal.winfo_width() + 10, janela_principal.winfo_height() + 10)

janela_principal.title("NBA GAMES")
janela_principal.geometry("50x50")


texto_orientacao = Label(janela_principal, text="Clique para assistir os jogos de hoje")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

# Exibe a data atual e horario
texto_data = Label(janela_principal, font=("Helvetica", 10))
texto_data.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela_principal, text="NBA GAMES", command=abrir_nba)
botao.grid(column=0, row=3, padx=10, pady=10)

atualizar_hora()

janela_principal.mainloop()