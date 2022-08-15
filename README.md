# <a name="top"></a>TELCO - CLASSIFICATION PROJECT
![]()

by: Dan Churchill

<p>
  <a href="https://github.com/DanChurchill" target="_blank">
    <img alt="Dan" src="https://img.shields.io/github/followers/DanChurchill?label=Follow_Dan&style=social" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___



## <a name="project_description"></a>Project Description:
[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:


        
### Hypothesis



### Target variable


### Need to haves (Deliverables):



### Nice to haves (With more time):



***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| customer_id | Unique id for each customer| str |
| senior_citizen| 1 if customer is a senior citizen | int |
| tenure | Months of tenure as a customer| int |
| monthly_charges| The customer's monthly bill| float |
| total_charges| The customer's total bills since they have been a customer| float|
| male | 1 if the customer is male | int |
| multiple_lines_no | 1 if the customer has phone service but only one line | int |
| multiple_lines_no_phone | 1 if the customer has no phone service | int |
| multiple_lines_yes | 1 if the customer has multiple phone lines | int |
| online_security_no | 1 if the customer has internet but no online security | int |
| online_security_no_internet | 1 if the customer has no internet  | int |
| online_security_yes | 1 if the customer has online security | int |
| online_backup_no | 1 if the customer has internet but no online backup | int |
| online_backup_no_internet | 1 if the customer has no internet  | int |
| online_backup_yes | 1 if the customer has online backup | int |
| device_protection_no | 1 if the customer has internet but no device protection | int |
| device_protection_no_internet | 1 if the customer has no internet  | int |
| device_protection_yes | 1 if the customer has device protection | int |
| tech_support_no | 1 if the customer has internet but no tech support | int |
| tech_support_no_internet | 1 if the customer has no internet  | int |
| tech_support_yes | 1 if the customer has tech_support | int |
| streaming_tv_no | 1 if the customer has internet but no streaming tv | int |
| streaming_tv_no_internet | 1 if the customer has no internet  | int |
| streaming_tv_yes | 1 if the customer has streaming tv | int |
| streaming_movies_no | 1 if the customer has internet but no streaming movies | int |
| streaming_movies_no_internet | 1 if the customer has no internet  | int |
| streaming_movies_yes | 1 if the customer has streaming movies | int |
| contract_type_month-to-month | 1 if the customer has a month-to-month contract | int |
| contract_type_one_year | 1 if the customer has a one year contract  | int |
| contract_type_two_year | 1 if the customer has a two year contract | int |
| payment_type_bank_transfer_auto | 1 if the customer pays by automatic bank transfer | int
| payment_type_credit_card_auto | 1 if the customer pays automatically by credit card | int
| payment_type_electronic_check | 1 if the customer pays manually by electronic check | int
| payment_type_mailed_check | 1 if the customer pays manually by mailed check | int
| internet_type_dsl  | 1 if the customer has DSL internet service |  int
| internet_type_fiber_optic | 1 if the customer has fiber optic internet service | int
| internet_type_none | 1 if the customer has no internet | int
| addon_count | sum of how many internet service add-ons the customer has | int

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Wrangle steps: 


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - wrangle.py 
    - explore.py
    - modeling.py


### Takeaways from exploration:


***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### Stats Test 1: ANOVA Test: One Way

Analysis of variance, or ANOVA, is a statistical method that separates observed variance data into different components to use for additional tests. 

A one-way ANOVA is used for three or more groups of data, to gain information about the relationship between the dependent and independent variables: in this case our clusters vs. the log_error, respectively.

To run the ANOVA test in Python use the following import: \
<span style="color:green">from</span> scipy.stats <span style="color:green">import</span> f_oneway

- f_oneway, in this case, takes in the individual clusters and returns the f-statistic, f, and the p_value, p:
    - the f-statistic is simply a ratio of two variances. 
    - The p_vlaue is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:


#### Summary:


### Stats Test 2: T-Test: One Sample, Two Tailed
- A T-test allows me to compare a categorical and a continuous variable by comparing the mean of the continuous variable by subgroups based on the categorical variable
- The t-test returns the t-statistic and the p-value:
    - t-statistic: 
        - Is the ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error. It is used in hypothesis testing via Student's t-test. 
        - It is used in a t-test to determine if you should support or reject the null hypothesis
        - t-statistic of 0 = H<sub>0</sub>
    -  - the p-value:
        - The probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct
- We wanted to compare the individual clusters to the total population. 
    - Cluster1 to the mean of ALL clusters
    - Cluster2 to the mean of ALL clusters, etc.

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is 
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:


#### Summary:

***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
    

- Selected features to input into models:
    - features = []

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:

    

- Other indicators of model performance with breif defiition and why it's important:

    
    
#### Model 1: Linear Regression (OLS)


- Model 1 results:



### Model 2 : Lasso Lars Model


- Model 2 results:


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:


### Model 4: Quadratic Regression Model

- Model 4 results:


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline | 0.167366 | 2.2204 x 10<sup>-16</sup> |
| Linear Regression (OLS) | 0.166731 | 2.1433 x 10<sup>-3</sup> |  
| Tweedie Regressor (GLM) | 0.155186 | 9.4673 x 10<sup>-4</sup>|  
| Lasso Lars | 0.166731 | 2.2204 x 10<sup>-16</sup> |  
| Quadratic Regression | 0.027786 | 2.4659 x 10<sup>-3</sup> |  


- {} model performed the best


## Testing the Model

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]

