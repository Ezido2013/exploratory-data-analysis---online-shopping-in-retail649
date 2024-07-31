import pandas as pd
class DataFrameTransform:
    def __init__(self, df):
        """
        Initializes the DataFrameInfo class with a Pandas DataFrame.

        Parameters:
        df (pd.DataFrame): The DataFrame to be analyzed.
        """
        self.df = df

def handle_null_values_with_median(df, column):
    """
    Fills null values in a specified column with the median of that column.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.
    column (str): The name of the column to handle null values for.

    Returns:
    pd.DataFrame: The DataFrame with null values filled.
    """
    median_value = df[column].median()
    df[column].fillna(median_value, inplace=True)
    return df
# Fill in null values for product_related_duration
# df = pd.read_csv('customer.csv')
# df = handle_null_values_with_median(df, 'product_related_duration')
# df['product_related_duration'] = df['product_related_duration'].fillna(df['product_related_duration'].median())
# print('percentage of null values in each column:')
# df.isnull().sum()/len(df)

# Fill in null values for informational_duration
# df = pd.read_csv('customer.csv')
# df = handle_null_values_with_median(df, 'informational_duration')
# df['informational_duration'] = df['informational_duration'].fillna(df['informational_duration'].median())
# print('percentage of null values in each column:')
# df.isnull().sum()/len(df)

# Fill in null values for administrative_duration
# df = pd.read_csv('customer.csv')
# df = handle_null_values_with_median(df, 'administrative_duration')
# df['administrative_duration'] = df['administrative_duration'].fillna(df['administrative_duration'].median())
# print('percentage of null values in each column:')
# df.isnull().sum()/len(df)