import pandas as pd
from sklearn.model_selection import train_test_split


def prep_telco(df):
    """
    Performs preparations on the telco DataFrame in order to make it usable for data exploration and modeling

    Keyword arguments:
    df: a dataframe containing customer data from the telco database

    Returns:
    prepared DataFrame
    """
    # delete index columns
    df = df.drop(columns=['internet_service_type_id', 'payment_type_id', 'contract_type_id'])
    
    # convert total charges from string to floats
    df.total_charges = df.total_charges.str.replace(' ', '0')
    df.total_charges = df.total_charges.astype(float)
    
    # create dummies for columns with binary values (and drop first)
    dummies = pd.get_dummies(df[['gender', 'partner', 'dependents', 'phone_service', 
                             'paperless_billing', 'churn']], drop_first=True)

    df = df.drop(columns=['churn'])
    # rename the dummy columns as necessary and add to df
    dummies.rename(columns = {'churn_Yes':'churn',
                            'paperless_billing_Yes' : 'paperless_billing',
                            'phone_service_Yes': 'phone_service',
                            'dependents_Yes': 'dependents', 
                            'gender_Male': 'male',
                            'partner_Yes' : 'partner'}, inplace = True)
    
    # concat to df
    df = pd.concat([df, dummies], axis=1)

    # for columns with 3/4 values, encode and do not drop first column
    dummies2 = pd.get_dummies(df[['multiple_lines', 'online_security', 'online_backup', 'device_protection',
                                'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 
                                'payment_type', 'internet_service_type']], drop_first=False)

    # concat to df
    df = pd.concat([df, dummies2], axis=1)

    # remove extra columns
    df = df.drop(columns=['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines',
                'online_security', 'online_backup', 'device_protection', 'tech_support', 
                'streaming_tv', 'streaming_movies', 'paperless_billing', 
                'contract_type', 'payment_type', 'internet_service_type'])


    # clean up column names.  Lower case, replace spaces with underscore, and shorten add-on names
    df.columns = map(str.lower, df.columns)
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('_service', '')
    df.columns = df.columns.str.replace("automatic", 'auto').str.replace('(', '').str.replace(')', '')

    
    # create column with # of add_ons
    df['addon_count'] = df['online_security_yes'] + df['online_backup_yes'] + df['device_protection_yes'] + df['tech_support_yes'] + df['streaming_tv_yes'] + df['streaming_movies_yes']
    
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