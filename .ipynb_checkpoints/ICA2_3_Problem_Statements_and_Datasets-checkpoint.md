ICA 2 – PROBLEM STATEMENTS & DATASETS

GROUP ALLOCATION  
\- Odd Group Number → Problem 1  
\- Even Group Number → Problem 2  
\- Each group consists of 2 students.

\============================================================  
PROBLEM 1 – E-COMMERCE CUSTOMER BEHAVIOUR, SEGMENTATION & CHURN  
\============================================================

BUSINESS SCENARIO

An online retailer wants to understand customer purchasing behaviour and identify customers who are at risk of becoming inactive. The company also wants to discover relationships between customers and products to improve targeted marketing and customer retention.

DATASET

UCI Online Retail II Dataset

Official Dataset Link:  
https\://archive.ics.uci.edu/dataset/502/online+retail+ii

The dataset contains transaction-level e-commerce data including invoice, product, quantity, date, unit price, customer and country information.
It contains missing values and cancelled transactions, requiring appropriate preprocessing.

TASK

A. DATA UNDERSTANDING & PREPROCESSING

1\. Explore the complete dataset.
2\. Identify missing values, duplicates, cancellations and unusual transactions.
3\. Decide how cancelled transactions should be treated and justify the decision.
4\. Create meaningful customer-level features.
5\. Define a suitable customer inactivity/churn target using the transaction history.
6\. Justify the definition of churn/inactivity.

B. NEO4J GRAPH MODELLING

Design and implement an e-commerce graph.

Possible nodes:
\- Customer
\- Product
\- Category/Product Group
\- Country
\- Transaction/Invoice

Possible relationships:  
\- Customer → PURCHASED → Product  
\- Customer → MADE → Transaction  
\- Transaction → CONTAINS → Product  
\- Product → BELONGS\_TO → Category  
\- Customer → LOCATED\_IN → Country

You may modify this structure if you can justify your design.

C. GRAPH ANALYSIS

Use Cypher to investigate:

1\. Which products are frequently purchased together?  
2\. Which products connect different customer groups?  
3\. Which customers have similar purchasing behaviour?  
4\. Which products/categories are strongly associated with high-value customers?  
5\. Which customers show weak or declining purchasing relationships?  
6\. Which graph characteristics could help identify inactive customers?

D. GRAPH-BASED FEATURE ENGINEERING

Create at least 4 meaningful features using Neo4j.

Examples:  
\- Number of unique products purchased by a customer.  
\- Number of product categories associated with a customer.  
\- Product co-purchase frequency.  
\- Number of customers connected through shared products.  
\- Customer/product network connectivity.  
\- Customer similarity-related measures.

The final features must be justified.

E. RAPIDMINER ML

Build a model to classify customers into appropriate activity/churn categories.

Requirements:  
1\. Compare at least 3 ML algorithms.  
2\. Use conventional customer features.  
3\. Incorporate Neo4j-derived features.  
4\. Use suitable validation.  
5\. Evaluate using appropriate classification metrics.  
6\. Explain important predictors.

F. CUSTOMER SEGMENTATION

Perform customer segmentation using an appropriate clustering technique.

Analyse:  
\- Characteristics of each segment.  
\- Product/category behaviour of each segment.  
\- Relationship between customer segments and churn/inactivity.

G. REQUIRED COMPARISON

Build and compare:

Model A – Customer features without graph features.

Model B – Customer features \+ Neo4j graph features.

Explain whether graph-based features improve the model and why.

FINAL QUESTION

Based on your analysis, how can the retailer use customer-product relationships and ML predictions to improve customer retention and targeted marketing?

\============================================================  
PROBLEM 2 – PREDICTIVE MAINTENANCE & MACHINE FAILURE ANALYSIS  
\============================================================

BUSINESS SCENARIO

A manufacturing organization wants to predict machine failures before they occur. The organization also wants to understand how machine characteristics, operating conditions and tool-wear relationships are associated with failures.

DATASET

UCI AI4I 2020 Predictive Maintenance Dataset

Official Dataset Link:  
https\://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

The dataset contains 10,000 observations and includes variables such as product type, air temperature, process temperature, rotational speed, torque, tool wear and machine failure.

TASK

A. DATA UNDERSTANDING & PREPROCESSING

1\. Perform complete data exploration.  
2\. Analyse the Machine Failure target.  
3\. Investigate class imbalance.  
4\. Analyse relationships between:  
   \- Air temperature  
   \- Process temperature  
   \- Rotational speed  
   \- Torque  
   \- Tool wear  
   \- Product type  
5\. Identify potential anomalies/outliers.  
6\. Apply appropriate preprocessing and justify each decision.

B. NEO4J GRAPH MODELLING

Create a graph representation of the manufacturing system.

Possible nodes:  
\- Machine  
\- Product  
\- Product Type  
\- Sensor/Measurement  
\- Operating Condition  
\- Failure  
\- Failure Type

Possible relationships:  
\- Machine → PRODUCES → Product  
\- Product → HAS\_TYPE → Product Type  
\- Machine → HAS\_READING → Measurement  
\- Measurement → HAS\_CONDITION → Operating Condition  
\- Machine → EXPERIENCES → Failure

The final graph structure must be justified.

C. GRAPH ANALYSIS

Use Neo4j/Cypher to investigate:

1\. Which operating conditions are associated with machine failures?  
2\. Which product types are more strongly connected with failures?  
3\. Which machines/conditions show similar behaviour?  
4\. Which sensor/measurement relationships are associated with failure?  
5\. Which combinations of operating conditions appear frequently before failure?  
6\. Can graph relationships identify potentially high-risk machines?

D. GRAPH-BASED FEATURE ENGINEERING

Create at least 4 meaningful graph-derived features.

Possible examples:  
\- Failure count associated with a machine/product type.  
\- Number of failure types connected to a machine.  
\- Frequency of a machine operating under high-risk conditions.  
\- Connectivity of a product type to failure events.  
\- Historical failure-related relationship count.  
\- Condition-based risk indicators.

The final features must be justified.

E. RAPIDMINER CLASSIFICATION

Build a machine-failure prediction model.

Target:  
Machine Failure

Requirements:  
1\. Compare at least 3 classification algorithms.  
2\. Address class imbalance appropriately.  
3\. Use suitable validation.  
4\. Evaluate using appropriate metrics such as:  
   \- Precision  
   \- Recall  
   \- F1-score  
   \- ROC-AUC  
   \- Confusion Matrix  
5\. Explain why the selected metrics are appropriate.

F. ADVANCED ANALYSIS

Create a second analytical task by predicting an appropriate risk category, for example:

\- Low Risk  
\- Medium Risk  
\- High Risk

The thresholds must be defined and justified using the available data.

Alternatively, students may develop an appropriate regression/score-based risk model if the target and methodology are clearly justified.

G. REQUIRED COMPARISON

Build and compare:

Model A – Sensor/product features without graph-derived features.

Model B – Sensor/product features \+ Neo4j graph-derived features.

Explain whether graph information provides additional predictive value.

FINAL QUESTION

Assume that the organization has limited maintenance capacity and cannot inspect every machine immediately.

Using your Neo4j analysis and ML results, how would you identify machines that require further investigation?

Your answer must be supported by evidence from your implementation.

\============================================================  
DATASET SOURCES  
\============================================================

Problem 1:  
UCI Online Retail II  
https\://archive.ics.uci.edu/dataset/502/online+retail+ii

Problem 2:
UCI AI4I 2020 Predictive Maintenance Dataset
https\://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset
