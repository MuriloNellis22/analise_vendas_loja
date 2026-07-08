import pandas as pd

def converter_data(df):
    df = df.copy()
    df['Data'] = pd.to_datetime(df['Data'])
    return df


def verificar_nulos(df):
    return df.isnull().sum()


def verificar_duplicados(df):
    return df.duplicated().sum()