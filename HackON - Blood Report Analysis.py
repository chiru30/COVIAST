#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[24]:


import matplotlib.pyplot as plt
import seaborn as sns
covid19_dataset = pd.read_csv('dataset-blood report analysis.csv')


# In[25]:


pd.set_option('display.max_row', 111)
pd.set_option('display.max_column', 111)


# In[26]:


df = covid19_dataset.copy()
df.shape


# In[27]:


df.head(3)


# In[28]:


df.columns


# In[29]:


df.rename(columns={'Patient age quantile':"Age",'SARS-Cov-2 exam result':"exam_result",
                   'Patient addmited to regular ward (1=yes, 0=no)':"regular_ward",
                   'Patient addmited to semi-intensive unit (1=yes, 0=no)':"semi-intensive",
                   'Patient addmited to intensive care unit (1=yes, 0=no)':"intensive",
                   "Mean platelet volume ":"platelet_volume","Red blood Cells":"RBC",
                   
                  "Mean corpuscular hemoglobin (MCH)":"MCH","Mean corpuscular volume (MCV)":'MCV',
                  "Red blood cell distribution width (RDW)":"RDW",
                  "Serum Glucose":"serum_glocose","Proteina C reativa mg/dL":"Proteina"},inplace=True)


# In[30]:


df.columns


# In[31]:


df.head(3)


# In[32]:


df.dtypes.value_counts().plot.pie()


# In[10]:


plt.figure(figsize=(20,10))
sns.heatmap(df.isna(), cbar=False)


# In[11]:


(df.isna().sum()/df.shape[0]).sort_values(ascending=True)


# In[12]:


df = df[df.columns[df.isna().sum()/df.shape[0] <0.9]]
df.head()


# In[13]:


plt.figure(figsize=(20,10))
sns.heatmap(df.isna(), cbar=False)


# In[33]:


df['exam_result'].value_counts(normalize=True)


# In[16]:


for col in df.select_dtypes('float'):
    plt.figure()
    sns.distplot(df[col])


# In[18]:


sns.distplot(df['Age'], bins=20)


# In[34]:


for col in df.select_dtypes('object'):
    print(f'{col :-<50} {df[col].unique()}')


# In[20]:


for col in df.select_dtypes('object'):
    plt.figure()
    df[col].value_counts().plot.pie()


# In[35]:


positive_df = df[df['exam_result'] == 'positive']
negative_df = df[df['exam_result'] == 'negative']

# Blood and viral data creation 
missing_rate = df.isna().sum()/df.shape[0]
blood_columns = df.columns[(missing_rate < 0.9) & (missing_rate >0.88)]
viral_columns = df.columns[(missing_rate < 0.88) & (missing_rate > 0.75)]


# In[23]:


for col in blood_columns:
    plt.figure()
    sns.distplot(positive_df[col], label='positive')
    sns.distplot(negative_df[col], label='negative')
    plt.legend()


# In[25]:


sns.countplot(x='Age', hue='exam_result', data=df)


# In[26]:


for col in viral_columns:
    plt.figure()
    sns.heatmap(pd.crosstab(df['exam_result'], df[col]), annot=True, fmt='d')


# In[27]:


sns.pairplot(df[blood_columns])


# In[28]:


sns.clustermap(df[blood_columns].corr())


# In[36]:


missing_rate = df.isna().sum()/df.shape[0]

blood_columns = list(df.columns[(missing_rate < 0.9) & (missing_rate >0.88)])
viral_columns = list(df.columns[(missing_rate < 0.80) & (missing_rate > 0.75)])


# In[37]:


key_columns = ['Age', 'exam_result']


# In[38]:


df = df[key_columns + blood_columns + viral_columns]
df.head()


# In[26]:


#df.columns


# In[27]:


#df.rename(columns={'Patient age quantile':"Age",'SARS-Cov-2 exam result':"exam_result","Mean platelet volume ":
                  #"platelet_volume","Red blood Cells":"RBC","Mean corpuscular hemoglobin concentration (MCHC)":"MCHC",
                  #"Mean corpuscular hemoglobin (MCH)":"MCH","Mean corpuscular volume (MCV)":'MCV',
                  #"Red blood cell distribution width (RDW)"},inplace=True)


# In[56]:


df.columns


# In[39]:


df.head(3)


# In[40]:


from sklearn.model_selection import train_test_split
trainset, testset = train_test_split(df, test_size=0.2, random_state=0)


# In[41]:


def encoding(df):
    code = {'negative':0,
            'positive':1,
            'not_detected':0,
            'detected':1}
    
    for col in df.select_dtypes('object').columns:
        df.loc[:,col] = df[col].map(code)
        
    return df


# In[42]:


def feature_engineering(df):
    df['is_sick'] = df[viral_columns].sum(axis=1) >= 1
    df = df.drop(viral_columns, axis=1)
    return df


# In[43]:


def imputation(df):
    df = df.dropna(axis=0)
    return  df


# In[44]:


def preprocessing(df):
    df = encoding(df)
    df = feature_engineering(df)
    df = imputation(df)
    X = df.drop('exam_result', axis=1)
    y = df['exam_result']
    print(y.value_counts())
    return X, y


# In[45]:


X_train, y_train = preprocessing(trainset)


# In[46]:


X_test, y_test = preprocessing(testset)


# In[47]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


# In[48]:


preprocessor = make_pipeline(PolynomialFeatures(2, include_bias=False), SelectKBest(f_classif, k=10))


# In[49]:


RandomForest = make_pipeline(preprocessor, RandomForestClassifier(random_state=0))
AdaBoost = make_pipeline(preprocessor, AdaBoostClassifier(random_state=0))
SVM = make_pipeline(preprocessor, StandardScaler(), SVC(random_state=0))
KNN = make_pipeline(preprocessor, StandardScaler(), KNeighborsClassifier())


# In[50]:


dict_of_models = {'RandomForest': RandomForest,
                  'AdaBoost' : AdaBoost,
                  'SVM': SVM,
                  'KNN': KNN
                 }


# In[51]:


from sklearn.metrics import f1_score, confusion_matrix, classification_report
from sklearn.model_selection import learning_curve


# In[52]:


def evaluation(model):
    model.fit(X_train, y_train)
    ypred = model.predict(X_test)
    print(confusion_matrix(y_test, ypred))
    print(classification_report(y_test, ypred))
    N, train_score, val_score = learning_curve(model, X_train, y_train,
                                              cv=4, scoring='f1',
                                               train_sizes=np.linspace(0.1, 1, 10))
 
    plt.figure(figsize=(12, 8))
    plt.plot(N, train_score.mean(axis=1), label='train score')
    plt.plot(N, val_score.mean(axis=1), label='validation score')
    plt.legend()


# In[53]:


for name, model in dict_of_models.items():
    print(name)
    evaluation(model)


# In[54]:


from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


# In[55]:


SVM


# In[56]:


hyper_params = {'svc__gamma':[1e-3, 1e-4, 0.0005],
                'svc__C':[1, 10, 100, 1000, 3000], 
               'pipeline__polynomialfeatures__degree':[2, 3],
               'pipeline__selectkbest__k': range(45, 60)}


# In[57]:


grid = RandomizedSearchCV(SVM, hyper_params, scoring='recall', cv=4,
                          n_iter=40)

grid.fit(X_train, y_train)

print(grid.best_params_)

y_pred = grid.predict(X_test)

print(classification_report(y_test, y_pred))


# In[58]:


X_train


# In[73]:


X_train.columns


# In[59]:


y_train


# In[60]:


evaluation(grid.best_estimator_)


# In[61]:


from sklearn.metrics import precision_recall_curve


# In[62]:


precision, recall, threshold = precision_recall_curve(y_test, grid.best_estimator_.decision_function(X_test))


# In[63]:


plt.plot(threshold, precision[:-1], label='precision')
plt.plot(threshold, recall[:-1], label='recall')
plt.legend()


# In[64]:


def model_final(model, X, threshold=0):
    return model.decision_function(X) > threshold


# In[65]:


y_pred = model_final(grid.best_estimator_, X_test, threshold=-1)


# In[66]:


from sklearn.metrics import recall_score


# In[67]:


f1_score(y_test, y_pred)


# In[68]:


recall_score(y_test, y_pred)


# In[69]:


import pickle


# In[70]:


pkl_file= open('blood_report.pkl',"wb")


# In[71]:


pickle.dump(model,pkl_file)


# In[72]:


pkl_file.close()

