from airflow import DAG
from airflow.providers.google.common.hooks.base_google import GoogleBaseHook
import pandas as pd
import gspread
from datetime import datetime


with DAG(
    dag_id="dataframe_to_spreadsheet",
    start_date=datetime.now(),
    schedule_interval="@daily",
) as dag:

    @dag.task
    def dataframe_to_spreadsheet_task():
        data = {
            "products": ["product_1", "product_2", "product_3"],
            "price": [50, 40, 45],
        }

        df = pd.DataFrame(data)

        # Hook to Google Sheets in order to get connection from Airflow
        hook = GoogleBaseHook(gcp_conn_id="google_conn_id")
        credentials = hook.get_credentials()
        google_credentials = gspread.Client(auth=credentials)

        # Reading a spreadsheet by its title
        sheet = google_credentials.open("Products - Data")

        # Defining the worksheet to manipulate
        worksheet = sheet.worksheet("products-data")

        # Sending data from df to the worksheet
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    dataframe_to_spreadsheet_task()
