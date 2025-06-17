from pyspark.sql import DataFrame
# from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df
from datetime import datetime

# specific date (max alerts)
date_str = "2024-11-30"
date = datetime.strptime(date_str, '%Y-%m-%d').date()

categorie_scenario = "dc-civ"

@transform_df(
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/alertes'),
    df=Input("ri.foundry.main.dataset.612746dd-d54d-4431-821e-4f621bb4357a"),
    )
def compute(ctx, df : DataFrame):

    df = df.filter((df["date_traitement"] == date) & (df["categorie_scenario"] == categorie_scenario))

    return df