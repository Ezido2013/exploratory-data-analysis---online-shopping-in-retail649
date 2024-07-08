import yaml
import pandas as pd
from sqlalchemy import create_engine

def load_credentials(credentials_filename: str):
    with open(f'{credentials_filename}.yaml','r') as f:
        credentials = yaml.safe_load(f)
        print(credentials)
        return credentials
# load_credentials('credentials')
db_credentials = load_credentials('credentials')
print(db_credentials)

class RDSDatabaseConnector:
    def __init__(self, credentials: dict):
        self.host = credentials.get('RDS_HOST')
        self.user = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.dbname = credentials.get('RDS_DATABASE')
        self.port = credentials.get('RDS_PORT')
    
    # Validate and convert the port value
        if self.port is None:
            raise ValueError("Port must be provided.")
        
        try:
            self.port = int(self.port)
        except ValueError:
            raise ValueError("Port must be an integer.")
        
        self.engine = None

    def initialize_sqlalchemy_engine(self):
        connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        self.engine = create_engine(connection_string)
        return self.engine

    def fetch_data(self, query: str) -> pd.DataFrame:
        if self.engine is None:
            raise Exception("Engine not initialized. Call initialize_sqlalchemy_engine() first.")
        return pd.read_sql_query(query, self.engine)

    def get_customer_activity(self) -> pd.DataFrame:
        if self.engine is None:
            raise Exception("Engine not initialized. Call initialize_sqlalchemy_engine() first.")
        query = "SELECT * FROM customer_activity"
        return pd.read_sql_query(query, self.engine)
    
    def load_data_from_csv(customer):
        try:
            df = pd.read_csv('customer.csv')
            print(f"Data successfully loaded from {'customer.csv'}")
            return df
        except Exception as e:
            print(f"Error loading data from {'customer.csv'}: {e}")
            return None
    df = load_data_from_csv('customer.csv')
    print(df.head()) 

connector = RDSDatabaseConnector(db_credentials)
connector.initialize_sqlalchemy_engine()
customer_activity = connector.get_customer_activity()
print(customer_activity)
customer_activity.to_csv('customer.csv', index=False)

  