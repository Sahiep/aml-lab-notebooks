# Introducing Training ML models with AzureML 

## Objectives

In the following Excercise you will learn:
- Train a model using the Azure ML Designer
- Traing a model using Azure ML AutoML
- Train a model using the Azure ML Python SDK

## The AzureML Designer

### Prerequisites

To run through below instructions, you need an Azure subscription, an AzureML workspace and an AzureML compute target (i.e. **cpu-cluster**). See instructions on how to create a workspace [here](../../../0_setup/setup.md) and create an AzureML compute target [here](../../../1_concepts/concepts.md).

### Create an AzureML experiment using Designer

- In the AzureML studio, navigate to the Designer tab and click on it
  
  ![](./media/launch_designer.png)

- Create a new experiment buy opening Sample 3: Binary Classification with Feature Selection - Income Prediction from the list of available examples
  
  ![](./media/new_experiment.png)

- The graph for the sample experiment will open. You can inspect the properties of each of the steps, but you cannot see any outputs until you run the experiment. 
  
    ![](./media/census_income.png)

- In the setting tab, click on 'select compute target' and select the compute cluster we have created in the previous steps, **cpu-cluster**

  ![](./media/setting.png)

- Click 'submit' button at the top-right. Create a new experiment (e.g. **designer-exp**) and press 'Submit'
    ![](./media/experiment.png)

- Wait until all steps are done ( a green tick-mark appears on the corner of each step)

    ![](./media/finish.png)

- Once you ran the experiment, you can inspect the outputs of the individual steps -- check out the output of the different steps, in particular the "Evaluate Model" step. Click on the step, which will take you to the outputs:
    ![](./media/logs.png)


- Click on the "visualize" button in the "Evaluation results' tab which will show a graphical representation for the binary classification evaluation and the predicted values for the test data:
    ![](./media/visualize.png)

## Automated Machine Learning

### Prerequisites

To run through below instructions, you need an Azure subscription, an AzureML workspace, a registered data set (i.e. **german-credit**) and an AzureML compute target (i.e. **cpu-cluster**). See instructions on how to create a workspace [here](../../../0_setup/setup.md), register an AzureML dataset and create an AzureML compute target [here](../../../1_concepts/concepts.md).

### Create your first automated ML experiment

Automated machine learning (automated ML) builds high quality machine learning models for you by automating model and hyperparameter selection. Bring a labelled dataset that you want to build a model for, automated ML will give you a high quality machine learning model that you can use for predictions.

If you are new to Data Science, automated ML will help you get jumpstarted by simplifying machine learning model building. It abstracts you from needing to perform model selection, hyperparameter selection and in one step creates a high quality trained model for you to use.

If you are an experienced data scientist, automated ML will help increase your productivity by intelligently performing the model and hyperparameter selection for your training and generates high quality models much quicker than manually specifying several combinations of the parameters and running training jobs. Automated ML provides visibility and access to all the training jobs and the performance characteristics of the models to help you further tune the pipeline if you desire.

### Using Automated Machine Learning

Follow the instructions in the [documentation](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-create-portal-experiments) for a full overview of the user interface.

1. Navigate to the left pane of your workspace. Select Automated ML under the Author section.

   ![Automated ML tab](https://docs.microsoft.com/en-us/azure/machine-learning/service/media/how-to-create-portal-experiments/nav-pane.png).

2. Enter your experiment name, then select a compute from the list of your existing computes or       [create a new compute](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-create-portal-experiments#create-an-experiment).

3. Select a the German credit dataset (**german-credit**) that you have created [before](../../../1-Concepts/2-Datastores-datasets/UI/README.md).

4. Preview data and keep all columns selected for training.

5. Select the training job type: **Classification**

6. Select target column: **Risk**

7. Open “**Advanced settings**”, set the 'Primary metric' to 'AUC_weighted' and training job time to 15 minutes (for the workshop).

8. Hit "**Start**" and wait for the training job to start. You’ll be able to see the models which are created during the run, click on any of the models to open the detailed view of that model, where you can analyze the [graphs and metrics](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-understand-automated-ml).

9. Once the run is completed, click **deploy the best model** to create a deployed endpoint from the model.

To learn more about automated ML, see documentation [here](https://docs.microsoft.com/en-us/azure/machine-learning/service/concept-automated-ml).

### Optional Tasks:
- Once your model has been deployed, follow these [instructions](https://docs.microsoft.com/en-us/power-bi/service-machine-learning-integration) to consume the model from Power BI.

- Try the sample notebooks [here](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/automated-machine-learning).

# Training ML models using the SDK

## Objectives

In the following exercise you will learn to submit training runs using the SDK:
- Train locally on the notebook
- Train remotely on the compute cluster
- User Hyperparameter Tuning to optimize your model
- Use AutoML in the SDK

## Review -- LINKs Prerequisits

To run through below instructions, you need an Azure subscription, an AzureML workspace, a registered data set (i.e. **german-credit**) and an AzureML compute target (i.e. **cpu-cluster**). See instructions on how to create a workspace [here](../../../0-Setup/README.md), register an AzureML dataset [here](../../1-Concepts/2-Datastores-datasets/UI/README.md) and create an AzureML compute target [here](../../1-Concepts/0-Compute/UI/README.md).

## Review --- LINKS Train a model using the AzureML SDK

In this module we train a machine learning model using the AzureML SDK.

1. Training on local compute: [Python SDK](./Python/1-aml-training-and-hyperdrive/1-scikit-learn-local-training-on-notebook-plus-aml-ds-and-log/binayclassification-german-credit-notebook.ipynb) 

2. Training on a remote compute:  [Python SDK](./Python/1-aml-training-and-hyperdrive/2-scikit-learn-remote-training-on-aml-compute-plus-hyperdrive/binayclassification-german-credit-aml-compute-notebook.ipynb)  / [R SDK](./R/README.md)

3. Hyper-parameter optimization:  [Python SDK](./Python/1-aml-training-and-hyperdrive/2-scikit-learn-remote-training-on-aml-compute-plus-hyperdrive/binayclassification-german-credit-aml-compute-notebook.ipynb)

For more details and examples on model training using SDK & hyper-parameter optimization see [here](https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-train-models-with-aml?view=azure-ml-py) and [here](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azure-ml-py).

### Review --- Clone the Git repository to your Compute Instance
For the following parts of the workshop, you are going to work on the notebook environment hosted on the Compute instance you just created. First, you need to clone this git repository onto the workspace.

1. To get started, first navigate to the Jupyter(Lab) instance running on the Compute instance by clicking on the Jupyter(Lab) link shown:

   ![](./media/computes_view.png)

  2. After going through authentication, you will see the Jupyter(Lab) frontend. As you authenticate, make sure to use the same user to log in as was used to create the Compute instance, or else your access will be denied. Next open an Terminal (either by File/New/Terminal, or by just clicking on Terminal from the 'New' drop-down menu)

     ![](./media/terminal_1.png)

     ![](./media/terminal_2.png)

3. In the terminal window clone this repository by typing:
   ```
   $ git clone https://github.com/Sahiep/aml-hands-on-lab.git
   ```

## What's a script run configuration?
A ScriptRunConfig is used to configure the information necessary for submitting a training run as part of an experiment.

You submit your training experiment with a ScriptRunConfig object. This object includes the:

* source_directory: The source directory that contains your training script
* script: The training script to run
* compute_target: The compute target to run on
* environment: The environment to use when running the script
* and some additional configurable options (see the reference documentation for more information)

## Review --- Exercise: Train ML model locally

In the following exercise you will:
- Create an experiment to run
- Create an environment where the script will run
- Create a ScriptRunConfig, which specifies the compute target and environment
- Submit the run
- Wait for the run to complete
- Register the newly trained model

### Review --- Execute the Jupyter Notebook 1-scikit-learn-local-train-on-notebook.....

1. Run the setup notebook to train locally [Python SDK](/sdk/local-compute/setup.ipynb) 
1. Check for your experiment run in the Azure ML Workspace
1. Check your newly registered ML model

## Review --- Exercise: Train ML model remotely + Hyperdrive

In the following exercise you will:
- Create an experiment to run
- Create an environment where the script will run
- Create a ScriptRunConfig, which specifies the compute target and environment
- Submit the run
- Wait for the run to complete
- Register the newly trained model
- *Optional*: Run Hyperdrive to optimize your model

### Review --- Execute the Jupyter Notebook 2-scikit-learn-remote-training.....

1. Run the setup notebook to train remotely ---> LINK [Python SDK](/sdk/local-compute/setup.ipynb) 
1. Check for your experiment run in the Azure ML Workspace
1. Check for your hyperdrive run in the Azure ML Workspace
1. Check your newly registered ML model

## Review -- Train AutoML using the SDK (locally or remote)

### Train an Auto ML model locally

### Train an Auto ML model on a remote compute

 - Run the notebook for AutoML remote compute:  [Python SDK](../SDK/remote-compute/binayclassification-german-credit-autoaml-remote-amlcompute.ipynb)

See also [here](https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-auto-train-models?view=azure-ml-py), for another example of trainig a model using Azure Automated ML.

## The Automated Machine Learning (SDK)

### Prerequisites

To run through below instructions, you need an Azure subscription, an AzureML workspace, a registered data set (i.e. **german-credit**) and an AzureML compute target (i.e. **cpu-cluster**). See instructions on how to create a workspace [here](../../../0_setup/setup.md), register an AzureML dataset and create an AzureML compute target [here](../../../1_concepts/concepts.md).

### Train a model with Azure Automated ML

In this tutorial, you use automated machine learning in Azure Machine Learning to create a classification model to predict credit risk for German credit dataset. This process accepts training data and configuration settings, and automatically iterates through combinations of different feature normalization/standardization methods, models, and hyperparameter settings to arrive at the best model.

![automlflow](./media/flow2.png)

Here we are considering two main scenarios:

### Train an Auto ML model on local compute

1. Run the setup notebook to install automl and onnx-runtime [Python SDK](../SDK/local-compute/setup.ipynb) 
2. Train a model using Automated ML on local compute:  [Python SDK](../SDK/local-compute/binayclassification-german-credit-autoaml-local-compute.ipynb)

### Train an Auto ML model on a remote compute

 - Run the notebook for AutoML remote compute:  [Python SDK](../SDK/remote-compute/binayclassification-german-credit-autoaml-remote-amlcompute.ipynb)

See also [here](https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-auto-train-models?view=azure-ml-py), for another example of trainig a model using Azure Automated ML.
