from pyspark.sql import functions as F
from transforms.api import transform_df, Input, Output
from pyspark.sql.window import Window
from datetime import datetime

start_date_str = "2024-11-01"
end_date_str = "2024-11-30"
start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

first_date_str = "2023-10-31"
first_date = datetime.strptime(first_date_str, '%Y-%m-%d').date()

@transform_df(
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/scenMgr2'),
    source_df=Input('ri.foundry.main.dataset.553d412a-15ef-4035-a5b3-bf7f20fa6db9'),
    df_param=Input("ri.foundry.main.dataset.9b7f6e94-f46e-4983-a42d-58c5dccf1134"),
)
def compute(source_df, df_param):

    df_param = df_param.filter(F.col("nom_scenario") == "DC-CIV")
    param1 = df_param.first()["dcciv_total_montant"]
    param2 = int(df_param.first()["dcciv_anciennete_compte_mois"])
    param3 = df_param.first()["dcciv_concentration_valeur_percentage"]
    param4 = df_param.first()["dcciv_deviation_score"]

    window_spec = Window.partitionBy("id_compte")
    window_spec_month = Window.partitionBy("id_compte", "month", "year")

    source_df = source_df.withColumn("exchange_list",
    F.collect_set("code_place").over(window_spec)
    ). \
    withColumn("product_list",
    F.collect_set("id_produit").over(window_spec)
    )
    source_df_agg = source_df.groupBy("id_compte", "month", "year").agg(
        F.count("*").alias("nb_trades"),
        F.sum("montant_transaction_origine").alias("sum_amount"),
        F.avg("montant_transaction_origine").alias("mean_amount"),
        F.max("montant_transaction_origine").alias("max_amount")
    )

    source_df_agg = source_df_agg.withColumn("avg_nb_trades",
    F.avg("nb_trades").over(window_spec)
     ). \
    withColumn("std_nb_trades",
    F.std("nb_trades").over(window_spec)
    ). \
    withColumn("avg_sum_amount",
    F.avg("sum_amount").over(window_spec)
     ). \
    withColumn("std_sum_amount",
    F.std("sum_amount").over(window_spec)
    ). \
    withColumn("avg_max_amount",
    F.avg("max_amount").over(window_spec)
     ). \
    withColumn("std_max_amount",
    F.std("max_amount").over(window_spec)
    )

    source_df = source_df.select("id_compte", "exchange_list", "product_list").distinct()
    source_df_agg = source_df_agg.join(source_df, on="id_compte", how="left")

    return source_df_agg