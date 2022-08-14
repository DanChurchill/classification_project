def get_telco_data():
    """
    Retrieve locally cached data .csv file from the telco dataset
    If no locally cached file is present retrieve the data from the codeup database server

    Keyword arguments:
    none

    Returns:
    DataFrame
    """
    
    filename = "telco.csv"

    # if file is available locally, read it
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
    # if file not available locally, acquire data from SQL database
    # and write it as csv locally for future use 
        df = pd.read_sql('''            
                            SELECT * FROM customers
                            JOIN contract_types 
                            USING (contract_type_id)
                            JOIN payment_types 
                            USING (payment_type_id)
                            JOIN internet_service_types 
                            USING (internet_service_type_id);  ''', get_connection('telco_churn'))

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)
        return df