# Project: Look at an Airbnb data from (https://osf.io/qyca8/files/z7vy6)
The compressed Airbnb database has been split into 2 files due to size limitation in Github upload.

/////////// PYTHON
#The project aims to look at daily price of a specific property_type (apartments), and to check the distribution of this variable against number of reviews.
#Different bins for prices and review count have been made for ease of comparison.

#Requirements
-Python version 3.10
- Libraries:
	> pandas
	> numpy
	> matplotlib
	> seaborn

# Clone the repository or download files
# Install required libraries: pip install -r 
# Run the master script: airbnb_raw.csv
# Outputs (cleaned CSV, plots, analysis) saved in data/Python_files/ as a compressed file airbnb_clean.csv


/////////// STATA
#The project aims to look at distribution of the daily price of the datasets.

#Requirements
-STATA version used: MP/15.0

# Types of do files
- Complete do file.do
	> contains complete analysis
- Transforming data.do
	> contains the change of the column to ensure numeric functions can be used
- Cleaning, summarizing and visualizing dataset.do
	> contains cleaning of data to remove empty cells. The dropping of values above 
	d_price=220 is used to ensure visual coherence while removing outliers with little 
	impact (5%, but outside appropriate s.d. of the mean). 

# Outputs (cleaned dataset, box plot, analysis do files) saved in data/STATA_files/ as a compressed file 