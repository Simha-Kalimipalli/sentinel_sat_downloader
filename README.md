# sentinel_sat_downloader

This allows someone to download images from a csv from ESA's Sentinel 2 scihub

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
* DSEN2_process/dsen_test.ipynb (without original bands)
* DSEN2_process/dsen_test-Copy1.ipynb (with original bands)

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
 
 


