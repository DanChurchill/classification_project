from IPython.display import display_html 


def correlation_report(df, target):
    '''
    Function to display two side-by-side dataframes of correlation data for the value of churn
    The table on the left shows the top 14 columns by highest absolute value of correlation
    The table on the right shows the top 14 columns by lowest absolute value of correlation
    The #1 correlated column will be the target with itself (value = 1) and is omitted

    function accepts a dataframe 
    '''
    corr = abs(df.corr()[[target]]).sort_values(by=target, ascending=False)
    corr.rename(columns={'churn' : 'Correlation'}, inplace=True)
    corr1 = corr.iloc[1:12]
    corr2 = corr.iloc[:22:-1]
    df1_style = corr1.style.set_table_attributes("style='display:inline; margin-right:100px;'").set_caption("Most Correlation")
    df2_style = corr2.style.set_table_attributes("style='display:inline'").set_caption("Least Correlation")

    display_html(df1_style._repr_html_() + df2_style._repr_html_(), raw=True)


