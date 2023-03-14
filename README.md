# sentinel_sat_downloader

This allows someone to download images from a csv from ESA's Sentinel 2 scihub
# Downloading_process
Contains 4 functions used to download the Sentinel 2 data from ESA Datahub given a set of CSV files
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
