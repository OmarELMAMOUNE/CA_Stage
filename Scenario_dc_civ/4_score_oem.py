from pyspark.sql import functions as F
from transforms.api import transform_df, Input, Output
from pyspark.sql.window import Window
from datetime import datetime

start_date_str = "2024-11-01"
end_date_str = "2024-11-30"
start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

first_date_str = "2023-11-30"
first_date = datetime.strptime(first_date_str, '%Y-%m-%d').date()

@transform_df(
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/scenMgr4'),
    source_df=Input('ri.foundry.main.dataset.63d553aa-de38-49f2-ba75-a4ae57a03232'),
    df_param=Input("ri.foundry.main.dataset.9b7f6e94-f46e-4983-a42d-58c5dccf1134"),
)
def compute(source_df, df_param):

    df_param = df_param.filter(F.col("nom_scenario") == "DC-CIV")
    param1 = df_param.first()["dcciv_total_montant"]
    param2 = int(df_param.first()["dcciv_anciennete_compte_mois"])
    param3 = df_param.first()["dcciv_concentration_valeur_percentage"]
    param4 = df_param.first()["dcciv_deviation_score"]

    source_df = source_df.withColumn("score_nb_trades",
    F.when(F.col("deviation_nb_trades") < 10, 0).
    when(F.col("deviation_nb_trades") < 30, 5).
    when(F.col("deviation_nb_trades") < 100, 10).
    when(F.col("deviation_nb_trades") >= 100, 15)
    )

    source_df = source_df.withColumn("score_sum_amount",
    F.when(F.col("deviation_sum_amount") < 20, 0).
    when(F.col("deviation_sum_amount") < 50, 5).
    when(F.col("deviation_sum_amount") < 150, 10).
    when(F.col("deviation_sum_amount") < 400, 15).
    when(F.col("deviation_sum_amount") < 1000, 20).
    when(F.col("deviation_sum_amount") >= 1000, 25)
    )

    source_df = source_df.withColumn("score_max_amount",
    F.when(F.col("deviation_max_amount") < 10, 0).
    when(F.col("deviation_max_amount") < 20, 5).
    when(F.col("deviation_max_amount") < 35, 10).
    when(F.col("deviation_max_amount") < 50, 15).
    when(F.col("deviation_max_amount") < 150, 17).
    when(F.col("deviation_max_amount") >= 150, 20)
    )

    source_df = source_df.withColumn("score_exchange",
    F.when(F.size("new_exchange_list") < 1, 0).
    when(F.size("new_exchange_list") < 2, 2).
    when(F.size("new_exchange_list") < 3, 7).
    when(F.size("new_exchange_list") >= 3, 10)
    )

    source_df = source_df.withColumn("score_product",
    F.when(F.size("new_product_list") < 4, 0).
    when(F.size("new_product_list") < 8, 3).
    when(F.size("new_product_list") < 10, 5).
    when(F.size("new_product_list") >= 10, 7)
    )

    source_df = source_df.withColumn("score_total_deviation",
    F.col("score_nb_trades") + F.col("score_sum_amount") + F.col("score_max_amount") +
    F.col("score_exchange") + F.col("score_product")
    )

    source_df = source_df.filter(F.col("score_total_deviation") >= param4)

    return source_df