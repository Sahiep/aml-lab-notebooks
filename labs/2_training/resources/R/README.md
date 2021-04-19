<!-- #region -->
# Training on a remote compute using AML R SDK

This module will show how to use Azure ML with R. The AzureML SDK for R is available today in public preview. The SDK is open-sourced and developed on [GitHub](https://github.com/Azure/azureml-sdk-for-r) and also available on [CRAN](https://cran.r-project.org/web/packages/azuremlsdk/index.html).

In this module we will be using both the Jupyter and the RStudio instances that are installed on the [Compute instance](https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-instance) you set up [earlier](../../../1-Concepts/0-Compute/UI/README.md) in the workshop.

## Setup
Before running through this module, please execute the setup script to make sure all required components are installed by opening a Jupyter terminal window and running the following command in the subdirectory `0-Setup/SDK/R/` of this repository:

```
sudo Rscript 0-setup.R
```

If you get a `"Would you like to install Miniconda? [Y/n]"` prompt please enter `"n"`.

## Explore in Jupyter
From the "Compute instances" tab in [studio](ml.azure.com), open the "Jupyter" link under "Application URI" to launch Jupyter on your compute instance. Navigate to the `2-Training/Code/R/1-explore-r.ipynb` notebook and run through the notebook.

## Train a model on AmlCompute
From the "Compute instances" tab in [studio](ml.azure.com), open the "RStudio" link under "Application URI" to launch RStudio web interface on your compute instance. Once in RStudio, in the bottom right tab "Files" navigate to `code/` and then where you cloned this repo to, for instance `code/aml_workshop_template`. Open `2-Training/Code/2-train-on-amlcompute.R`

Prior to running the script, set the working directory to the current file location using `setwd(dirname)` or Session -> Set Working Directory -> To Source File Location.

<!-- #endregion -->
