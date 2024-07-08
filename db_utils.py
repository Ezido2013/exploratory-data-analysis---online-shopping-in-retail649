from sqlalchemy import create_engine
import pandas as pd
import yaml

# load_credentials('credentials')
def load_credentials(credentials_filename: str):
    """
    Loads the credentials from a YAML file and returns the data dictionary.

    Args:
        file_path (str): The path to the YAML file containing the credentials. Default is 'credentials.yaml'.

    Returns:
        dict: The dictionary containing the credentials data.
    """
    with open(f'{credentials_filename}.yaml','r') as f:
        credentials = yaml.safe_load(f)
        print(credentials)
        return credentials
db_credentials = load_credentials('credentials')
print(db_credentials)

class RDSDatabaseConnector:
    def __init__(self, credentials: dict):
        """
        Initializes the RDSDatabaseConnector with the provided credentials.

        Args:
            credentials (dict): A dictionary containing the following keys:
                - 'RDS_HOST': The hostname or IP address of the RDS instance.
                - 'RDS_USER': The username for the database.
                - 'RDS_PASSWORD': The password for the database user.
                - 'RDS_DATABASE': The name of the database to connect to.
                - 'RDS_PORT': The port number for the RDS instance (default is 3306).

        Raises:
            ValueError: If any of the required credentials are missing.
        """
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
        """
        Establishes a connection to the RDS database using the provided credentials.
        """
        connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"
        self.engine = create_engine(connection_string)
        return self.engine

    def get_customer_activity(self) -> pd.DataFrame:
        """
        Uses Pandas read_sql_query function to extract data from the RDS database and returns it as a Pandas DataFrame
        stored in a table called customer_activity.

        """
        if self.engine is None:
            raise Exception("Engine not initialized. Call initialize_sqlalchemy_engine() first.")
        query = "SELECT * FROM customer_activity"
        return pd.read_sql_query(query, self.engine)
    
    def load_data_from_csv(customer):
        """
        Load data from a local CSV file into a Pandas DataFrame.

        Parameters:
        file_path (str): The path to the CSV file.

        Returns:
        pd.DataFrame: The data loaded into a DataFrame.
        """
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

  