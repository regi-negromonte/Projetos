import tkinter as tk
from tkinter import ttk
import time

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro @Regi-Negromonte")
        self.root.geometry("350x150")
        self.root.configure(bg="#2E3440")

        self.tempo_inicial = 0
        self.tempo_pausado = 0
        self.executando = False

        self.label_tempo = tk.Label(root, text="00:00:00.000", font=("Helvetica", 24), fg="#D8DEE9", bg="#2E3440")
        self.label_tempo.pack(pady=20)

        self.botao_iniciar = ttk.Button(root, text="Iniciar", command=self.iniciar)
        self.botao_iniciar.pack(side=tk.LEFT, padx=10)

        self.botao_pausar = ttk.Button(root, text="Pausar", command=self.pausar, state=tk.DISABLED)
        self.botao_pausar.pack(side=tk.LEFT, padx=10)

        self.botao_parar = ttk.Button(root, text="Parar", command=self.parar, state=tk.DISABLED)
        self.botao_parar.pack(side=tk.LEFT, padx=10)

    def iniciar(self):
        if not self.executando:
            if self.tempo_pausado == 0:
                self.tempo_inicial = time.time()
            else:
                self.tempo_inicial = time.time() - self.tempo_pausado
            self.executando = True
            self.atualizar_tempo()
            self.botao_iniciar.config(state=tk.DISABLED)
            self.botao_pausar.config(state=tk.NORMAL)
            self.botao_parar.config(state=tk.NORMAL)

    def pausar(self):
        if self.executando:
            self.tempo_pausado = time.time() - self.tempo_inicial
            self.executando = False
            self.botao_iniciar.config(state=tk.NORMAL)
            self.botao_pausar.config(state=tk.DISABLED)

    def parar(self):
        self.executando = False
        self.tempo_pausado = 0
        self.label_tempo.config(text="00:00:00.000")
        self.botao_iniciar.config(state=tk.NORMAL)
        self.botao_pausar.config(state=tk.DISABLED)
        self.botao_parar.config(state=tk.DISABLED)

    def atualizar_tempo(self):
        if self.executando:
            tempo_decorrido = time.time() - self.tempo_inicial
            horas, resto = divmod(tempo_decorrido, 3600)
            minutos, segundos = divmod(resto, 60)
            milissegundos = int((tempo_decorrido - int(tempo_decorrido)) * 1000)
            tempo_formatado = f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}.{milissegundos:03}"
            self.label_tempo.config(text=tempo_formatado)
            self.root.after(10, self.atualizar_tempo)  # Atualiza a cada 10ms

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()