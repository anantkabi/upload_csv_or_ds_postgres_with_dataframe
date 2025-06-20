
```markdown
# Upload CSV or Dataset to PostgreSQL with DataFrame using Airflow

This project demonstrates how to automate the process of loading a CSV or dataset into a PostgreSQL database using Apache Airflow. It includes a DAG that reads a CSV file into a Pandas DataFrame and inserts the data into a PostgreSQL table using `PostgresHook`.

## 🚀 Features

- Reads CSV data using Pandas
- Inserts data into PostgreSQL using Airflow's `PostgresHook`
- Conditional table cleanup based on row count
- Modular and extensible DAG structure
- Includes SQL table creation via `SQLExecuteQueryOperator`

## 📁 Project Structure

```
├── dags/
│   ├── file_to_postgres_dataframe.py
│   └── data/
│       └── loan_data.csv
├── requirements.txt
└── README.md

```

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/anantkabi/upload_csv_or_ds_postgres_with_dataframe.git
cd upload_csv_or_ds_postgres_with_dataframe
```

2. **Install dependencies**

Make sure you have Airflow and required providers installed:

```bash
pip install apache-airflow pandas psycopg2-binary yfinance
```

3. **Place your CSV file**

Put your `loan_data.csv` file in the `dags/data/` directory.

4. **Start Airflow and other dependencies**

```bash
docker-compose up -d
```
Then visit `http://localhost:8080` to trigger the DAG.

5. **Configure Airflow connection**

Set up a PostgreSQL connection in Airflow with the ID: `postgres_airflow_conn`.

## 📊 Example DAG Tasks

- `File_upload_Re-create_postgres_table_if_not_exists`: Re-Creates the `loan_data` table if it doesn't exist to upload data from a csv file
- `File_upload_Delete_table_if_not_empty`: Deletes existing rows if the table has data while uploading csv file to table
- `File_upload_insert_csv_into_postgres_db_using_hook_and_df`: Loads CSV into PostgreSQL table using dataframes and hook.
- `Dataset_upload_Re-create_postgres_table_if_not_exists`: Creates the `iris_data` table if it doesn't exist to upload public dataset
- `Dataset_upload_Delete_table_if_not_empty`: Deletes existing rows if the table has data
- `Dataset_upload_Insert_iris_data_into_postgres_db_using_hook_and_df`: Loads iris dataset into PostgreSQL
- 
## 📌 Notes

- The DAG is scheduled to run daily at midnight (`0 0 * * *`)
- You can modify the table schema or CSV path as needed
- Compatible with Airflow 3.x

## 📬 Contact

Maintained by [@anantkabi](https://github.com/anantkabi). Feel free to open issues or submit pull requests!

---

Happy automating! 🛠️🐘📈
```
