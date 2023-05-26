# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The goal of this project is to develop a loan approval prediction system using machine learning techniques. The system will take applicant data as input and predict whether the loan application should be approved or rejected

## Hypothesis
The hypothesis is that certain subsets of applicants will be more likely to have their loan applications approved. For example, applicants with a higher credit history score, higher income, and lower loan amount may have a higher probability of loan approval. To test this hypothesis, we will analyze the dataset and check the relationships between various features and the loan approval status. We will also use machine learning algorithms to identify important features and check their impact on loan approval predictions.
## EDA 
During the exploratory data analysis (EDA) phase, we discovered various insights about the dataset. We analyzed the distribution of features, checked for missing values, and assessed the balance between approved and rejected loan applications


## Process
Data Cleaning: We addressed missing values by imputing or removing them appropriately. We also performed data preprocessing tasks such as handling categorical variables, scaling numerical features, and transforming features

Feature Engineering: We created new features, such as adding a 'TotalIncome' column and taking the logarithm of 'TotalIncome'. These engineered features aimed to capture additional information that could improve the predictive power of the model.

## Results/Demo
Below are the findings

1. Graduates have a higher loan approval rate (70.83%) compared to non-graduates (61.19%).Educational background plays a role in loan approval decisions.
2. Loan approval rates for males and females are 69.12% and 66.96%, respectively.The difference in loan approval rates between genders is relatively small.
3. Married individuals have a higher loan approval rate (71.82%) compared to unmarried individuals (62.91%).Marital status appears to be a factor influencing loan approval.
4. Applicants with a credit history of 1.0 (good credit) have a loan approval rate of 79.05%.However, applicants with a credit history of 0.0 (no credit or bad credit) face a lower loan approval rate of 7.87%.
5. The income ranges are categorized into different bins based on the applicant's income. Applicants with higher incomes tend to have a slightly higher loan approval rate.Applicants in the income range of (7500.0, 10000.0] have the highest loan   approval rate of 73.17%.Applicants in the income range of (0.0, 2500.0] and (10000.0, inf] have loan approval rates of around 68-69%.Applicants in the income range of (2500.0, 5000.0] and (5000.0, 7500.0] have loan approval rates of around 68-68.5%.
Applicants in the income range of (7500.0, 10000.0] have a lower rejection rate of 26.83%.

Below are the results for ML models

Logistic regression - Accuracy: 0.7804
Grid Search - Accuracy: 0.7886
Random Forest Accuracy: 0.7804
SVM Accuracy: 0.7886
Gradient Boosting Accuracy: 0.7642
Decision Tree Accuracy: 0.7154





## Challanges 
The biggest challange was to deploy on AWS since there are a lot of configurations required for the cloud. 

## Future Goals
Given more time further work can be done to try more models like Naive Bayes and improve the accuracy of the models. ALso further hyperparamter tuning can be explored for better results