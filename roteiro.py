import tkinter as tk
from tkinter import ttk, messagebox

def recomendar():
    perfil = perfil_cb.get()
    destino = destino_cb.get()
    orcamento = orcamento_cb.get()     #parte onde recebe informação do menu dada pelo usuario
    dias = dias_entry.get()

    if not perfil or not destino or not orcamento or not dias.isdigit():
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
        return

    dias = int(dias)
    resultado = ""

    if destino == "Litoral Catarinense":
        if perfil == "Familiar":
            if orcamento == "Baixo":
                if dias <= 2:
                    resultado = "Atividades: Praia de Itapema com infraestrutura gratuita"
                elif dias <= 5:
                    resultado = "Atividades: Praia do Estaleiro e visita ao Oceanic Aquarium"
                else:
                    resultado = "Atividades: Tour por praias de Bombinhas e parque em Penha"
            elif orcamento == "Médio":
                if dias <= 2:
                    resultado = "Atividades: Parque aquático em Gaspar"
                elif dias <= 5:
                    resultado = "Atividades: City tour em Balneário Camboriú e parque Beto Carrero"
                else:
                    resultado = "Atividades: Pacote com praias, parques e atrações culturais"
            else:
                if dias <= 2:
                    resultado = "Atividades: Day-use em resort e beach club"
                elif dias <= 5:
                    resultado = "Atividades: Roteiro VIP com spa e gastronomia litorânea"
                else:
                    resultado = "Atividades: Tour completo por praias exclusivas e marinas"

        elif perfil == "Romântico":
            if orcamento == "Baixo":
                resultado = "Atividades: Praia deserta e piquenique ao entardecer"
            elif orcamento == "Médio":
                resultado = "Atividades: Passeio ao pôr do sol com jantar à beira-mar"
            else:
                resultado = "Atividades: Passeio de barco privativo com jantar exclusivo"

        elif perfil == "Aventureiro":
            if orcamento == "Baixo":
                resultado = "Atividades: Trilha ecológica e snorkel em Bombinhas"
            elif orcamento == "Médio":
                resultado = "Atividades: Mergulho guiado e trilha costeira"
            else:
                resultado = "Atividades: Kite surf e esportes radicais em Itajaí"

        else:
            resultado = "Atividades: Passeios exclusivos com serviços personalizados"

    elif destino == "Serra Catarinense":
        if perfil == "Romântico":
            if orcamento == "Baixo":
                resultado = "Atividades: Mirante da Serra do Rio do Rastro com lanche artesanal"
            elif orcamento == "Médio":
                resultado = "Atividades: Jantar romântico e visita a vinícola"
            else:
                resultado = "Atividades: Spa com vista para serra e passeio privativo"

        elif perfil == "Aventureiro":
            if dias <= 2:
                resultado = "Atividades: Trilha na Pedra Furada"
            elif dias <= 5:
                resultado = "Atividades: Canyoning e visita a cavernas de Urubici"
            else:
                resultado = "Atividades: Circuito de trilhas e esportes de aventura"

        elif perfil == "Familiar":
            resultado = "Atividades: Passeio de trator, visita à neve e parque temático serrano"

        else:
            resultado = "Atividades: Degustação de vinhos premium, piquenique com queijos artesanais"

    elif destino == "Cidades Históricas":
        if perfil == "Aventureiro":
            resultado = "Atividades: Roteiro de bike entre museus e ruínas em Laguna"
        elif perfil == "Romântico":
            resultado = "Atividades: Caminhada ao pôr do sol e jantar típico colonial"
        elif perfil == "Familiar":
            resultado = "Atividades: Passeio guiado por centros históricos em São Francisco do Sul"
        else:
            resultado = "Atividades: City tour VIP com experiências culturais exclusivas"

    elif destino == "Turismo Rural":
        if perfil == "Familiar":
            if orcamento == "Baixo":
                resultado = "Atividades: Fazenda com ordenha, trilhas leves e alimentação caseira"
            elif orcamento == "Médio":
                resultado = "Atividades: Cavalgada, plantio e colheita de alimentos"
            else:
                resultado = "Atividades: Roteiro completo com vivência rural e gastronomia típica"

        elif perfil == "Aventureiro":
            resultado = "Atividades: Trilha rural, rafting e rapel"

        elif perfil == "Romântico":
            resultado = "Atividades: Piquenique ao entardecer, passeio a cavalo e fogueira noturna"        

        else:
            resultado = "Atividades: Degustação exclusiva e experiências agroecológicas"                          #um montão de else if para distinguir o resultado dada pelas informações do usuario

    resultado_label.config(text=resultado)

janela = tk.Tk()
janela.title("Sistema Especialista de Roteiros em SC")

perfil_cb = ttk.Combobox(janela, values=["Aventureiro", "Romântico", "Familiar", "Luxo"], state="readonly")
destino_cb = ttk.Combobox(janela, values=["Serra Catarinense", "Litoral Catarinense", "Cidades Históricas", "Turismo Rural"], state="readonly")
orcamento_cb = ttk.Combobox(janela, values=["Baixo", "Médio", "Alto"], state="readonly")
dias_entry = tk.Entry(janela)

labels = ["Perfil do Viajante:", "Destino Preferido:", "Orçamento:", "Dias de Viagem:"]
widgets = [perfil_cb, destino_cb, orcamento_cb, dias_entry]

for i, (label, widget) in enumerate(zip(labels, widgets)):
    tk.Label(janela, text=label).grid(row=i, column=0, sticky="w", padx=10, pady=5)                                          #Parte onde fica o menu 
    widget.grid(row=i, column=1, padx=10, pady=5)

tk.Button(janela, text="Recomendar Roteiro", command=recomendar).grid(row=4, column=0, columnspan=2, pady=10)

resultado_label = tk.Label(janela, text="", wraplength=500, justify="left")
resultado_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()



# FUNCIONA KRLLLLL