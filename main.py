from flask import Flask, render_template
import os  # Para interagir com o sistema operacional
import pandas as pd  # Para análise de dados
import plotly.express as px  # Para gerar gráficos
import plotly.io as pio  # Para salvar o gráfico como HTML

app = Flask(__name__)

@app.route('/')
def index():
    # Guardar a lista dos arquivos
    lista_arquivos = os.listdir("C:\\Users\\rahys\\OneDrive\\Desktop\\Estudos Programação\\Back End\\Python\\Projeto estudo\\Projeto Básico de Programação Hashtag\\Base_dados\\Vendas")

    # Criar uma tabela vazia que irá armazenar os dados gerais
    tabela_total = pd.DataFrame()

    # Analisar os arquivos e adicionar os dados à tabela total
    for arquivo in lista_arquivos:
        if "vendas" in arquivo.lower():
            tabela = pd.read_csv(f"C:\\Users\\rahys\\OneDrive\\Desktop\\Estudos Programação\\Back End\\Python\\Projeto estudo\\Projeto Básico de Programação Hashtag\\Base_dados\\Vendas\\{arquivo}")
            tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)

    # Exibir a tabela total
    print(tabela_total)

    # Criar uma tabela específica de produtos mais vendidos
    tabelas_produtos = tabela_total.groupby("Produto")["Quantidade Vendida"].sum().sort_values(ascending=True)
    print(tabelas_produtos)

    # Calcular o produto com maior faturamento
    tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
    tabela_faturamento = tabela_total.groupby("Produto")["Faturamento"].sum().sort_values(ascending=True)
    print(tabela_faturamento)

    # Calcular a loja/cidade que mais faturou
    tabela_lojas = tabela_total.groupby("Loja")["Faturamento"].sum().sort_values(ascending=True)
    print(tabela_lojas)

    # Gerar o gráfico de faturamento por loja
    grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento", title="Faturamento por Loja")
    

    # Renderizar a página HTML passando as tabelas e o gráfico
    return render_template('index.html', 
                           tabela_total=tabela_total.to_html(), index=False, 
                           tabelas_produtos=tabelas_produtos.to_frame().to_html(), 
                           tabela_faturamento=tabela_faturamento.to_frame().to_html(),
                           tabela_lojas=tabela_lojas.to_frame().to_html(), 
                           grafico=grafico.to_html())

if __name__ == '__main__':
    app.run(debug=True)