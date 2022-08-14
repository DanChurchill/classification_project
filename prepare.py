def prep_telco(df):
    """
    Performs preparations on the telco DataFrame in order to make it usable for data exploration and modeling

    Keyword arguments:
    df: a dataframe containing customer data from the telco database

    Returns:
    prepared DataFrame
    """
    # delete index columns
    df = df.drop(columns=['internet_service_type_id', 'payment_type_id', 'contract_type_id', 'customer_id'])
    
    # convert total charges from string to floats
    df.total_charges = df.total_charges.str.replace(' ', '0')
    df.total_charges = df.total_charges.astype(float)
    
    # create dummies for binary columns and concat to df
    dummies = pd.get_dummies(df[['churn', 'gender', 'partner', 'dependents', 'phone_service',
                                 'paperless_billing']], drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    
    dummies = pd.get_dummies(df[['multiple_lines', 'online_security', 'online_backup','device_protection',
                                 'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 'payment_type',
                                 'internet_service_type']], drop_first=False)
    df = pd.concat([df, dummies], axis=1)
    
    # delete original columns where dummies were created
    df = df.drop(columns=['churn', 'gender', 'partner', 'dependents', 'phone_service',
                                 'paperless_billing', 'multiple_lines', 'online_security', 'online_backup',
                                 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
                                 'contract_type', 'payment_type','internet_service_type'])
    
    # clean up column names
    df.rename(columns={'churn_Yes' : 'churn', 'gender_Male': 'male', 'partner_Yes' : 'partner',
                       'dependents_Yes':'dependents', 'phone_service_Yes' : 'phone_service', 
                       'paperless_billing_yes':'paperless_billing'}, inplace=True)
    
    return df
    

    
def my_split(df, target):
    """
    Separates a dataframe into train, validate, and test datasets

    Keyword arguments:
    df: a dataframe containing multiple rows
    target:  a string containing the column name that will be the target of a model

    Returns:
    three dataframes who's length is 60%, 20%, and 20% of the length of the original dataframe
    """

    # separate into 80% train/validate and test data
    train_validate, test = train_test_split(df, test_size=.2, stratify=df[target])

    # further separate the train/validate data into train and validate
    train, validate = train_test_split(train_validate, 
                                       test_size=.25, 
                                       stratify=train_validate[target])

    return train, validate, test