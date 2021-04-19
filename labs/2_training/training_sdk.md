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

