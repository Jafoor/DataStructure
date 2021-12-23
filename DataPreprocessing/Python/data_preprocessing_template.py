# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv('Data.csv') 
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values


# Taking care of missing data
# =============================================================================
# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
# print(imputer)
# imputer = imputer.fit(X[:, 1:3])
# print(imputer)
# X[:, 1:3] = imputer.transform(X[:, 1:3])
# =============================================================================

# =============================================================================
# Encoding Categorical data
# =============================================================================

# =============================================================================
# from sklearn.preprocessing import OneHotEncoder, LabelEncoder
# from sklearn.compose import ColumnTransformer
# ct = ColumnTransformer([("Country", OneHotEncoder(), [0])], remainder = 'passthrough')
# X = ct.fit_transform(X)
# 
# labelencoder_y = LabelEncoder()
# Y = labelencoder_y.fit_transform(Y)
# =============================================================================


# =============================================================================
# Spliting the dataset into Training set test set
# =============================================================================
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


# =============================================================================
# Feature scling
# =============================================================================
# =============================================================================
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
# X_test[:, 3:] =  sc.fit_transform(X_test[:, 3:])
# =============================================================================
