
```markdown
# Upload CSV or Dataset to PostgreSQL with DataFrame using Apache airflow and Python with Metabase and Postgres integration

This project demonstrates how to automate the process of loading a CSV or dataset into a PostgreSQL database using Apache Airflow. It includes a DAG that reads a CSV file into a Pandas DataFrame and inserts the data into a PostgreSQL table using `PostgresHook`. Metabase setup is also included now with this setup for visualization and reporting purpose.

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
![image](https://github.com/user-attachments/assets/d6383f27-e315-40c8-897b-2ff063ab57f1)

Then visit `http://localhost:8080` to trigger the DAG.

5. **Configure Airflow connection**

Set up a PostgreSQL connection in Airflow with the ID: `postgres_airflow_conn`.

6. **Run the DAG 'load_csv_and_dataset_to_postgres'**

This step will create load_data table and add data into it for reporting purpose.

7. **Visit Metabase setup page at `http://localhost:3000`**

If your metabase services are properly working and started, you would see a metabase UI

![image](https://github.com/user-attachments/assets/a3f83b37-afc8-4c75-b730-0b1307f21b88)


8. **Setup Metabase connection with airflow postgres DB as per below**
![image](https://github.com/user-attachments/assets/82547ba0-33e7-471c-882d-840c4fd7ef96)

9. **Feel free to create various dashboard from your table/data**

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
