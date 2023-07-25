import pandas as pd
from google.cloud import bigquery



def fetch_data(query):
    '''
    Function to fetch desired data from the main file stored in bigquery
    The query defines whether you get it all or just a desired slice
    '''
    client = bigquery.Client(project=PROJECT_NAME)
    query_job = client.query(query)
    
    return query_job.result().to_dataframe()

def clean_df(df):
    
    df.drop(columns = ["Domain","Domain_Code","Area_Code__M49_","Element_Code","Item_Code__CPC_","Year_Code"], inplace = True)