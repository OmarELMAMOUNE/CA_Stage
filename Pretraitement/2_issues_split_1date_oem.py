from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df
from datetime import datetime

# specific date (max alerts)
date_str = "2024-11-30"
date = datetime.strptime(date_str, '%Y-%m-%d').date()

categorie_scenario = "dc-civ"


@transform_df(
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/issues_split'),
    df=Input('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/issues'),
    )
def compute(ctx, df : DataFrame):

    # df = df.filter((df["date_traitement"] == date) & (df["categorie_scenario"] == categorie_scenario))

    valeurs_generatrices_cle = df.first()["valeurs_generatrices_cle"]
    len_val = len(valeurs_generatrices_cle)
    for i in range(len_val):
        df = df.withColumn(valeurs_generatrices_cle[i], F.col("valeurs_generatrices_valeur").getItem(i))

    return df
    