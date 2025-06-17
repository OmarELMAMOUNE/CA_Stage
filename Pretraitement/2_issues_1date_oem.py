from pyspark.sql import DataFrame
# from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df
from datetime import datetime

# specific date (max alerts)
date_str = "2024-11-30"
date = datetime.strptime(date_str, '%Y-%m-%d').date()

categorie_scenario = "dc-civ"


@transform_df(
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/issues'),
    df=Input("ri.foundry.main.dataset.52d8bbeb-6e49-45d6-a703-b1a8499a4c92"),
    )
def compute(ctx, df : DataFrame):

    df = df.filter((df["date_traitement"] == date) & (df["categorie_scenario"] == categorie_scenario))

    return df