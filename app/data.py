import pandas as pd
import faostat


def fetch_yield_data(crop, country=None, null_values=False, clean=True):
    '''
    This function returns a pandas df containing yield data for the crop and country (optional) provided as input
    If country is not specified, all countries and regions in the FAOSTAT db will be returned
    If null_values is not set to true, it will only return entries for years in which there are registered values (it may vary from country to country)
    If clean is not set to false, the function will only return the info considered to be relevant for further analytics and ML applications
    '''

    #Firstly, we fetch the encoding lists
    countries = faostat.get_areas('QCL')
    elements = faostat.get_elements('QCL')
    items = faostat.get_items('QCL')

    if crop not in items.keys():
        return "We don't have data on the selected crop"
        
    if country is None:
        df = faostat.get_data_df('QCL', pars={'elements':elements['Yield'],'items':items[crop]}, null_values=null_values)
    else:
        if country not in countries.keys():
            return "Please enter a valid country"
        else:
            df = faostat.get_data_df('QCL', pars={'elements':elements['Yield'],'items':items[crop],'areas':countries[country]}, null_values=null_values)
    
    if clean:
        df.drop(columns = ["Domain","Domain Code","Area Code (FAO)","Element Code","Item Code","Year Code"], inplace = True)
        df['Value'] = pd.to_numeric(df.Value)
        df['Year'] = pd.to_numeric(df.Year)
        
    return df

def populate_db ():
    """
    Populates a db in the cloud with the predicts created by the model
    """
    pass

if __name__=="__main__":
    data = fetch_yield_data("Wheat")
    print(data.head())
    print(data.info())