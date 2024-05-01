## Supervised Learning
- The model or algorithm is presented with example inputs and their desired outputs, and then finds patterns and connections between the input and the output
    - Image Classifications
    - Market Prediction/Regression

## Unsupervised Learning
- No labels are given to the learning algorithm, leaving it on its own to find structure in its input.
    - Clustering
    - High-Dimension Visualization
    - Generative Models

## Semi-supervised learning
- Problems where you have a large amount of input data and only some of the data is labeled are called semi-supervised learning problems.These problems sit in between both supervised and unsupervised learning.
    - A photo archive where only some of images are labeled and the majority are unlabeled

## Reinforcement learning
- A computer programa interacts with a dynamic environment in which it must perform a certain goal (such as driving a vehicle or playing a game against an opponent). The program is provided feedback in terms of rewards and punishments as it navigates its problem space.

### Classification
- Supervised learning
    - Binary Classification
        - spam filtering is an example of binary classification.
    - Multiclass Classification

### Regressions
- Supervised learning
    - predicts a numeric value and outputs are continuous rather than discrete.

### Clustering
- Unsupervised learning
    - set of inputs divided in group

### Density Estimation
- Unsupervised learning
    - the task is to find the distribution of inputs in some space

### Dimensionality rediction
- Unsupervised learning
    - It simplifies inputs by mapping them into a lower-dimensional space.Topic modeling is a related problem, where a program is given a list of human language documents and is tasked to find out which documents cover similar topics.

### Algorithms
- Linear Regression
- Logistic Regression
- Decision Tree
- SVM(Support vector machines)
- Naive Bayes
- KNN(K nearest neighbors)
- K-Means
- Random Forest

### Terminologies
- Model - A model is a specific representation learned from data by applying some machine learning algorithm. A model is also called a hypothesis.
- Feature - A feature is an individual measurable property of our data.For example in order to predict a fruit, there may be features like color, smell, taste, etc.
- Target - A target variable of label is the value to be predicted by our model. for the fruit prediction the label would be the name of the fruit.
- Training - The idea is to give a set of inputs(features) and its expected output(labels), so after training, we will have a model (hypothesis) that will then map new data to one of the categories trained on.
- Prediction