import pandas as pd
from sklearn.model_selection import train_test_split


def prep_telco(df):
    """
    Performs preparations on the telco DataFrame in order to make it usable for data exploration and modeling
    - Encodes Yes/No columns to binary
    - Changes column names to lower case, removes spaces and parenthesis
    - Creates column addon_count, and integer representing the number of internet service add-ons

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
    
    # encode binary columns with 1 and 0 instead of 'Yes' and 'No' (dropping first)
    dummies = pd.get_dummies(df[['gender', 'partner', 'dependents', 'phone_service', 
                                 'paperless_billing', 'churn']], drop_first=True)
    
    # drop the unencoded versions
    df = df.drop(columns=['churn','partner','dependents', 'phone_service', 'paperless_billing'])

    # rename the created dummy columns as necessary 
    dummies.rename(columns = {'churn_Yes':'churn',
                            'paperless_billing_Yes' : 'paperless_billing',
                            'phone_service_Yes': 'phone_service',
                            'dependents_Yes': 'dependents', 
                            'gender_Male': 'male',
                            'partner_Yes' : 'partner'}, inplace = True)
    
    # concat to df
    df = pd.concat([df, dummies], axis=1)

    # for columns with 3/4 values, encode and do not drop first
    dummies2 = pd.get_dummies(df[['multiple_lines', 'online_security', 'online_backup', 'device_protection',
                                'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 
                                'payment_type', 'internet_service_type']], drop_first=False)

    # concat to df
    df = pd.concat([df, dummies2], axis=1)

    # remove unencoded columns
    df = df.drop(columns=['gender', 'multiple_lines', 'online_security', 'online_backup', 
                        'device_protection', 'tech_support', 'streaming_tv', 
                        'streaming_movies', 'contract_type', 'payment_type', 'internet_service_type'])


    # clean up column names.  Lower case, replace spaces with underscore, remove parenthesis, and shorten add-on names
    df.columns = map(str.lower, df.columns)
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('_service', '')
    df.columns = df.columns.str.replace("automatic", 'auto').str.replace('(', '').str.replace(')', '')

    # remove columns later determined to not be needed
    df = df.drop(columns=['multiple_lines_no', 'multiple_lines_no_phone', 'device_protection_no_internet', 
                          'online_backup_no_internet', 'streaming_movies_no_internet', 'streaming_tv_no_internet',
                          'tech_support_no_internet', 'online_security_no_internet'])
    
    # create column with # of add_ons
    df['addon_count'] = df['online_security_yes'] + df['online_backup_yes'] + df['device_protection_yes'] + df['tech_support_yes'] + df['streaming_tv_yes'] + df['streaming_movies_yes']
    
    # return the prepared DataFrame
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
    train_validate, test = train_test_split(df, test_size=.2, stratify=df[target], random_state=333)

    # further separate the train/validate data into train and validate
    train, validate = train_test_split(train_validate, 
                                       test_size=.25, 
                                       stratify=train_validate[target], random_state=333)

    return train, validate, test