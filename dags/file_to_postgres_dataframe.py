from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator  # Use this instead of PostgresOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import numpy as np
import pandas as pd
import warnings
from sklearn.datasets import load_iris
warnings.filterwarnings('ignore')

default_args = {
    'owner': 'anant_kabi',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

def insert_dataframe():
    #df = pd.read_csv('loan_data.csv')   
    df = pd.read_csv('/opt/airflow/dags/data/loan_data.csv')  # Update path as per your deployment
    hook = PostgresHook(postgres_conn_id="postgres_airflow_conn")
    rows = list(df.itertuples(index=False, name=None))
    hook.insert_rows(table="loan_data", rows=rows)

def insert_iris_dataframe():
    #df = pd.read_csv('loan_data.csv')   
    # Load historical stock data for a symbol (e.g., Apple)
    iris = load_iris(as_frame=True)
    df1 = iris.frame
    hook = PostgresHook(postgres_conn_id="postgres_airflow_conn")
    rows = list(df1.itertuples(index=False, name=None))
    hook.insert_rows(table="iris_data", rows=rows)

def delete_table_if_has_data():
    hook = PostgresHook(postgres_conn_id="postgres_airflow_conn")
    table_name = "loan_data"
    count_result = hook.get_first(f"SELECT COUNT(*) FROM {table_name};")
    row_count = count_result[0] if count_result else 0 #Ternary operator to handle None
    if row_count > 0:
        hook.run(f"delete from {table_name};")
        print(f"Table {table_name} data deleted because it contained {row_count} rows.")
    else:
        print(f"Table {table_name} is empty. No action taken.")

def delete_iris_table_if_has_data():
    hook = PostgresHook(postgres_conn_id="postgres_airflow_conn")
    table_name = "iris_data"
    count_result = hook.get_first(f"SELECT COUNT(*) FROM {table_name};")
    row_count = count_result[0] if count_result else 0 #Ternary operator to handle None
    if row_count > 0:
        hook.run(f"delete from {table_name};")
        print(f"Table {table_name} data deleted because it contained {row_count} rows.")
    else:
        print(f"Table {table_name} is empty. No action taken.")

with DAG(
    dag_id='load_csv_and_dataset_to_postgres',
    description='A DAG to connect to Postgres and execute SQL commands to load CSV data',
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule='0 0 * * *'
) as dag:
    task1 = SQLExecuteQueryOperator(
        task_id='File_upload_Re-create_postgres_table_if_not_exists',
        conn_id='postgres_airflow_conn',
        sql="""
            CREATE TABLE IF NOT EXISTS public.loan_data (
                id VARCHAR(200), 
                amount_requested VARCHAR(200),
                amount_funded_by_investors VARCHAR(200),
                interest_rate VARCHAR(200),
                loan_length VARCHAR(200),
                loan_purpose VARCHAR(200),
                debt_to_income_ratio VARCHAR(200),
                state VARCHAR(200),
                home_ownership VARCHAR(200),
                monthly_income VARCHAR(200),
                fico_range VARCHAR(200),
                open_credit_lines VARCHAR(200),
                revolving_credit_balance VARCHAR(200),
                inquiries_last_6_months VARCHAR(200),
                employment_length VARCHAR(200)
                )
        """
    )
    task2 = PythonOperator(
        task_id='File_upload_Delete_table_if_not_empty',
        python_callable=delete_table_if_has_data,
        dag=dag
    )
    task3 = PythonOperator(
        task_id="File_upload_insert_csv_into_postgres_db_using_hook_and_df",
        python_callable=insert_dataframe,
        dag=dag
    )
    task4 = SQLExecuteQueryOperator(
        task_id='Dataset_upload_Re-create_postgres_table_if_not_exists',
        conn_id='postgres_airflow_conn',
        sql="""
            CREATE TABLE IF NOT EXISTS public.iris_data (
                sepal_length_cm FLOAT,
                sepal_width_cm FLOAT,
                petal_length_cm FLOAT,
                petal_width_cm FLOAT,
                target INTEGER
                )
        """
    )
    task5 = PythonOperator(
        task_id='Dataset_upload_Delete_table_if_not_empty',
        python_callable=delete_iris_table_if_has_data,
        dag=dag
    )
    task6 = PythonOperator(
        task_id="Dataset_upload_Insert_iris_data_into_postgres_db_using_hook_and_df",
        python_callable=insert_iris_dataframe,
        dag=dag
    )
    task1 >> task2 >> task3
    task4 >> task5 >> task6
