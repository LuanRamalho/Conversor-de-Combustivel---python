import tkinter as tk
from tkinter import ttk

# Função para realizar a conversão
def converter():
    try:
        litros = float(entry_litros.get())
        galões_americanos = litros / 3.78541
        galões_britânicos = litros / 4.54609

        label_resultado_am.config(
            text=f"Galões Americanos: {galões_americanos:.2f}"
        )
        label_resultado_br.config(
            text=f"Galões Britânicos: {galões_britânicos:.2f}"
        )
    except ValueError:
        label_resultado_am.config(text="Erro: Insira um número válido")
        label_resultado_br.config(text="")

# Configuração da janela principal
root = tk.Tk()
root.title("Conversor de Combustível")
root.geometry("400x300")
root.configure(bg="#87CEEB")

# Título
titulo = tk.Label(
    root,
    text="Conversor de Combustível",
    font=("Helvetica", 18, "bold"),
    bg="#4682B4",
    fg="white",
    pady=10
)
titulo.pack(fill=tk.X)

# Caixa de entrada
frame_input = tk.Frame(root, bg="#87CEEB")
frame_input.pack(pady=20)

label_litros = tk.Label(
    frame_input, text="Litros:", font=("Helvetica", 14), bg="#87CEEB"
)
label_litros.grid(row=0, column=0, padx=10)

entry_litros = ttk.Entry(frame_input, font=("Helvetica", 14), width=10)
entry_litros.grid(row=0, column=1)

# Botão de conversão
botao_converter = tk.Button(
    root,
    text="Converter",
    command=converter,
    font=("Arial",14,"bold"),
    bg="darkslateblue",
    fg="greenyellow"
)
botao_converter.pack(pady=10)

# Resultados
frame_resultados = tk.Frame(root, bg="#87CEEB")
frame_resultados.pack(pady=20)

label_resultado_am = tk.Label(
    frame_resultados,
    text="Galões Americanos: ",
    font=("Helvetica", 14),
    bg="#87CEEB"
)
label_resultado_am.pack()

label_resultado_br = tk.Label(
    frame_resultados,
    text="Galões Britânicos: ",
    font=("Helvetica", 14),
    bg="#87CEEB"
)
label_resultado_br.pack()

root.mainloop()
