from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'anant_kabi',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='dag_with_postgres_operator',
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PostgresOperator(
        task_id='recreate_postgres_table',
        postgres_conn_id='postgres_airflow_conn',
        sql="""
            CREATE TABLE if not exists Orders (
                OrderID INT PRIMARY KEY,
                Status VARCHAR(50)
            )
        """
    )

    task2 = PostgresOperator(
        task_id='insert_data_into_table',
        postgres_conn_id='postgres_local',
        sql="""
            insert into Orders values(21,'delivered')
        """
    )
    
    task1 >>  task2