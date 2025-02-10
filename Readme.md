
# Deforestation Data Feeder (Python)

Refactor of the [Deforestation Data Feeder](https://github.com/terrabrasilis/deforestation-data-feeder) project, now developed in Python.

This project aims to generate .json files from data in our Postgres database to be used in the Deforestation Dashboard.

## Requirements

### 1. Install project dependencies
After creating your virtualenv, install the project dependencies using the following command:
```
pip install -r requirements.txt
```

### 2. Create and configure the .env file
Create a file named `.env` with the same parameters as the `.env_example` file. In each variable, provide the connection parameters to the database.

### 3. Run the project
After completing the previous steps, run the following command:
```
python generate_data.py
```