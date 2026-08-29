#%% loading of file
import sys
print(sys.executable)
import pandas as pd

df = pd.read_csv(r"C:\Users\Shubham Chouhan\OneDrive\Desktop\verbal_autospy\data\data.csv")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nTarget values:")
print(df["cause_of_death"].value_counts())
# %% separating variablles
Y = df["cause_of_death"]
X=df.drop(columns=["cause_of_death"])
for col in X.columns:
    print(col, X[col].unique())

# %% encoding the categorical values
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

categorical_columns = X.select_dtypes(include=["object"]).columns

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)
#%%split data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)
#%% train dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    ))
])

model.fit(X_train, y_train)
#%% evaluate 
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

print(classification_report(
    y_test,
    predictions
))

print(confusion_matrix(
    y_test,
    predictions
))
#%%cross validation
from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    model,
    X,
    Y,
    cv=5,
    scoring="f1_weighted"
)

print(scores)
print("Mean F1:", scores.mean())

model.fit(X_train, y_train)
#%% TESTING
print("Mean F1:", scores.mean())
print("F1 scores:", scores)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
#%% TRAINING PERFORMANCE
train_predictions = model.predict(X_train)

print("Training Accuracy:",
      accuracy_score(y_train, train_predictions))

print(classification_report(y_train, train_predictions))
#%% saving the model
import joblib

joblib.dump(
    model,
    "saved_model/verbal_autopsy_model.pkl"
)
# %%
