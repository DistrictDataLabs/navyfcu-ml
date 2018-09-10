# Bank Marketing

**Downloaded from the UCI Machine Learning Repository on September 8, 2018.**

- Data Set: Multivariate
- Categorical, Real Attributes
- 41188 Instances
- 20 Attributes
- Well suited for _classification_ tasks
- [https://archive.ics.uci.edu/ml/datasets/bank+marketing](https://archive.ics.uci.edu/ml/datasets/bank+marketing)

## Abstract

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. The classification goal is to predict if the client will subscribe (yes/no) a term deposit (variable y).

## Description

We propose a data mining (DM) approach to predict the success of telemarketing
calls for selling bank long-term deposits. A Portuguese retail bank was addressed, with data collected from 2008 to 2013, thus including the effects of the recent financial crisis. We analyzed a large set of 150 features related with bank client, product and social-economic attributes. A semi-automatic feature selection was explored in the modeling phase, performed with the data prior to July 2012 and that allowed to select a reduced set of 22 features. We also compared four DM models: logistic regression, decision trees (DT), neural network (NN) and support vector machine. Using two metrics, area of the receiver operating characteristic curve (AUC) and area of the LIFT cumulative curve (ALIFT), the four models were tested on an evaluation phase, using the most recent data (after July 2012) and a rolling windows scheme. The NN presented the best results (AUC=0.8 and ALIFT=0.7), allowing to reach 79% of the subscribers by selecting the half better classified clients. Also, two knowledge extraction methods, a sensitivity analysis and a DT, were applied to the NN model and revealed several key attributes (e.g., Euribor rate, direction of the call and bank agent experience). Such knowledge extraction confirmed the obtained model as credible and valuable for telemarketing campaign managers.

### Attributes

**Client data attributes**
1. age (numeric)
2. job : type of job (categorical):
    'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown'
3. marital : marital status (categorical):
    'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed
4. education (categorical):
    'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown'
5. default: has credit in default? (categorical):
    'no','yes','unknown'
6. housing: has housing loan? (categorical):
    'no','yes','unknown'
7. loan: has personal loan? (categorical):
    'no','yes','unknown'

**Related with the last contact of the current campaign**
8. contact: contact communication type (categorical):
    'cellular','telephone'
9. month: last contact month of year (categorical):
    'jan', 'feb', 'mar', ..., 'nov', 'dec'
10. day_of_week: last contact day of the week (categorical):    
    'mon','tue','wed','thu','fri'
11. duration: last contact duration, in seconds (numeric).
    Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.

**Other attributes**
12. campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
13. pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
14. previous: number of contacts performed before this campaign and for this client (numeric)
15. poutcome: outcome of the previous marketing campaign (categorical):
    'failure','nonexistent','success'

**Social and economic context attributes**
16. emp.var.rate: employment variation rate - quarterly indicator (numeric)
17. cons.price.idx: consumer price index - monthly indicator (numeric)
18. cons.conf.idx: consumer confidence index - monthly indicator (numeric)
19. euribor3m: euribor 3 month rate - daily indicator (numeric)
20. nr.employed: number of employees - quarterly indicator (numeric)

**Output variable (desired target)**
21. y - has the client subscribed a term deposit? (binary): 'yes','no'

### Citation

Moro, Sérgio, Paulo Cortez, and Paulo Rita. "A data-driven approach to predict the success of bank telemarketing." Decision Support Systems 62 (2014): 22-31.

```
@article{moro2014data,
  title={A data-driven approach to predict the success of bank telemarketing},
  author={Moro, S{\'e}rgio and Cortez, Paulo and Rita, Paulo},
  journal={Decision Support Systems},
  volume={62},
  pages={22--31},
  year={2014},
  publisher={Elsevier}
}
```
