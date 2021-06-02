# ML Landscape

## What is ML

- ability for computer to learn without being programmed for it
- for coding a spam filter you will : Understand problem -> write complex rules -> evaluate solution :=> deploy application-> end :=> evaluate errors -> understand problem.
- for ML system : understand problem -> build a model using data -> evaluate solution :=> deploy model -> update data ->build model :=> analyze problem :=> analyze error -> understand problem.

## Where to use ML
- Traditional systems have very complex rules that are hard to maintain
- Traditional solutions do not work
- Environment is always changing
- Gain deeper insights by applying machine learning to the dataset. Data mining!!

## Types of ML

### Human Intervention

#### supervised:
- training set fed to the algorithm includes the correct labels
- classification and regression are two generic tasks accomplished by supervised.

##### classification task
- predicts the class from a set of labels in training set
- mail with class spam or ham and then predicting the class of a new email

##### regression task:
- predict a target value
- predicts a target value from a continuous distribution given a set of features
- some regression algorithms can be used for classification; logistic regression
- knn, linear regression, logistic regression, svm, decision tree, nn, 

#### unsupervised
- labels are not provided along with the training set. model learns groups on it's own.
- tasks: clustering, anomaly detection and novelty detection, visualization and dimensionality reduction, association rule learning

##### clustering
- grouping of samples based on feature(s)

##### anomaly detection
- finding an outlier

##### novelty detection
- identifying samples never seen before by the model

##### dimensionality reduction
- reducing the number of dimensions of the data by without losing too much information

##### association rule learning
- digs into large amount of data to learn a pattern

#### semi supervised
- when you have partially labelled data
- deep belief network

#### reinforcement learning
- agents observe environment and perform actions to learn better policies to maximize rewards

### Can learn incrementally?
- Key question to ask is how quickly the model needs to relearn

#### Online learning
- Once model is deployed, we retrain the model by feeding data in mini batches
- Good idea if the data is too huge to fit onto memory: out-of-core learning
- Key question to ask is how quickly your model should adapt to new data, defined by learning rate
- high lr means model adapts to the new data rapidly but also tend to quickly forget old data
- low lr means the model has more inertia, as a result the model learns new data slowly, however is more resilient to noise in the data
- a major challenge is how to you mitigate bad data. As model is fed bad data, the model performance may decline, prompt monitoring and applying anomaly detection is a good idea

#### batch learning
- system is incapable of learning incrementally
- model is trained offline and then it just applies what is has learnt, hence, offline learning
- To train model on newer data, you need to train on new+old data and then pull down older model and then deploy new model
- Requires large compute resource and storage
- Bad idea if model requires limited resources or data is rapidly changing
- Key question to ask is should your model adapt to new data

### How do they generalize?

#### instance based learning
- learn all samples by heart
- use certain measure of similarity to generalize to new case
- in case of spam we may learn word count to check if something is spam and use count of common words as a similarity measure

#### model based learning
- build a model and then predict 
- understand the data before *model selection*
- define *utility function* or *cost function* to asses _how good the model performs_
- find _parameters_ that _best fit_ the data during _training_
- apply model to new data during _inference_ to predict 

## ML Challenges

### Data based challenges

#### Insufficient data
- ML generally needs lots of data

#### Non representative data
- training set should represent the overall distribution
- respresent new cases to generalize on
- small samples have sampling noise(non-rep data by chance)
- sampling bais: poorly collected data

#### Poor quality data
- has outliers, noise and errors
- model can't detect underlying pattern
- solution: data cleaning

##### Outliers
- remove them
- manually correct them

#### Incomplete features
- ignore the feature
- ignore the samples
- fill the values
- train model with and without the feature

#### Irrelevant features
- good model need relevant features
- irrelevant features can screw the model
- feature engineering; coming up with good feature
- feature selection; select good relevant features
- feature extraction; combine features for better one
- create new feature by data gathering

#### Overfitting
- performs well on training set
- but doesn't generalize very well
- model may end up detecting pattern in noise
- model too complex; simply the model
- more training data
- reduce noise
- regularization; constraining the model
- hyperparameters control amount of regularization
- hyperparameters; params of algo not model

#### Underfitting
- Problem more complex than model
- more powerful model is solution
- feed better features to the model
- reduce constrains on the model

#### Testing and Validation

#### Test train sets
- use train set and test set
- error on test is generalization error or out-of-sampling error

#### Hyper parameter tuning and model selection
- if model tuned as per error on test set
- model adapts to test set, hence may not generalize well
- Solution holdout validation
- val set too small; imprecise evaluation
- val set too large; not enought data to train
- solution: cross validation

##### holdout validation
- create validation set
- find model that performs best on validation set
- train on val + train set and evaluate on test set

### Data Mismatch
- trained on set but production data is very different
- val and test set should represent production
- if model performs bad on val set; bad model or data mismatch
- create train-dev set, a subset of training set
- val set;bad, train-dev set;bad : overfitting
- val set bad, train\_dev set good, data mismatch

## References:
### Books
- Data Science from Scratch
- Machine Learning: An Algorithmic Perspective
- Deep Learning with Python
- Learning from Data
- Artificial Intelligence: A Modern Approach
### Papers
- [Scaling to very very large corpora for natural language disambiguation](https://dl.acm.org/doi/10.3115/1073012.1073017)
- [Unresonable effectiveness of data](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf)
- [No Free Lunch Theorem Paper](https://direct.mit.edu/neco/article/8/7/1341/6016/The-Lack-of-A-Priori-Distinctions-Between-Learning)