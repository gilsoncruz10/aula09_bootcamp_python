import pandas as pd
import os
import glob

#uma função de extract que le e consolida os arquivos json

def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    # criando um caminho a ser lido pelo script
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    # criando uma lista de arquivos json
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    # concatenando os arquivos em um arquivo so
    df_consolidado = pd.concat(df_list, ignore_index=True)
    return df_consolidado


# uma função que transforma

def calcular_kpi_de_total_de_vendas(df_consolidado: pd.DataFrame) -> pd.DataFrame:
    """
    Pega meu dataframe e acrescenta uma nova coluna com o 'valor total', que e a multiplicação da quantitade x venda
    """
    df_consolidado ["Total"] = df_consolidado["Quantidade"] * df_consolidado["Venda"]
    return df_consolidado


#uma função que da load em csv e parquet

# parametro que vai ser "csv" ou "parquet" ou "ambos"

def carregar_dados(df_consolidado: pd.DataFrame, format_saida: list):
    """
    parametro que vai ser "csv" ou "parquet" ou "ambos"
    """
    for formato in format_saida:
        if formato == 'csv':
            df_consolidado.to_csv("dados.csv")
        elif formato == 'parquet':
            df_consolidado.to_parquet("dados.parquet")

def pipeline_calcular_kpi_de_vendas_consolidado (pasta: str, formato_de_saida: list):
    df_consolidado = extrair_dados_e_consolidar(pasta)
    df_calculado = calcular_kpi_de_total_de_vendas(df_consolidado)
    carregar_dados(df_calculado, formato_de_saida)

if __name__ == "__main__":
    pasta_argumento: str = 'data'
    dataframe_consolidado = extrair_dados_e_consolidar(pasta=pasta_argumento)
    dataframe_calculado = calcular_kpi_de_total_de_vendas(dataframe_consolidado)
    formato_de_saida: list = ["csv", "parquet"]
    carregar_dados(dataframe_calculado, formato_de_saida)
