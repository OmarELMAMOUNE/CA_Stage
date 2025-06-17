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
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/scenMgr3'),
    source_df_1m=Input('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/scenMgr1'),
    source_df_1y=Input('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/scenMgr2'),
    df_param=Input("ri.foundry.main.dataset.9b7f6e94-f46e-4983-a42d-58c5dccf1134"),
)
def compute(source_df_1m, source_df_1y, df_param):

    df_param = df_param.filter(F.col("nom_scenario") == "DC-CIV")
    param1 = df_param.first()["dcciv_total_montant"]
    param2 = int(df_param.first()["dcciv_anciennete_compte_mois"])
    param3 = df_param.first()["dcciv_concentration_valeur_percentage"]
    param4 = df_param.first()["dcciv_deviation_score"]

    source_df_1y = source_df_1y.select("id_compte", "avg_nb_trades", "avg_sum_amount", "avg_max_amount", 
    "std_max_amount", "std_nb_trades", "std_sum_amount", "exchange_list", "product_list")

    source_df_1y = source_df_1y.withColumnRenamed("exchange_list", "histo_exchange_list")
    source_df_1y = source_df_1y.withColumnRenamed("product_list", "histo_product_list")
    source_df_1y = source_df_1y.withColumnRenamed("nb_trades", "histo_nb_trades")

    source_df_1m = source_df_1m.join(source_df_1y, on="id_compte", how="left").distinct()

    source_df_1m = source_df_1m.withColumn("deviation_nb_trades",
    F.abs(F.col("nb_trades") - F.col("avg_nb_trades")) / F.col("std_nb_trades")
    ). \
    withColumn("deviation_sum_amount",
    F.abs(F.col("sum_total_amount") - F.col("avg_sum_amount")) / F.col("std_sum_amount")
    ). \
    withColumn("deviation_max_amount",
    F.abs(F.col("max_amount") - F.col("avg_max_amount")) / F.col("std_max_amount")
    )

    source_df_1m = source_df_1m.withColumn("new_exchange_list",
    F.when(F.size(F.col("histo_exchange_list")) >= 0,
    F.array_except(F.col("exchange_list"), F.col("histo_exchange_list"))
    ).otherwise(F.col("exchange_list"))
    ). \
    withColumn("new_product_list",
    F.when(F.size(F.col("histo_product_list")) >= 0,
    F.array_except(F.col("product_list"), F.col("histo_product_list"))
    ).otherwise(F.col("product_list"))
    )

    return source_df_1m