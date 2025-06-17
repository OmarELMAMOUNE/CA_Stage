from pyspark.sql import DataFrame
# from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df
from datetime import datetime

# specific date (max alerts)
date_str = "2024-11-30"
date = datetime.strptime(date_str, '%Y-%m-%d').date()

@transform_df(
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/executions_marche'),
    df_exec_marche=Input("ri.foundry.main.dataset.95211009-dbc5-431e-9310-a703ec220a5e"),
    )
def compute(ctx, df_exec_marche : DataFrame):

    df_exec_marche = df_exec_marche.filter(df_exec_marche["date_traitement"] == date)

 #   list_id_produit = df_ordre_marche.select("id_produit").drop_duplicates().toPandas()["id_produit"].tolist()

 #   df_exec_marche = df_exec_marche.filter(df_exec_marche["id_produit"].isin(list_id_produit))

    return df_exec_marche