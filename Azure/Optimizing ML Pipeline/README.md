# Optimizing an ML Pipeline in Azure

## Overview
This project is part of the Udacity Azure ML Nanodegree.
In this project, we build and optimize an Azure ML pipeline using the Python SDK and a provided Scikit-learn model.
This model is then compared to an Azure AutoML run.

## Summary
This dataset is about the direct phone call marketing campaigns, which aim to promote term deposits among existing customers, by a Portuguese banking institution from May 2008 to November 2010. It is publicly available in the UCI Machine Learning Repository, which can be retrieved from kaggle or http://archive.ics.uci.edu/ml/datasets/Bank+Marketing#.predict. Main goal is to predict customers' response('y') i.e. if customer would opt for the bank's product being campaigned.

**In 1-2 sentences, explain the solution: e.g. "The best performing model was a ..."**

## Scikit-learn Pipeline

Scikit-learn pipeline architecture can be described as below - 
1. Data Cleaning - Data cleaning and One Hot encoding was done by using a function in train.py
2. Data Splitting - Data was split into training and testing
3. Model Creation - "LogisticRegression" was selected as the classification algorithm
4. Hyper-parameter tuning by creating HyperDrive configuration for logistic regression. Parameter Sampling and Early stopping policy were used for sampling the hyper-parameters and to make sure that the processing does not run idefinitely.
- Parameter Sampling 
        - Unifrom sampling is suitable for continous parameters and hence it was used for regularization c
        - Choice sampling is suitable for discrete parameters and hence it was selected to sample max_iterations
        
- Early Stopping
        - Early stoppingallows to terminate the poorly performing runs. In this Bandit Policy which is based on slack factor/slack amount and evaluation terminals runs where ther primary mettric )(accuracy) is not within specified slack factor compared to the best performing run.


                                                 **Best Model **
![image.png](attachment:image.png)


## AutoML

AutoML generated a number of models with the best model as MaxAbsScaler LightGBM with an accuracy of 0.9150

TBA

## Pipeline comparison
The results of the primary metric i.e. Accuracy are pretty close:

Hyperdrive Accuracy: 0.9115
AutoMl Accuravy: 0.9150

Even though in this use case there was not a huge difference in results but there's a lot of difference between the two piplines.

Creating the model with Auto ML meant only specifying the configuration of the Auto ML and there is no work required to be done for data cleaning, feaure engineering, hyper paramtere selection & tunining or model selection. AutoML reduces the amount of effort and brought out model with ease.

## Future work
**What are some areas of improvement for future experiments? Why might these improvements help the model?**

Below are some suggestions for further improving the experiments - 

- Balancing the data - Balancing the data with up or downsampling will help in datset balancing and improved model performance.
- Metrics - Review further and use suitable metrics such as precion/recall, F1 score. Since this is an unbalaced dataset - confusion matrix would be very helpful
- Feature slection - Apply some domain expertise and keep only desired features. Feature slection using feature correlation and feature importance would help in reducing unecssary features.


```

```
