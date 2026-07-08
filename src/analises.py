def receita_total(df):
    return df['Total'].sum()


def produtos_mais_vendidos(df):
    return (
        df.groupby('Produto')['Quantidade']
        .sum()
        .sort_values(ascending=False)
    )


def faturamento_por_cidade(df):
    return (
        df.groupby('Cidade')['Total']
        .sum()
        .sort_values(ascending=False)
    )


def faturamento_por_categoria(df):
    return (
        df.groupby('Categoria')['Total']
        .sum()
        .sort_values(ascending=False)
    )


def pagamento_por_cidade(df):

    return (
        df.groupby(['Cidade', 'Pagamento'])
          .size()
          .unstack(fill_value=0)
    )


def vendas_mensais(df):
    df = df.copy()

    meses = {
    1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr',
    5: 'Mai', 6: 'Jun', 7: 'Jul', 8: 'Ago',
    9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
}

    df['Mes'] = df['Data'].dt.month.map(meses)

    ordem = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
             'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    faturamento_mes = (
        df.groupby('Mes')['Total']
          .sum()
          .reindex(ordem)
    )

    return faturamento_mes