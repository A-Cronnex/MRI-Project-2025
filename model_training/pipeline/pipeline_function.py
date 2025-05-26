import matplotlib.pyplot as plt
from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score 
import numpy as np

def pipeline_preprocess(X_new, rf_indices, anova_selector, trained_model,scaler):
    X_scaled = scaler.transform(X_new)
    
    # Step 2: Select RF Top Features
    X_rf_selected = X_scaled[:, rf_top_indices]
    
    # Step 3: Apply ANOVA selector
    X_anova_selected = anova_selector.transform(X_rf_selected)
    
    # Step 4: Predict
    return trained_model.predict(X_anova_selected)

    