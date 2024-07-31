import matplotlib.pyplot as plt
import matplotlib.style as style
import missingno as msno 
import pandas as pd
import seaborn as sns

class Plotter:
    def __init__(self, df):
        """
        Initializes the Plotter class to visualise the removal of NULL values
        """
        self.df = df
    
    def visualize_null_removal(self):
        """
        Visualizes the missing values in the dataset using a bar chart.
        """
        msno.bar(self.df)
        plt.show()
    
    def visualize_numeric_features(self):
        """
        Visualizes histograms with KDE plots for all numeric features and prints the list of categorical features.
        """
        numeric_features = [
            'administrative',
            'administrative_duration',
            'informational',
            'informational_duration',
            'product_related',
            'bounce_rates',
            'exit_rates',
            'page_values',
            'month',
            'operating_systems',
            'browser',
            'region',
            'traffic_type',
            'visitor_type',
            'weekend',
            'revenue'
        ]        
   
        categorical_features = [col for col in self.df.columns if col not in numeric_features]
        
        sns.set(font_scale=0.7)
        f = pd.melt(self.df, value_vars=numeric_features)
        g = sns.FacetGrid(f, col="variable", col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)

        plt.show()
        
        print(categorical_features)

df = pd.read_csv('customer.csv')
plotter = Plotter(df)
plotter.visualize_null_removal()
plotter.visualize_numeric_features()




