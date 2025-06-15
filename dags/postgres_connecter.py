from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator  # Use this instead of PostgresOperator

default_args = {
    'owner': 'anant_kabi',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='postrgres-connecter',
    description='A DAG to connect to Postgres and execute SQL commands',
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule='0 0 * * *'
) as dag:
    task1 = SQLExecuteQueryOperator(
        task_id='recreate_postgres_table',
        conn_id='postgres_airflow_conn',
        sql="""
            CREATE TABLE if not exists Orders (
                OrderID INT PRIMARY KEY,
                Status VARCHAR(50)
            )
        """
    )
    task2 = SQLExecuteQueryOperator(
        task_id='insert_data_into_table',
        conn_id='postgres_airflow_conn',
        sql="""
            INSERT INTO Orders VALUES (21, 'delivered')
        """
    )
    task1 >> task2