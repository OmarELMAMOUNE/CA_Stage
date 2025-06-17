from pyspark.sql import functions as F
from transforms.api import transform_df, Input, Output
from pyspark.sql.window import Window

@transform_df(
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/scenMgr1'),
    source_df=Input('ri.foundry.main.dataset.de03c29d-b43f-410b-8329-343228efa0fe'),
    df_param=Input("ri.foundry.main.dataset.9b7f6e94-f46e-4983-a42d-58c5dccf1134"),
)
def compute(source_df, df_param):

    df_param = df_param.filter(F.col("nom_scenario") == "DC-CIV")
    param1 = df_param.first()["dcciv_total_montant"]
    param2 = int(df_param.first()["dcciv_anciennete_compte_mois"])
    param3 = df_param.first()["dcciv_concentration_valeur_percentage"]
    param4 = df_param.first()["dcciv_deviation_score"]

  #  source_df_agg = source_df.groupBy("id_compte").agg(
  #  F.sum("montant_transaction_origine").alias("sum_total_amount")
  #  )
  #  source_df = source_df.join(source_df_agg, on="id_compte", how="left")

    window_spec = Window.partitionBy("id_compte")
    window_spec_isin = Window.partitionBy("id_compte", "code_isin")


    source_df_agg = source_df.groupBy("id_compte").agg(
       F.sum("montant_transaction_origine").alias("sum_total_amount"),
       F.collect_set("code_place").alias("exchange_list"),
       F.collect_set("id_produit").alias("product_list"),
       F.count("*").alias("nb_trades"),
       F.avg("montant_transaction_origine").alias("mean_amount"),
       F.max("montant_transaction_origine").alias("max_amount")
    )

    source_df_agg = source_df_agg.filter(F.col("sum_total_amount") >= param1)

    source_df_agg_isin = source_df.groupBy("id_compte", "code_isin").agg(
       F.sum("montant_transaction_origine").alias("sum_amount_by_isin")
    )

    source_df_agg_isin = source_df_agg_isin.join(source_df_agg, on="id_compte", how="left")

    source_df_agg_isin = source_df_agg_isin.withColumn("ratio_sum_amount_by_product",
    F.col("sum_amount_by_isin") / F.col("sum_total_amount")
    )

  #  source_df = source_df.withColumn("sum_total_amount",
  #  F.sum("montant_transaction_origine").over(window_spec)
  #  )
  #  source_df = source_df.withColumn("exchange_list",
  #  F.collect_set("code_place").over(window_spec)
  #  ). \
  #  withColumn("product_list",
  #  F.collect_set("id_produit").over(window_spec)
  #  ). \
  #  withColumn("nb_trades",
  #  F.count("*").over(window_spec)
  #  ). \
  #  withColumn("mean_amount",
  #  F.avg("montant_transaction_origine").over(window_spec)
  #  ). \
  #  withColumn("max_amount",
  #  F.max("montant_transaction_origine").over(window_spec)
  #  ). \
  #  withColumn("sum_amount_by_isin",
  #  F.sum("montant_transaction_origine").over(window_spec_isin)
  #  ). \
  #  withColumn("ratio_sum_amount_by_product",
  #  F.col("sum_amount_by_isin") / F.col("sum_total_amount")
  #  )
    
  #  source_df = source_df.filter(F.col("ratio_sum_amount_by_product") >= param3)

    source_df_agg_isin = source_df_agg_isin.withColumn("isin_avec_concentration",
    F.collect_set("code_isin").over(window_spec)
    ). \
    withColumn("ratio_avec_concentration",
    F.collect_set("ratio_sum_amount_by_product").over(window_spec)
    )

    return source_df_agg_isin