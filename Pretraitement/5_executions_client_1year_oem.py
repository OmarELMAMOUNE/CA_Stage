from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from transforms.api import Input, Output, transform_df
from datetime import datetime

# specific date (max alerts)
start_date_str = "2024-11-01"
end_date_str = "2024-11-30"
start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

first_date_str = "2023-10-31"
first_date_str = "2023-11-01"
first_date = datetime.strptime(first_date_str, '%Y-%m-%d').date()

@transform_df(
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/executions_client_1year'),
    df_exec_client=Input("ri.foundry.main.dataset.2f14af88-8165-4ff0-8b08-fb768fdea6d4"),
    df_comptes=Input("ri.foundry.main.dataset.6019fc25-e4fe-449e-ae68-91a3fa2bc02e"),
    df_produits=Input("ri.foundry.main.dataset.9a4d6bed-b277-47c7-b77c-f185b6adc4e4"),
    df_param=Input("ri.foundry.main.dataset.9b7f6e94-f46e-4983-a42d-58c5dccf1134"),
)
def compute(ctx, df_exec_client : DataFrame, df_comptes : DataFrame, df_produits : DataFrame, df_param : DataFrame):

#    df_exec_client = df_exec_client.filter(df_exec_client["date_traitement"] == date)

    df_param = df_param.filter(F.col("nom_scenario") == "DC-CIV")
    param1 = df_param.first()["dcciv_total_montant"]
    param2 = int(df_param.first()["dcciv_anciennete_compte_mois"])
    param3 = df_param.first()["dcciv_concentration_valeur_percentage"]
    param4 = df_param.first()["dcciv_deviation_score"]

    # filtering equities (ou code_type_produit == "EQ")
    df_produits = df_produits.select("id_produit", "numero_isin", "numero_isin_sous_jacent", "code_type_produit", "code_type_titre", "nature_sous_jacent")
    df_exec_client = df_exec_client.join(df_produits, on="id_produit", how="left")
    df_exec_client = df_exec_client.filter(F.col("code_type_produit") == "EQ")
    df_exec_client = df_exec_client.filter(F.col("nature_sous_jacent").isNull() | (F.col("nature_sous_jacent").isNotNull()
    & (F.col("nature_sous_jacent") != "Indice")))

    # date_ouverture de table comptes
    df_comptes = df_comptes.select("id_compte", "business_unit", "date_ouverture")
    df_exec_client = df_exec_client.join(df_comptes, on=["id_compte", "business_unit"], how="inner")

    # Récupération des comptes dont l’ancienneté est >= Paramètre2 mois (au moment du lancement de l’analyse)
    df_exec_client = df_exec_client.withColumn("month",
    F.month("date_traitement")
    ) \
    .withColumn("year",
    F.year("date_traitement")
    ) \
    .withColumn("start_time",
    F.to_timestamp(F.trunc("date_traitement", "MM"))
    ) \
     .withColumn("business_date",
    F.last_day("date_traitement")
    ) \
    .withColumn("end_time",
    F.to_timestamp(F.concat(F.last_day("date_traitement").cast("string"), F.lit("T23:59:59.000Z")))
    ) \
    .withColumn("start_date_ts",
    F.to_timestamp(F.lit(start_date))
    ) \
    .withColumn("end_date_ts",
    F.to_timestamp(F.concat(F.lit(end_date).cast("string"), F.lit("T23:59:59.000Z")))
    ) \
    .withColumn("first_date_ts",
     F.to_timestamp(F.lit(first_date))
   # F.to_timestamp(F.concat(F.lit(first_date).cast("string"), F.lit("T23:59:59.000Z")))
    )

    # df_exec_client = df_exec_client.filter(F.add_months(F.col("date_ouverture"), param2) <= F.col("first_date_ts"))

    df_exec_client = df_exec_client.filter((F.col("date_traitement") >= F.col("first_date_ts")) & (F.col("date_traitement") < F.col("start_date_ts")))

    return df_exec_client