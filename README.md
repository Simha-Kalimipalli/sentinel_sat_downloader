# sentinel_sat_downloader

This allows someone to download images from a csv from ESA's Sentinel 2 Scihub

# Downloading_process
Contains 4 functions in **1_sentinel_sat_downloader/1_sentinel_sat_downloader.ipynb** used to download the Sentinel 2 data from ESA Datahub given a set of CSV files
* Directory Function
  * Gets the names of a directory
* Cleans CSV lists Function
  * cleans/splits df of list of images
* Real Name Function
  * function to help find real names of files
* Search string Function
  * searchs esa datahub for image and downsloads it
* Main function
  * Combination of the 4 functions

# DSEN2_process
Contains the code to run Dsen2 with and without original bands on Sentinel 2 images
* **DSEN2_process/dsen_test.ipynb** (without original bands)
* **DSEN2_process/dsen_test-Copy1.ipynb** (with original bands)

# DSEN2_S2LP_process
Contains 4 functions in **DSEN2_S2LP_process/6_DSEN2_application/6_DSEN2_application.ipynb** used to automate running DSen2 on Sentinel 2 images
* Directory Function
  * Gets the names of a directory
* Unzipping Function
  * "unzip the files in the directory
* Moving zipped file function
  * Moving zip files to another location
* Three methods to run  Dsen2 include:
  * Method 1: Typical Ipython method (working)
  * Method 2: Pass string to cmd inside python (not working yet)
  * Method 3: Pass string to run (working)
    * ipython_command_maker function
  
# Estimate_prediction_process
Contains 2 methods to estimate uncertainity
* **auto_examples_jupyter** folder (Sklearn/Forestci method examplars)
  *  plot_mpg_svr.ipynb - Plotting Bagging Regression Error Bars
  *  plot_mpg.ipynb     - Plotting Regression Forest Error Bars
  *  plot_spam.ipynb    - Plotting Classification Forest Error Bars
* **Tensorflow_probability** folder (Tensorflow Probability method)
  *  A_Tour_of_TensorFlow_Probability.ipynb - General Tensorflow probability examplar
  *  Modelling_uncertainty_examplar.ipynb   - Modelling Aleatoric and Epistemic uncertainity in a probability regression Tensorflow probability examplar
  *  Probabilistic_Layers_Regression.ipynb  - Modelling Aleatoric and Epistemic uncertainity in a linear regression Tensorflow probability examplar
  *  regression.ipynb                       - Linear regression and Regression with a deep neural network using for single and multiple inputs
  *  tensorflow_example.ipynb               - An example of Deep Learning Models, Advanced Model Features and methods to Better Model Performance
* **Uncertanity_example** folder ( examplar of both  Sklearn/Forestci  and Tensorflow Probability methods on LAI data
  * Uncertainty_Tensorflow_and_Tensorflow_probability.ipynb - The examplar (to be used in NEON)
