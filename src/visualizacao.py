import matplotlib.pyplot as plt

def grafico_produtos(produtos):

    produtos.plot(
        kind='barh',
        figsize=(10,6)
    )

    plt.title('Top 10 Produtos Mais Vendidos')
    plt.xlabel('Quantidade')
    plt.ylabel('Produto')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def grafico_cidades(cidades):

    cidades.plot(
        kind='bar',
        figsize=(10,6),
        color='orange'
    )

    plt.title('Faturamento por Cidade')
    plt.xlabel('Cidade')
    plt.ylabel('Faturamento (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_categoria(categorias):

    categorias.plot(
        kind='bar',
        figsize=(8,5)
    )

    plt.title('Faturamento por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Faturamento')
    plt.tight_layout()
    plt.show()

def grafico_pagamentos(pagamentos):

    pagamentos.plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title('Distribuição das Formas de Pagamento')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()


def grafico_vendas_mensais(faturamento_mes):

    faturamento_mes.plot(
        kind='line',
        marker='o',
        figsize=(10,5),
        color='orange'
    )

    plt.title('Vendas por mês')
    plt.xlabel('Mês')
    plt.ylabel('Faturamento (R$)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()