import tkinter as tk
from tkinter import ttk, messagebox

class ControleFinanceiro:
    def __init__(self, root):
        # Inicializa a janela principal e configurações básicas
        self.root = root
        self.root.title("Controle Financeiro")
        self.root.geometry("600x600")
        self.root.configure(bg='#dbdbdb')

        self.total_disponivel = 0.0  # Armazena o total disponível
        self.entradas = 0.0  # Armazena o valor total de entradas
        self.saidas = 0.0  # Armazena o valor total de saídas
        self.transacoes = []  # Lista para armazenar as transações
        self.transacao_id = 0  # Contador para os IDs das transações

        # Frame do cabeçalho
        self.header_frame = ttk.Frame(root, padding="10")
        self.header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Label do título
        self.title_label = ttk.Label(self.header_frame, text="CONTROLE FINANCEIRO", font=("Helvetica", 16, "bold"))
        self.title_label.pack()

        # Frame do resumo financeiro
        self.summary_frame = ttk.Frame(root, padding="10", relief="solid")
        self.summary_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Labels de entradas, saídas e total
        self.entradas_label = ttk.Label(self.summary_frame, text="Entradas\nR$ 0.00", font=("Helvetica", 12), foreground='green')
        self.entradas_label.grid(row=0, column=0, padx=20, pady=10)

        self.saidas_label = ttk.Label(self.summary_frame, text="Saídas\nR$ 0.00", font=("Helvetica", 12), foreground='red')
        self.saidas_label.grid(row=0, column=1, padx=20, pady=10)

        self.total_label = ttk.Label(self.summary_frame, text="Total\nR$ 0.00", font=("Helvetica", 12))
        self.total_label.grid(row=0, column=2, padx=20, pady=10)

        # Frame do formulário de entrada de dados
        self.form_frame = ttk.Frame(root, padding="10")
        self.form_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Labels e campos de entrada de descrição e valor
        self.descricao_label = ttk.Label(self.form_frame, text="Descrição:", font=("Helvetica", 10))
        self.descricao_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.descricao_entry = ttk.Entry(self.form_frame, width=20)
        self.descricao_entry.grid(row=0, column=1, padx=5, pady=5)

        self.valor_label = ttk.Label(self.form_frame, text="Valor:", font=("Helvetica", 10))
        self.valor_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.valor_entry = ttk.Entry(self.form_frame, width=10)
        self.valor_entry.grid(row=0, column=3, padx=5, pady=5)

        # Radio buttons para selecionar o tipo de transação (entrada ou saída)
        self.tipo_var = tk.StringVar()
        self.entrada_radio = ttk.Radiobutton(self.form_frame, text="Entrada", variable=self.tipo_var, value="entrada")
        self.entrada_radio.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        self.saida_radio = ttk.Radiobutton(self.form_frame, text="Saída", variable=self.tipo_var, value="saida")
        self.saida_radio.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        # Botão para adicionar a transação
        self.add_button = ttk.Button(self.form_frame, text="ADICIONAR", command=self.adicionar_transacao)
        self.add_button.grid(row=0, column=6, padx=5, pady=5)

        # Frame das transações
        self.transacoes_frame = ttk.Frame(root, padding="10")
        self.transacoes_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Treeview para mostrar as transações
        self.transacoes_tree = ttk.Treeview(self.transacoes_frame, columns=("ID", "Descrição", "Valor", "Tipo"), show='headings', height=10)
        self.transacoes_tree.heading("ID", text="ID")
        self.transacoes_tree.heading("Descrição", text="Descrição")
        self.transacoes_tree.heading("Valor", text="Valor")
        self.transacoes_tree.heading("Tipo", text="Tipo")
        self.transacoes_tree.column("ID", width=30, anchor="center")
        self.transacoes_tree.column("Descrição", width=180, anchor="center")
        self.transacoes_tree.column("Valor", width=100, anchor="center")
        self.transacoes_tree.column("Tipo", width=50, anchor="center")
        self.transacoes_tree.pack(side="left", fill="both", expand=True)

        self.transacoes_scroll = ttk.Scrollbar(self.transacoes_frame, orient="vertical", command=self.transacoes_tree.yview)
        self.transacoes_scroll.pack(side="right", fill="y")
        self.transacoes_tree.configure(yscroll=self.transacoes_scroll.set)

        # Botão para deletar a transação selecionada
        self.delete_button = ttk.Button(root, text="Deletar Selecionado", command=self.deletar_transacao)
        self.delete_button.grid(row=4, column=0, padx=5, pady=5)

        # Botão para zerar entradas e saídas
        self.reset_button = ttk.Button(root, text="Zerar Entradas/Saídas", command=self.zerar_entradas_saidas)
        self.reset_button.grid(row=5, column=0, padx=10, pady=5)

    def adicionar_transacao(self):
        # Adiciona uma nova transação
        descricao = self.descricao_entry.get()
        valor = self.valor_entry.get()
        tipo = self.tipo_var.get()

        if not descricao or not valor or not tipo:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            valor = float(valor)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")
            return

        self.transacao_id += 1  # Incrementa o ID da transação

        if tipo == "entrada":
            self.total_disponivel += valor
            self.entradas += valor
            tipo_simbolo = "+"
        else:
            self.total_disponivel -= valor
            self.saidas += valor
            tipo_simbolo = "-"

        self.entradas_label.config(text=f"Entradas\nR$ {self.entradas:.2f}")
        self.saidas_label.config(text=f"Saídas\nR$ {self.saidas:.2f}")
        self.total_label.config(text=f"Total\nR$ {self.total_disponivel:.2f}", foreground='red' if self.total_disponivel < 0 else 'black')

        # Adiciona a transação ao Treeview e à lista de transações
        self.transacoes.append((self.transacao_id, descricao, valor, tipo_simbolo))
        self.transacoes_tree.insert('', 'end', values=(self.transacao_id, descricao, f"R$ {valor:.2f}", tipo_simbolo))

        # Limpa os campos de entrada
        self.descricao_entry.delete(0, 'end')
        self.valor_entry.delete(0, 'end')
        self.tipo_var.set('')

    def deletar_transacao(self):
        # Deleta a transação selecionada
        selected_item = self.transacoes_tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Por favor, selecione uma transação para deletar.")
            return

        item = self.transacoes_tree.item(selected_item)
        transacao_id, descricao, valor_str, tipo = item['values']
        valor = float(valor_str.replace("R$", "").replace(",", "."))

        self.transacoes_tree.delete(selected_item)
        self.transacoes = [transacao for transacao in self.transacoes if transacao[0] != transacao_id]

        if tipo == "+":
            self.total_disponivel -= valor
            self.entradas -= valor
        else:
            self.total_disponivel += valor
            self.saidas -= valor

        self.entradas_label.config(text=f"Entradas\nR$ {self.entradas:.2f}")
        self.saidas_label.config(text=f"Saídas\nR$ {self.saidas:.2f}")
        self.total_label.config(text=f"Total\nR$ {self.total_disponivel:.2f}", foreground='red' if self.total_disponivel < 0 else 'black')

    def zerar_entradas_saidas(self):
        # Zera os valores de entradas e saídas
        self.entradas = 0.0
        self.saidas = 0.0
        self.entradas_label.config(text=f"Entradas\nR$ {self.entradas:.2f}")
        self.saidas_label.config(text=f"Saídas\nR$ {self.saidas:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ControleFinanceiro(root)
    root.mainloop()
