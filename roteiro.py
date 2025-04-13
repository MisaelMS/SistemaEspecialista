import tkinter as tk
from contextlib import nullcontext
from tkinter import ttk, messagebox
from datetime import datetime


def determinar_estacao(data):
    dia, mes, ano = map(int, data.split("/"))  # Separa o dia, mês e ano
    data_atual = datetime(ano, mes, dia)

    if datetime(ano, 3, 20) <= data_atual <= datetime(ano, 6, 20):
        return "Outono"
    elif datetime(ano, 6, 21) <= data_atual <= datetime(ano, 9, 22):
        return "Inverno"
    elif datetime(ano, 9, 23) <= data_atual <= datetime(ano, 12, 21):
        return "Primavera"
    else:
        return "Verão"


def recomendar():
    perfil = perfil_cb.get()
    destino = destino_cb.get()
    orcamento = orcamento_cb.get()     #parte onde recebe informação do menu dada pelo usuario
    dias = dias_entry.get()
    data_viagem = data_viagem_entry.get()     #Outono 20/03 a 20/06 - Inverno 21/06 a 22/09 - Primavera 23/09 a 21/12 - Verão 22/12 a 20/03

    if not perfil or not destino or not orcamento or not dias.isdigit() or not data_viagem:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
        return

    try:
        datetime.strptime(data_viagem, "%d/%m/%Y")  # Tenta converter a data
    except ValueError:
        messagebox.showerror("Erro", "Data inválida. Use o formato DD/MM/AAAA.")
        return

    dias = int(dias)
    estacao = determinar_estacao(data_viagem)
    resultado = ""

    if destino == "Litoral Catarinense":
        if estacao == "Verão":
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

        elif estacao == "Outono":
            if perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado = "Atividades: Praia tranquila em Palhoça"
                    elif dias <= 5:
                        resultado = "Atividades: Passeio em Porto Belo e visitas culturais"
                    else:
                        resultado = "Atividades: Passeios em Bombinhas e tour de barco"
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado = "Atividades: Parque aquático em Balneário Camboriú"
                    elif dias <= 5:
                        resultado = "Atividades: City tour em Balneário Camboriú e visita ao parque Beto Carrero"
                    else:
                        resultado = "Atividades: Pacote de atividades em praias e atrações culturais"
                else:
                    if dias <= 2:
                        resultado = "Atividades: Passeio privativo em resort à beira-mar"
                    elif dias <= 5:
                        resultado = "Atividades: Roteiro VIP com gastronomia e spa em praias exclusivas"
                    else:
                        resultado = "Atividades: Tour privado completo por praias e marinas"

            elif perfil == "Romântico":
                if orcamento == "Baixo":
                    resultado = "Atividades: Piquenique ao entardecer em praia tranquila"
                elif orcamento == "Médio":
                    resultado = "Atividades: Passeio de barco ao pôr do sol"
                else:
                    resultado = "Atividades: Jantar privado à beira-mar com passeio exclusivo de barco"

            elif perfil == "Aventureiro":
                if orcamento == "Baixo":
                    resultado = "Atividades: Trilha ecológica e passeio de barco em Bombinhas"
                elif orcamento == "Médio":
                    resultado = "Atividades: Mergulho e trilha costeira"
                else:
                    resultado = "Atividades: Kite surf e esportes radicais em Itajaí"

            else:
                resultado = "Atividades: Passeios exclusivos com serviços personalizados"

        elif estacao == "Inverno":
            if perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado = "Atividades: Praia de águas calmas e passeio de barco"
                    elif dias <= 5:
                        resultado = "Atividades: Visita ao Oceanic Aquarium e passeio pela região"
                    else:
                        resultado = "Atividades: Tour completo pela costa litorânea e atividades em parques"
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado = "Atividades: City tour em Balneário Camboriú e visita ao parque Beto Carrero"
                    elif dias <= 5:
                        resultado = "Atividades: Passeio em parques aquáticos e atividades culturais"
                    else:
                        resultado = "Atividades: Tour completo por praias e parques"

            elif perfil == "Romântico":
                if orcamento == "Baixo":
                    resultado = "Atividades: Caminhada ao pôr do sol e jantar simples à beira-mar"
                elif orcamento == "Médio":
                    resultado = "Atividades: Jantar ao pôr do sol e passeio de barco"
                else:
                    resultado = "Atividades: Passeio de barco exclusivo com jantar e champanhe"

            elif perfil == "Aventureiro":
                if orcamento == "Baixo":
                    resultado = "Atividades: Trilha e caminhada ecológica"
                elif orcamento == "Médio":
                    resultado = "Atividades: Mergulho guiado e esportes radicais"
                else:
                    resultado = "Atividades: Kite surf e esportes radicais em Itajaí"

            else:
                resultado = "Atividades: Passeios exclusivos com serviços personalizados"

        elif estacao == "Primavera":
            if perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado = "Atividades: Praia com infraestrutura simples em Itapema"
                    elif dias <= 5:
                        resultado = "Atividades: Passeio de barco e visita ao Oceanic Aquarium"
                    else:
                        resultado = "Atividades: Tour por Bombinhas e Penha"
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado = "Atividades: Passeio de barco e visita a praias próximas"
                    elif dias <= 5:
                        resultado = "Atividades: City tour e visita ao parque Beto Carrero"
                    else:
                        resultado = "Atividades: Pacote completo com praias e atividades culturais"
                else:
                    if dias <= 2:
                        resultado = "Atividades: Passeio exclusivo em resort e atividades litorâneas"
                    elif dias <= 5:
                        resultado = "Atividades: Roteiro VIP com gastronomia e spa"
                    else:
                        resultado = "Atividades: Tour completo por praias exclusivas"

            elif perfil == "Romântico":
                if orcamento == "Baixo":
                    resultado = "Atividades: Piquenique romântico ao pôr do sol"
                elif orcamento == "Médio":
                    resultado = "Atividades: Passeio de barco e jantar típico à beira-mar"
                else:
                    resultado = "Atividades: Passeio de barco privativo com jantar exclusivo"

            elif perfil == "Aventureiro":
                if orcamento == "Baixo":
                    resultado = "Atividades: Mergulho e trilha ecológica"
                elif orcamento == "Médio":
                    resultado = "Atividades: Mergulho guiado e trilha costeira"
                else:
                    resultado = "Atividades: Kite surf e esportes radicais"

            else:
                resultado = "Atividades: Passeios exclusivos com serviços personalizados"

    elif destino == "Serra Catarinense":
        if estacao == "Verão":
            if perfil == "Romântico":
                if orcamento == "Baixo":
                    resultado = "Atividades: Mirante da Serra do Rio do Rastro com lanche artesanal."
                elif orcamento == "Médio":
                    resultado = "Atividades: Jantar romântico e visita a vinícola."
                else:
                    resultado = "Atividades: Spa com vista para serra e passeio privativo."

            elif perfil == "Aventureiro":
                if dias <= 2:
                    resultado = "Atividades: Trilha na Pedra Furada."
                elif dias <= 5:
                    resultado = "Atividades: Canyoning e visita a cavernas de Urubici."
                else:
                    resultado = "Atividades: Circuito de trilhas e esportes de aventura."

            elif perfil == "Familiar":
                resultado = "Atividades: Passeio de trator, visita à neve e parque temático serrano."

            else:  # Perfil Luxo
                resultado = "Atividades: Degustação de vinhos premium, piquenique com queijos artesanais."

        elif estacao == "Outono":
            if perfil == "Romântico":
                if orcamento == "Baixo":
                    resultado = "Atividades: Passeio no mirante do Morro da Igreja e lanche artesanal."
                elif orcamento == "Médio":
                    resultado = "Atividades: Jantar romântico em pousada e visita a vinícola."
                else:
                    resultado = "Atividades: Jantar de luxo com vista panorâmica para a serra e passeios exclusivos."

            elif perfil == "Aventureiro":
                if dias <= 2:
                    resultado = "Atividades: Trilha no Parque Nacional de São Joaquim."
                elif dias <= 5:
                    resultado = "Atividades: Escalada e visita a cavernas de Urubici."
                else:
                    resultado = "Atividades: Circuito de trilhas de aventura e visita aos cânions da serra."

            elif perfil == "Familiar":
                resultado = "Atividades: Passeio guiado pelo Parque Nacional de São Joaquim e visita a museus."

            else:  # Perfil Luxo
                resultado = "Atividades: Experiência VIP com degustação de vinhos e jantar gourmet."

        elif estacao == "Inverno":
            if perfil == "Romântico":
                if orcamento == "Baixo":
                    resultado = "Atividades: Visita ao Mirante da Serra do Rio do Rastro com lanche típico."
                elif orcamento == "Médio":
                    resultado = "Atividades: Jantar romântico e visita a vinícola com degustação de vinhos."
                else:
                    resultado = "Atividades: Passeio de luxo pela serra com spa e jantar em restaurante sofisticado."

            elif perfil == "Aventureiro":
                if dias <= 2:
                    resultado = "Atividades: Trilha na Pedra Furada."
                elif dias <= 5:
                    resultado = "Atividades: Canyoning e visita às cavernas de Urubici."
                else:
                    resultado = "Atividades: Circuito de trilhas e esportes de aventura."

            elif perfil == "Familiar":
                resultado = "Atividades: Passeio de trator, visita à neve e parque temático serrano."

            else:  # Perfil Luxo
                resultado = "Atividades: Degustação de vinhos premium, piquenique com queijos artesanais e experiência exclusiva."

        elif estacao == "Primavera":
            if perfil == "Romântico":
                if orcamento == "Baixo":
                    resultado = "Atividades: Caminhada pelos jardins e mirantes com lanche artesanal."
                elif orcamento == "Médio":
                    resultado = "Atividades: Jantar romântico em restaurante com vista e visita a vinícola."
                else:
                    resultado = "Atividades: Passeio de luxo pelas flores da primavera e jantar gourmet."

            elif perfil == "Aventureiro":
                if dias <= 2:
                    resultado = "Atividades: Trilha no Parque Nacional de São Joaquim."
                elif dias <= 5:
                    resultado = "Atividades: Escalada e visita a cavernas de Urubici."
                else:
                    resultado = "Atividades: Circuito de trilhas de aventura e visita aos cânions da serra."

            elif perfil == "Familiar":
                resultado = "Atividades: Passeio no Parque Nacional de São Joaquim e visita a cachoeiras."

            else:  # Perfil Luxo
                resultado = "Atividades: Degustação de vinhos premium com flores da estação e piquenique exclusivo."

    elif destino == "Cidades Históricas":
        if estacao == "Verão":
            if perfil == "Aventureiro":
                if dias <= 3:
                    resultado = "Atividades: Roteiro de bike entre museus e ruínas em Laguna."
                else:
                    resultado = "Atividades: Roteiro de bike, visita a museus históricos e ruínas em Laguna com parada para almoço típico."
            elif perfil == "Romântico":
                if dias <= 3:
                    resultado = "Atividades: Caminhada ao pôr do sol e jantar típico colonial em Blumenau."
                else:
                    resultado = "Atividades: Caminhada ao pôr do sol, visita a centros históricos e jantar típico colonial em Blumenau."
            elif perfil == "Familiar":
                if dias <= 3:
                    resultado = "Atividades: Passeio guiado por centros históricos em São Francisco do Sul e visita ao Museu Nacional do Mar."
                else:
                    resultado = "Atividades: Passeio guiado por centros históricos em São Francisco do Sul, visita ao Museu Nacional do Mar e ao Forte Marechal Luz."
            else:  # Perfil Luxo
                if dias <= 3:
                    resultado = "Atividades: City tour VIP com visitas exclusivas aos museus históricos e jantares em restaurantes renomados de Florianópolis."
                else:
                    resultado = "Atividades: City tour VIP com visitas exclusivas aos museus históricos, jantares renomados e experiências culturais personalizadas."

        elif estacao == "Outono":
            if perfil == "Aventureiro":
                if dias <= 3:
                    resultado = "Atividades: Roteiro de bike e visita às ruínas de São João Batista e Laguna."
                else:
                    resultado = "Atividades: Roteiro de bike, visita a museus históricos e exploração de ruínas em Laguna e São João Batista."
            elif perfil == "Romântico":
                if dias <= 3:
                    resultado = "Atividades: Caminhada ao pôr do sol, visita a igrejas históricas e jantar colonial em Joinville."
                else:
                    resultado = "Atividades: Caminhada ao pôr do sol, visita a igrejas históricas e jantar colonial com show folclórico em Joinville."
            elif perfil == "Familiar":
                if dias <= 3:
                    resultado = "Atividades: Passeio guiado por centros históricos de São Francisco do Sul e visita a museus."
                else:
                    resultado = "Atividades: Passeio guiado por centros históricos de São Francisco do Sul, visita a museus e caminhada pela orla."
            else:  # Perfil Luxo
                if dias <= 3:
                    resultado = "Atividades: City tour VIP em Blumenau com experiências culturais exclusivas e jantar gourmet."
                else:
                    resultado = "Atividades: City tour VIP, visitas culturais exclusivas e jantar gourmet com vista panorâmica em Blumenau."

        elif estacao == "Inverno":
            if perfil == "Aventureiro":
                if dias <= 3:
                    resultado = "Atividades: Roteiro de bike e visitas a museus históricos em São José e Laguna."
                else:
                    resultado = "Atividades: Roteiro de bike, visitas a museus e ruínas históricas em São José, Laguna e Joinville."
            elif perfil == "Romântico":
                if dias <= 3:
                    resultado = "Atividades: Caminhada no centro histórico de Florianópolis, visita ao Mercado Público e jantar à luz de velas."
                else:
                    resultado = "Atividades: Caminhada pelo centro histórico de Florianópolis, visita a centros históricos e jantar à luz de velas em restaurante exclusivo."
            elif perfil == "Familiar":
                if dias <= 3:
                    resultado = "Atividades: Passeio guiado pelo centro histórico de São Francisco do Sul, visita a museus e caminhada pela praia."
                else:
                    resultado = "Atividades: Passeio guiado, visita a museus e caminhada pela praia, com parada para almoço em restaurantes locais."
            else:  # Perfil Luxo
                if dias <= 3:
                    resultado = "Atividades: City tour VIP por Florianópolis, incluindo visitas a museus e jantares exclusivos."
                else:
                    resultado = "Atividades: City tour VIP, visita a museus e jantares exclusivos com experiências culturais em Florianópolis."

        elif estacao == "Primavera":
            if perfil == "Aventureiro":
                resultado = "Atividades: Passeio de bike entre os museus e ruas floridas de Blumenau."
            elif perfil == "Romântico":
                resultado = "Atividades: Passeio romântico ao pôr do sol pelos centros históricos e jantar típico."
            elif perfil == "Familiar":
                resultado = "Atividades: Passeio guiado por centros históricos com foco em atividades ao ar livre."
            else:  # Perfil Luxo
                resultado = "Atividades: City tour VIP com experiências culturais e jantares exclusivos em áreas floridas."

    elif destino == "Turismo Rural":
        if estacao == "Verão":
            if perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 3:
                        resultado = "Atividades: Fazenda com ordenha, trilhas leves e alimentação caseira."
                    else:
                        resultado = "Atividades: Fazenda com ordenha, trilhas leves, alimentação caseira e visita a fazendas próximas."
                elif orcamento == "Médio":
                    if dias <= 3:
                        resultado = "Atividades: Cavalgada, plantio e colheita de alimentos."
                    else:
                        resultado = "Atividades: Cavalgada, plantio, colheita e visita a vinícolas."
                else:
                    if dias <= 3:
                        resultado = "Atividades: Roteiro completo com vivência rural e gastronomia típica."
                    else:
                        resultado = "Atividades: Roteiro completo com vivência rural, gastronomia típica e hospedagem em fazendas de luxo."
            elif perfil == "Aventureiro":
                if dias <= 3:
                    resultado = "Atividades: Trilha rural, rafting e rapel."
                else:
                    resultado = "Atividades: Trilha rural, rafting, rapel e expedição em regiões selvagens."
            elif perfil == "Romântico":
                if dias <= 3:
                    resultado = "Atividades: Piquenique ao entardecer, passeio a cavalo e fogueira noturna."
                else:
                    resultado = "Atividades: Piquenique ao entardecer, passeio a cavalo, fogueira noturna e jantar exclusivo à luz de velas."
            else:  # Perfil "Luxo"
                if dias <= 3:
                    resultado = "Atividades: Degustação exclusiva e experiências agroecológicas."
                else:
                    resultado = "Atividades: Experiência rural exclusiva, incluindo visitas a vinícolas, gastronomia de luxo e hospedagem VIP."

        elif estacao == "Outono":
            if perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 3:
                        resultado = "Atividades: Colheita de frutas, ordenha e passeio por fazendas."
                    else:
                        resultado = "Atividades: Colheita de frutas, ordenha e passeio por fazendas, com visita a mercados locais."
                elif orcamento == "Médio":
                    if dias <= 3:
                        resultado = "Atividades: Plantio de hortas e visita a vinícolas."
                    else:
                        resultado = "Atividades: Plantio de hortas, visita a vinícolas e tour por fazendas históricas."
                else:
                    if dias <= 3:
                        resultado = "Atividades: Turismo rural de luxo, com experiências em vinícolas e gastronomia."
                    else:
                        resultado = "Atividades: Turismo rural de luxo, com estada em fazendas exclusivas e gastronomia gourmet."
            elif perfil == "Aventureiro":
                if dias <= 3:
                    resultado = "Atividades: Trilha e visita a fazendas orgânicas."
                else:
                    resultado = "Atividades: Trilha em regiões remotas e exploração de fazendas sustentáveis."
            elif perfil == "Romântico":
                if dias <= 3:
                    resultado = "Atividades: Passeio romântico por vinhedos e piquenique ao ar livre."
                else:
                    resultado = "Atividades: Passeio romântico por vinhedos, piquenique ao ar livre e jantar exclusivo."
            else:  # Perfil "Luxo"
                if dias <= 3:
                    resultado = "Atividades: Experiência rural VIP com gastronomia exclusiva e tratamentos de spa."
                else:
                    resultado = "Atividades: Turismo rural VIP com estada em pousadas exclusivas, gastronomia de luxo e massagens relaxantes."

        elif estacao == "Inverno":
            if perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 3:
                        resultado = "Atividades: Passeio por fazendas e trilhas leves."
                    else:
                        resultado = "Atividades: Passeio por fazendas, trilhas leves e aulas de culinária rural."
                elif orcamento == "Médio":
                    if dias <= 3:
                        resultado = "Atividades: Aulas de culinária rural e visita a fazendas históricas."
                    else:
                        resultado = "Atividades: Aulas de culinária, visita a fazendas históricas e degustação de produtos locais."
                else:
                    if dias <= 3:
                        resultado = "Atividades: Experiência gourmet em fazendas de luxo com hospedagem."
                    else:
                        resultado = "Atividades: Experiência gourmet de luxo, com hospedagem em fazendas e jantares de 5 estrelas."
            elif perfil == "Aventureiro":
                if dias <= 3:
                    resultado = "Atividades: Trilha de inverno e esportes radicais em fazendas."
                else:
                    resultado = "Atividades: Trilha de inverno, esportes radicais e exploração em regiões montanhosas."
            elif perfil == "Romântico":
                if dias <= 3:
                    resultado = "Atividades: Passeio a cavalo na neve e jantares românticos em fazendas."
                else:
                    resultado = "Atividades: Passeio a cavalo na neve, jantares românticos em fazendas e tratamentos de spa."
            else:  # Perfil "Luxo"
                if dias <= 3:
                    resultado = "Atividades: Turismo rural de luxo com estadia em pousadas exclusivas."
                else:
                    resultado = "Atividades: Turismo rural de luxo com estadia em pousadas exclusivas, gastronomia requintada e experiências personalizadas."

        elif estacao == "Primavera":
            if perfil == "Familiar":
                if orcamento == "Baixo":
                    resultado = "Atividades: Passeio no campo com caminhada e piquenique com produtos da estação."
                elif orcamento == "Médio":
                    resultado = "Atividades: Passeio de cavalo e plantio de flores com a família."
                else:
                    resultado = "Atividades: Vivência rural com foco em gastronomia orgânica e experiências em hortas."

            elif perfil == "Aventureiro":
                resultado = "Atividades: Trilhas no campo e atividades de plantio e colheita."

            elif perfil == "Romântico":
                resultado = "Atividades: Passeio a cavalo, piquenique nas flores e noite de fogueira."

            else:  # Perfil Luxo
                resultado = "Atividades: Degustação de vinhos, culinária local e piquenique em um campo florido."

    elif destino == "Vale Europeu":
        if estacao == "Inverno":
            if perfil == "Aventureiro":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Caminhadas curtas em trilhas locais com baixo custo."
                    elif dias <= 5:
                        resultado += "Atividades: Trilhas e camping em parques acessíveis."
                    else:
                        resultado += "Atividades: Circuito de trilhas econômicas em diversas cidades."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeio guiado por montanhas e hospedagem em pousada."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito de trilhas com serviços guiados e estadia confortável."
                    else:
                        resultado += "Atividades: Pacote completo com trilhas e atividades ao ar livre."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Caminhadas premium com guias particulares."
                    elif dias <= 5:
                        resultado += "Atividades: Trilhas exclusivas com estadia em hotéis luxuosos."
                    else:
                        resultado += "Atividades: Roteiro personalizado de aventuras com serviços VIP."

            elif perfil == "Romântico":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Jantar em restaurante local e visita rápida a pontos turísticos."
                    elif dias <= 5:
                        resultado += "Atividades: Pacote econômico com passeios culturais e hospedagem aconchegante."
                    else:
                        resultado += "Atividades: Tour por vilarejos românticos com baixo custo."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Estadia em pousadas aconchegantes com jantar romântico."
                    elif dias <= 5:
                        resultado += "Atividades: Passeios culturais com estadia em pousadas confortáveis."
                    else:
                        resultado += "Atividades: Tour completo por vinícolas e locais históricos."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Hospedagem luxuosa com jantar exclusivo."
                    elif dias <= 5:
                        resultado += "Atividades: Pacote romântico premium com experiências particulares."
                    else:
                        resultado += "Atividades: Tour VIP por locais exclusivos e degustações refinadas."

            elif perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Visita a museus com entrada gratuita e parques locais."
                    elif dias <= 5:
                        resultado += "Atividades: Roteiro cultural econômico com atrações para crianças."
                    else:
                        resultado += "Atividades: Pacote familiar com atividades acessíveis em várias cidades."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios culturais com estadia em pousadas confortáveis."
                    elif dias <= 5:
                        resultado += "Atividades: Roteiro completo com atividades interativas para crianças."
                    else:
                        resultado += "Atividades: Experiências completas em fazendas e museus interativos."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Pacote VIP com atrações exclusivas para a família."
                    elif dias <= 5:
                        resultado += "Atividades: Experiências personalizadas com hospedagem de luxo."
                    else:
                        resultado += "Atividades: Tour completo com atrações exclusivas e serviços premium."

            elif perfil == "Luxo":
                if orcamento == "Baixo":
                    resultado += "Atividades: Perfil 'Luxo' exige orçamento elevado."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Day-use em propriedades luxuosas com serviços limitados."
                    elif dias <= 5:
                        resultado += "Atividades: Roteiro luxuoso com algumas opções exclusivas."
                    else:
                        resultado += "Atividades: Experiências selecionadas em hotéis confortáveis."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Hospedagem em resort cinco estrelas com spa e gastronomia."
                    elif dias <= 5:
                        resultado += "Atividades: Pacote completo de experiências VIP."
                    else:
                        resultado += "Atividades: Tour personalizado por vinícolas e resorts exclusivos."

        elif estacao == "Primavera":
            if perfil == "Aventureiro":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Trilhas curtas em jardins floridos com entrada gratuita."
                    elif dias <= 5:
                        resultado += "Atividades: Ecoturismo acessível com passeios guiados em parques naturais."
                    else:
                        resultado += "Atividades: Circuito de trilhas e cachoeiras em áreas floridas."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios guiados com estadia em pousadas confortáveis."
                    elif dias <= 5:
                        resultado += "Atividades: Ecoturismo completo em parques e regiões floridas."
                    else:
                        resultado += "Atividades: Pacote completo de aventuras em áreas de preservação ambiental."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Passeios exclusivos em jardins privados com guias especializados."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito VIP em áreas floridas e estadia luxuosa."
                    else:
                        resultado += "Atividades: Tour premium com hospedagem de luxo e experiências personalizadas."

            elif perfil == "Romântico":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Piquenique em campos floridos e jantar em restaurante local."
                    elif dias <= 5:
                        resultado += "Atividades: Passeios culturais e hospedagem econômica em pousadas aconchegantes."
                    else:
                        resultado += "Atividades: Tour por vilarejos românticos e festivais locais com baixo custo."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios por jardins e estadia em pousadas confortáveis."
                    elif dias <= 5:
                        resultado += "Atividades: Pacote romântico com visitas guiadas a locais floridos."
                    else:
                        resultado += "Atividades: Tour completo por áreas floridas e vinícolas."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Hospedagem luxuosa com piquenique exclusivo em jardim privado."
                    elif dias <= 5:
                        resultado += "Atividades: Experiências românticas VIP em locais floridos."
                    else:
                        resultado += "Atividades: Tour exclusivo por vinícolas e jardins privados com serviços premium."

            elif perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Feira local com atividades para crianças e adultos."
                    elif dias <= 5:
                        resultado += "Atividades: Roteiro cultural em parques naturais e centros interativos."
                    else:
                        resultado += "Atividades: Experiências completas com atrações econômicas para toda a família."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios culturais e hospedagem confortável."
                    elif dias <= 5:
                        resultado += "Atividades: Roteiro completo com atividades interativas para crianças e adultos."
                    else:
                        resultado += "Atividades: Pacote familiar com experiências floridas e hospedagem em fazendas."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Passeios exclusivos com serviços premium para a família."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito VIP com atrações personalizadas para todas as idades."
                    else:
                        resultado += "Atividades: Experiências completas com hospedagem luxuosa e atrações exclusivas."

            elif perfil == "Luxo":
                if orcamento == "Baixo":  # O perfil "Luxo" não se aplica a orçamentos baixos
                    resultado += "Atividades: O perfil 'Luxo' exige orçamento mais elevado."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Day-use em propriedades luxuosas com serviços limitados."
                    elif dias <= 5:
                        resultado += "Atividades: Passeios exclusivos com hospedagem confortável."
                    else:
                        resultado += "Atividades: Tour de luxo em jardins e vinícolas com conforto e exclusividade."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Hospedagem em resort cinco estrelas e passeios privados."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito VIP em locais floridos com experiências exclusivas."
                    else:
                        resultado += "Atividades: Tour completo de luxo com atrações personalizadas e serviços premium."


        elif estacao == "Verão":
            if perfil == "Aventureiro":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Caminhadas curtas e aventuras em cachoeiras."
                    elif dias <= 5:
                        resultado += "Atividades: Trilhas e camping em áreas de rios e lagos."
                    else:
                        resultado += "Atividades: Roteiro completo de aventuras aquáticas e esportes ao ar livre."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios guiados com atividades aquáticas moderadas."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito completo de esportes aquáticos com estadia confortável."
                    else:
                        resultado += "Atividades: Pacote completo de aventuras ao ar livre com conforto."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Passeios exclusivos em cachoeiras com serviços premium."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito VIP de esportes aquáticos e hospedagem luxuosa."
                    else:
                        resultado += "Atividades: Experiência completa com aventuras exclusivas e serviços personalizados."

            elif perfil == "Romântico":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Passeio ao pôr do sol em praias e jantar econômico."
                    elif dias <= 5:
                        resultado += "Atividades: Hospedagem em pousadas simples com passeios românticos."
                    else:
                        resultado += "Atividades: Tour por praias paradisíacas e vilarejos costeiros com baixo custo."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios por mirantes costeiros e estadia confortável."
                    elif dias <= 5:
                        resultado += "Atividades: Pacote romântico com experiências exclusivas ao ar livre."
                    else:
                        resultado += "Atividades: Tour completo por praias e locais paradisíacos com conforto."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Hospedagem em resort de luxo com jantar exclusivo e spa."
                    elif dias <= 5:
                        resultado += "Atividades: Passeios VIP por praias e experiências românticas personalizadas."
                    else:
                        resultado += "Atividades: Tour exclusivo por ilhas e marinas com serviços premium."

            elif perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Visitas a praias acessíveis e parques aquáticos simples."
                    elif dias <= 5:
                        resultado += "Atividades: Roteiro econômico com atrações para todas as idades."
                    else:
                        resultado += "Atividades: Pacote completo com visitas a praias e parques acessíveis."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios culturais e diversão em praias confortáveis."
                    elif dias <= 5:
                        resultado += "Atividades: Roteiro completo com atrações interativas para toda a família."
                    else:
                        resultado += "Atividades: Pacote familiar com visitas a locais diversos e hospedagem confortável."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Day-use em resorts com atrações exclusivas para a família."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito VIP com atividades personalizadas para todas as idades."
                    else:
                        resultado += "Atividades: Experiências completas com hospedagem luxuosa e serviços premium."

            elif perfil == "Luxo":
                if orcamento == "Baixo":  # O perfil "Luxo" não se aplica a orçamentos baixos
                    resultado += "Atividades: O perfil 'Luxo' exige orçamento mais elevado."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios moderadamente luxuosos com hospedagem confortável."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito de luxo com serviços personalizados em praias."
                    else:
                        resultado += "Atividades: Tour VIP com experiências exclusivas e hospedagem refinada."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Hospedagem em resort cinco estrelas com spa e atrações privadas."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito completo de luxo com experiências exclusivas."
                    else:
                        resultado += "Atividades: Tour personalizado por ilhas e locais de alto padrão."

            # Inclui outras condições para os perfis "Romântico", "Familiar" e "Luxo".

        elif estacao == "Outono":
            if perfil == "Aventureiro":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Caminhadas curtas em trilhas com folhas caindo."
                    elif dias <= 5:
                        resultado += "Atividades: Passeios guiados em parques com paisagens de outono."
                    else:
                        resultado += "Atividades: Roteiro completo de trilhas em regiões com clima ameno."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios em parques com serviços guiados moderados."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito completo de trilhas em áreas preservadas."
                    else:
                        resultado += "Atividades: Pacote com hospedagem confortável e aventuras guiadas."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Passeios exclusivos em parques com guias particulares."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito VIP em áreas arborizadas e estadia luxuosa."
                    else:
                        resultado += "Atividades: Experiência completa em regiões exclusivas com serviços personalizados."

            elif perfil == "Romântico":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Passeio breve por vilas históricas com café artesanal."
                    elif dias <= 5:
                        resultado += "Atividades: Pacote cultural com hospedagem econômica e jantar ao ar livre."
                    else:
                        resultado += "Atividades: Roteiro por vilarejos charmosos com festivais locais."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Jantar romântico em restaurante com vista para paisagens de outono."
                    elif dias <= 5:
                        resultado += "Atividades: Passeios por vilarejos floridos e estadia em pousadas confortáveis."
                    else:
                        resultado += "Atividades: Tour completo com experiências exclusivas em vinícolas e locais culturais."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Hospedagem luxuosa com jantar exclusivo e passeio privado por vilas."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito VIP em locais arborizados com experiências exclusivas."
                    else:
                        resultado += "Atividades: Tour completo com hospedagem em resorts de luxo e passeios personalizados."

            elif perfil == "Familiar":
                if orcamento == "Baixo":
                    if dias <= 2:
                        resultado += "Atividades: Visitas a parques naturais com atividades para crianças."
                    elif dias <= 5:
                        resultado += "Atividades: Passeios econômicos em museus e centros interativos."
                    else:
                        resultado += "Atividades: Roteiro completo com atrações acessíveis para toda a família."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios em fazendas com estadia confortável para famílias."
                    elif dias <= 5:
                        resultado += "Atividades: Roteiro cultural com atividades interativas para todas as idades."
                    else:
                        resultado += "Atividades: Pacote completo com experiências interativas em parques e museus."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Day-use em propriedades exclusivas com atrações para crianças e adultos."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito VIP com estadia luxuosa e atividades personalizadas."
                    else:
                        resultado += "Atividades: Tour completo com hospedagem premium e serviços exclusivos."

            elif perfil == "Luxo":
                if orcamento == "Baixo":  # Ajuste: o perfil "Luxo" não se aplica a orçamento baixo
                    resultado += "Atividades: Perfil 'Luxo' exige orçamento mais elevado."
                elif orcamento == "Médio":
                    if dias <= 2:
                        resultado += "Atividades: Passeios moderadamente luxuosos com hospedagem confortável."
                    elif dias <= 5:
                        resultado += "Atividades: Experiências de luxo com opções personalizadas em parques e vilas."
                    else:
                        resultado += "Atividades: Circuito completo de luxo com estadia confortável e atrações exclusivas."
                else:  # Alto
                    if dias <= 2:
                        resultado += "Atividades: Hospedagem em resort cinco estrelas com passeios privados."
                    elif dias <= 5:
                        resultado += "Atividades: Circuito VIP com serviços exclusivos em regiões arborizadas."
                    else:
                        resultado += "Atividades: Tour completo de luxo com atrações personalizadas e hospedagem refinada."

    #um montão de else if para distinguir o resultado dada pelas informações do usuario

    resultado_label.config(text=resultado)

janela = tk.Tk()
janela.title("Sistema Especialista de Roteiros em SC")

perfil_cb = ttk.Combobox(janela, values=["Aventureiro", "Romântico", "Familiar", "Luxo"], state="readonly")
destino_cb = ttk.Combobox(janela, values=["Serra Catarinense", "Litoral Catarinense", "Cidades Históricas", "Turismo Rural", "Vale Europeu"], state="readonly")
orcamento_cb = ttk.Combobox(janela, values=["Baixo", "Médio", "Alto"], state="readonly")
dias_entry = tk.Entry(janela)

data_viagem_entry = tk.Entry(janela)
tk.Label(janela, text="Data da Viagem:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
data_viagem_entry.grid(row=4, column=1, padx=10, pady=5)

labels = ["Perfil do Viajante:", "Destino Preferido:", "Orçamento:", "Dias de Viagem:"]
widgets = [perfil_cb, destino_cb, orcamento_cb, dias_entry]

for i, (label, widget) in enumerate(zip(labels, widgets)):
    tk.Label(janela, text=label).grid(row=i, column=0, sticky="w", padx=10, pady=5)                                          #Parte onde fica o menu 
    widget.grid(row=i, column=1, padx=10, pady=5)

tk.Button(janela, text="Recomendar Roteiro", command=recomendar).grid(row=6, column=0, columnspan=2, pady=10)

resultado_label = tk.Label(janela, text="", wraplength=500, justify="left")
resultado_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()



# FUNCIONA KRLLLLL