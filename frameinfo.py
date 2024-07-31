class DataFrameInfo:
    def __init__(self, df):
        """
        Initializes the DataFrameInfo class with a Pandas DataFrame.

        Parameters:
        df (pd.DataFrame): The DataFrame to be analyzed.
        """
        self.df = df

    def describe_columns(self):
        """Describe all columns in the DataFrame to check their data types."""
        description = {
            "Column Name": self.df.columns,
            "Data Type": self.df.dtypes,
            'Non-Null Count': self.df.count(),
            'Unique Count': self.df.nunique()
         } 
        # description_df = pd.DataFrame(description)
        # return description_df.reset_index(drop=True)

    def get_statistical_values(self):
        """
        Extracts statistical values (median, standard deviation, and mean) from the DataFrame.

        Returns:
        pd.DataFrame: A DataFrame containing the median, standard deviation, and mean for numeric columns.
        """
        try:
            numeric_df = self.df.select_dtypes(include=[float, int])
            stats = {
                'Median': numeric_df.median(),
                'Standard Deviation': numeric_df.std(),
                'Mean': numeric_df.mean()
            }
            # stats_df = pd.DataFrame(stats)
            # return stats_df
        except Exception as e:
            print(f"Error calculating statistical values: {e}")
            return None
        
    def count_distinct_values(df):
        """
        Counts distinct values in categorical columns of a DataFrame.

        Parameters:
        df (pd.DataFrame): The DataFrame to analyze.

        Returns:
        pd.Series: A series where the index is the column names and the values are the counts of distinct values.
        """
        # Identifying categorical columns
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns

        # Counting distinct values in each categorical column
        distinct_counts = df[categorical_columns].nunique()

        return distinct_counts


# df = pd.read_csv('customer.csv')
# df_info = DataFrameInfo(df)
# description = df_info.describe_columns()
# print(description)
# print(df_info.get_statistical_values())
# distinct_counts = count_distinct_values(df)
# print(distinct_counts)