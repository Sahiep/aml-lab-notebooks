# ### Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import joblib
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn_pandas import DataFrameMapper
from interpret.ext.blackbox import TabularExplainer
from azureml.interpret import ExplanationClient
import os
import pandas as pd
os.system('pip freeze')


from azureml.core import Run, Workspace, Experiment
import azureml.core
print("SDK version:", azureml.core.VERSION)

OUTPUT_DIR='./outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

print('load dataset')

run = Run.get_context()
if(run.id.startswith("OfflineRun")):
    ws = Workspace.from_config()
    experiment = Experiment(ws, "Train-Explain-Interactive")
    is_remote_run = False
    run = experiment.start_logging(outputs=None, snapshot_directory=".")
    creditData = ws.datasets['german-credit'].to_pandas_dataframe()
else:
    ws = run.experiment.workspace
    creditData = run.input_datasets['credit'].to_pandas_dataframe()
    is_remote_run = True

print(creditData.head())

# Dropping Employee count as all values are 1 and hence attrition is independent of this feature
creditData = creditData.drop(['Sno'], axis=1)
creditData["Risk_cat"] = creditData["Risk"].astype('category').cat.codes
creditData = creditData.drop(['Risk'], axis=1)

target = creditData["Risk_cat"]

creditXData = creditData.drop(['Risk_cat'], axis=1)

# Creating dummy columns for each categorical feature
categorical = []
for col, value in creditXData.iteritems():
    if value.dtype == 'object':
        categorical.append(col)

# Store the numerical columns in a list numerical
numerical = creditXData.columns.difference(categorical)

numeric_transformations = [([f], Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])) for f in numerical]

categorical_transformations = [([f], OneHotEncoder(handle_unknown='ignore', sparse=False)) for f in categorical]

transformations = numeric_transformations + categorical_transformations

# Append classifier to preprocessing pipeline.
# Now we have a full prediction pipeline.
clf = Pipeline(steps=[('preprocessor', DataFrameMapper(transformations)),
                      ('classifier', LogisticRegression(solver='lbfgs'))])

client = ExplanationClient.from_run(run)

# Split data into train and test
x_train, x_test, y_train, y_test = train_test_split(creditXData,
                                                    target,
                                                    test_size=0.2,
                                                    random_state=0,
                                                    stratify=target)


# write x_test out as a pickle file for later visualization
x_test_pkl = 'x_test.pkl'

joblib.dump(value=x_test, filename=os.path.join(OUTPUT_DIR, x_test_pkl))
run.upload_file('x_test_credit.pkl', os.path.join(OUTPUT_DIR, x_test_pkl))

print('train model')
# preprocess the data and fit the classification model
clf.fit(x_train, y_train)
model = clf.steps[-1][1]

# save model for use outside the script
model_file_name = 'log_reg.pkl'
joblib.dump(value=clf, filename=os.path.join(OUTPUT_DIR, model_file_name))

# register the model with the model management service for later use
run.upload_file('model.pkl', os.path.join(OUTPUT_DIR, model_file_name))
original_model = run.register_model(model_name='creditmodel_explainer_remote',
                                    model_path='model.pkl')

print('create explainer')
# create an explainer to validate or debug the model
tabular_explainer = TabularExplainer(model,
                                     x_train,
                                     features=creditXData.columns,
                                     classes=[0, 1],
                                     transformations=transformations)

# explain overall model predictions (global explanation)
# passing in test dataset for evaluation examples - note it must be a representative sample of the original data
# more data (e.g. x_train) will likely lead to higher accuracy, but at a time cost
global_explanation = tabular_explainer.explain_global(x_test)

print('upload explanation')
# uploading model explanation data for storage or visualization
comment = 'Global explanation on classification model trained on German credit dataset'
client.upload_model_explanation(global_explanation, comment=comment)

if not is_remote_run:
    run.complete()

print('completed')

