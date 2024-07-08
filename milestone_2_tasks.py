
import yaml
import pandas as pd
from sqlalchemy import create_engine

def load_credentials(credentials):
    with open(f'{credentials}.yaml','r') as f:
        credentials = yaml.safe_load(f)
        print(credentials)
    load_credentials(credentials)

class RDSDatabaseConnector:
    def __init__(self, credentials: dict):
        self.host = credentials.get('host')
        self.user = credentials.get('user')
        self.password = credentials.get('password')
        self.dbname = credentials.get('dbname')
        self.port = credentials.get('port')
        self.database_type = credentials.get('database_type')
        self.dbapi = credentials.get('dbapi')
        self.engine = None

    # Validate and convert the port value
        if self.port is None:
            raise ValueError("Port must be provided.")
        
        try:
            self.port = int(self.port)
        except ValueError:
            raise ValueError("Port must be an integer.")
        
        self.engine = None

    def initialize_engine(self):
        connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        self.engine = create_engine(connection_string)
        return self.engine

    def fetch_data(self, query: str) -> pd.DataFrame:
        if self.engine is None:
            raise Exception("Engine not initialized. Call initialize_engine() first.")
        return pd.read_sql_query(query, self.engine)

    def get_customer_activity(self) -> pd.DataFrame:
        if self.engine is None:
            raise Exception("Engine not initialized. Call initialize_engine() first.")
        query = "SELECT * FROM customer_activity"
        return pd.read_sql_query(query, self.engine)
    
    def save_data_to_csv(self, df: pd.DataFrame, file_path: str):
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")

# Usage example:
# Define the credentials dictionary
credentials = {
    'RDS_HOST': 'eda-projects.cq2e8zno855e.eu-west-1.rds.amazonaws.com',
    'RDS_USER': 'admin',
    'RDS_PASSWORD': 'EDAonlinecustomer',
    'RDS_DB_NAME': 'postgres',
    'RDS_PORT': 5432 
}

# Create an instance of the RDSDatabaseConnector class
connector = RDSDatabaseConnector(credentials)

# Initialize the engine
connector.initialize_engine()

# Fetch data from the customer_activity table
customer_activity_df = connector.get_customer_activity()

# Save the DataFrame to a CSV file
connector.save_data_to_csv(customer_activity_df, 'customer_activity.csv')

# Print the DataFrame to verify
print(customer_activity_df)