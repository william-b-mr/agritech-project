import pandas as pd
from google.cloud import bigquery

PROJECT_NAME="windproject"
PROJECT_ID="windproject-393609"
query = """
    SELECT *
    FROM `windproject-393609.FAOSTAT.crop_yield`
    """

def fetch_data(query):
    '''
    Function to fetch desired data from the main file stored in bigquery
    The query defines whether you get it all or just a desired slice
    '''
    client = bigquery.Client()
    query_job = client.query(query)
    result = query_job.result()
    
    # Create a DataFrame from the queried results
    data_df = result.to_dataframe()
    
    return data_df

if __name__=="__main__":
    data = fetch_data(query)
    print(data.head())
    print(data.info())