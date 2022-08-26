from IPython.display import display_html 
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_report(df, target):
    '''
    Function to display two side-by-side dataframes of correlation data for the value of churn
    The table on the left shows the top 11 columns by highest absolute value of correlation
    The table on the right shows the top 11 columns by lowest absolute value of correlation
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



def churn_plot(df, col):
    '''
    Function to display a plot with the binary distribution of a column in a dataframe.  
    Labels are currently set up to display churn, but they could be changed to utilize this function for another variable
    '''
    # calculate baseline mean for the print statements
    baseline = round(df[col].mean() ,4)

    # display countplot with axis labels and column totals above the bars
    x = sns.countplot(x =col, data = df)
    plt.title('Customers who churn')
    plt.gcf().set_size_inches(12, 6)
    plt.xticks([0,1],['No','Yes'])
    plt.xlabel('Churn')
    plt.ylabel('# of Customers')
    plt.bar_label(x.containers[0])
    plt.show()

    # print baseline results these would need to be changed if another column was to be used
    print('Our baseline for predictions is that ', baseline,' of customers churn')
    print('                            and that ',1-baseline,'of customers do not churn')



def internet_plot(df):
    '''
    Function to display a factor plot with the rate of churn for customers that do and do not
    have internet service 
    '''
    # create subsets of df for those with/without internet service
    internet = df[df.internet_type_none == 0]
    no_internet = df[df.internet_type_none == 1]

    # get baseline churn rate for the horizontal line
    baseline = round(df.churn.mean() ,4)

    # display factorplot
    p = sns.factorplot( x="internet_type_none", y="churn",  data=df, size=5, 
                   aspect=2, kind="bar", palette="muted", ci=None,
                   edgecolor=".2")
    plt.axhline(baseline, label = 'overall churn rate', ls='--')
    p.set_xticklabels(['Yes','No'])
    p.set_ylabels("Churn Rate")
    p.set_xlabels("Internet")
    plt.title('Do those with internet churn more?')
    plt.show()
    # compare rates of churn in each sample
    print('Churn rate of those with internet is', round(internet.churn.mean(),4))
    print('Churn rate of those without internet is', round(no_internet.churn.mean(),4))
    
