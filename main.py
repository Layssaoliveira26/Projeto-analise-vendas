#Importação de tabelas
import os #para interagir com o sistema operacional
import pandas as pd #para mexer com análise de dados
import plotly.express as px #para lidar com gráficos
print(pd.__version__)
#Guardar a lista dos arquivos
lista_arquivos = os.listdir("C:/Users/rahys/OneDrive/Desktop/Estudos Programação/Back End/Python/Projeto estudo/Projeto Básico de Programação Hashtag/Vendas-20241004T101833Z-001/vendas")
#Criar uma tabela vazia que irá armazenar os dados gerais
tabela_total = pd.DataFrame()
#Analisar os arquivos, fazer com que uma tabela receba ele e por fim adicionar essa tabela na tabela total
for arquivo in lista_arquivos:
    if "vendas" in arquivo.lower():
            print(f"Processando arquivo: {arquivo}")  # Verificar quais arquivos estão sendo processados
            tabela = pd.read_csv(f"C:/Users/rahys/OneDrive/Desktop/Estudos Programação/Back End/Python/Projeto estudo/Projeto Básico de Programação Hashtag/Vendas-20241004T101833Z-001/vendas/{arquivo}")
            # Normalizar os nomes das colunas para garantir consistência
            tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)
#for arquivo in lista_arquivos:
    #if "vendas" in arquivo.lower():
        #tabela = pd.read_csv(f"C:/Users/rahys/OneDrive/Desktop/Estudos Programação/Back End/Python/Projeto estudo/Projeto Básico de Programação Hashtag/Vendas-20241004T101833Z-001/vendas/{arquivo}")
        #tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)
        #tabela_total = pd.concat([tabela_total, tabela], ignore_index= True)
#Apresentar na tela essa tabela total
print(tabela_total)
#Observar produtos mais vendidos e criar uma tabela especifica para esses produtos
tabelas_produtos = tabela_total.groupby("Produto")["Quantidade Vendida"].sum().sort_values(ascending = True)
print(tabelas_produtos)
#Calcular o produto com maior faturamento
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto")["Faturamento"].sum().sort_values(ascending = True)
print(tabela_faturamento)
#Calcular a loja/cidade que mais faturou + montar um dashboard/gráfico
tabela_lojas = tabela_total.groupby("Loja")["Faturamento"].sum().sort_values(ascending = True)
print(tabela_lojas)
grafico = px.bar(tabela_lojas, x = tabela_lojas.index, y = "Faturamento")
grafico.show()