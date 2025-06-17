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
    Output('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/scenMgr5'),
    source_df=Input('/ABM-f23a10/ABM - Revue des modèles/2025/output/FV/S07_DCCIV/scenMgr4'),
    df_param=Input("ri.foundry.main.dataset.9b7f6e94-f46e-4983-a42d-58c5dccf1134"),
)
def compute(source_df, df_param):

    source_df = source_df.drop("code_isin", "sum_amount_by_isin", "ratio_sum_amount_by_product").distinct()

    return source_df